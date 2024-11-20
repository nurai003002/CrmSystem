from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from apps.settings.models import Setting
from apps.users.models import User
from apps.chat.models import ChatMessage, Room
# Create your views here.

@login_required
def chat(request):
    current_user = request.user
    user_id = request.GET.get('user_id')

    if user_id:
        other_user = get_object_or_404(User, id=user_id)
        if request.method == 'POST' and 'send_message' in request.POST:
            content = request.POST.get('content', '').strip()
            if content:  # Проверяем, что сообщение не пустое
                ChatMessage.objects.create(
                    sender=current_user,
                    receiver=other_user,
                    content=content
                )
            return redirect(f"{request.path}?user_id={user_id}")

        # Получение сообщений между текущим и другим пользователем
        messages = ChatMessage.objects.filter(
            Q(sender=current_user, receiver=other_user) |
            Q(sender=other_user, receiver=current_user)
        ).order_by('timestamp')

        context = {
            'other_user': other_user,
            'messages': messages,
        }
        return render(request, 'applications/app/apps-chat.html', context)

    else:
        # Список пользователей, с которыми есть переписки
        messages = ChatMessage.objects.filter(
            Q(sender=current_user) | Q(receiver=current_user)
        ).order_by('-timestamp')
        users = set()

        for message in messages:
            if message.sender != current_user:
                users.add(message.sender)
            if message.receiver != current_user:
                users.add(message.receiver)

        return render(request, 'applications/app/apps-chat.html', {'users': users})
