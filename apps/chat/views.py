from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from apps.settings.models import Setting
from apps.users.models import User
from apps.chat.models import ChatMessage, Room
# Create your views here.

@login_required
def chat(request):
    current_user = request.user
    user_id = request.GET.get('user_id')

    users = User.objects.exclude(id=current_user.id).annotate(
        unread_messages=Count(
            'sent_messages',
            filter=Q(sent_messages__receiver=current_user, sent_messages__is_read=False)
        )
    )

    if user_id:
        other_user = get_object_or_404(User, id=user_id)

        if request.method == 'POST' and 'send_message' in request.POST:
            content = request.POST.get('content', '').strip()
            if content:
                ChatMessage.objects.create(
                    sender=current_user,
                    receiver=other_user,
                    content=content
                )
            return redirect(f"{request.path}?user_id={user_id}")

        messages = ChatMessage.objects.filter(
            Q(sender=current_user, receiver=other_user) |
            Q(sender=other_user, receiver=current_user)
        ).order_by('timestamp')

        ChatMessage.objects.filter(sender=other_user, receiver=current_user, is_read=False).update(is_read=True)

        context = {
            'users': users,
            'other_user': other_user,
            'messages': messages,
        }
        return render(request, 'applications/app/apps-chat.html', context)

    else:
        recent_users = ChatMessage.objects.filter(
            Q(sender=current_user) | Q(receiver=current_user)
        ).values('sender', 'receiver').distinct()

        context = {
            'users': users,
            'recent_users': recent_users,
        }
        return render(request, 'applications/app/apps-chat.html', context)
  
  
def chat_message_delete(request, message_id):
    if request.method != "POST":
        return JsonResponse({'error': 'Неверный метод запроса.'}, status=405)

    try:
        # Загружаем данные из POST-запроса
        data = json.loads(request.body)
        delete_for_all = data.get('delete_for_all', False)
        
        # Ищем сообщение
        message = get_object_or_404(ChatMessage, id=message_id)

        # Проверка прав: пользователь должен быть отправителем или получателем
        if request.user != message.sender and request.user != message.recipient:
            return JsonResponse({'error': 'Нет прав для удаления.'}, status=403)

        if delete_for_all:
            # Удалить для всех
            message.delete()
            return JsonResponse({'success': 'Сообщение удалено для всех.'})
        else:
            # Удалить только для текущего пользователя
            if request.user == message.sender:
                message.is_deleted_for_sender = True
            elif request.user == message.recipient:
                message.is_deleted_for_recipient = True
            message.save()
            return JsonResponse({'success': 'Сообщение удалено для вас.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
