from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
import uuid

from apps.products.models import Products

User = get_user_model()

# Create your models here.
class Billing(models.Model):
    class BillingReceiptTypeChoices(models.TextChoices):
        PICKUP = 'Самовывоз', _('Самовывоз')
        DELIVERY = 'Доставка', _('Доставка')
        UNKNOWN = 'Неизвестно', _('Неизвестно')
    class BillingStatusChoices(models.TextChoices):
        INBACKET = 'В корзине', _('В корзине')
        ISSUED = 'Оформлен', _('Оформлен')
        PAID = 'Оплачен', _('Оплачен')
        DELIVERED = 'Доставлен', _('Доставлен')
        Return = 'Возврат', _('Возврат')
        UNKNOWN = 'Неизвестно', _('Неизвестно')
    class BillingPaymentStatusChoices(models.TextChoices):
        PAID = 'Оплачен', _('Оплачен')
        NOTPAID = 'Не оплачен', _('Не оплачен')
        ERROR = 'Ошибка', _('Ошибка')
        PERFORMED = 'В исполнении', _('В исполнении')
    class BillingPaymentChoices(models.TextChoices):
        CASH_IN_STORE = 'Наличными в магазине', _('Наличными в магазине')
        CASH_TO_COURIER = 'Наличными курьеру', _('Наличными курьеру')
        PAYMENT_CARD_TO_COURIER = 'Оплата картой курьеру', _('Оплата картой курьеру')
        PAYMENT_TRANSFER = 'Оплата переводом', _('Оплата переводом')
        PAYMENT_INSTALLMENTS = 'Оплата в рассрочку', _('Оплата в рассрочку')
        PAYMENT_VISA = 'Картой Visa', _('Картой Visa')
        MBANK = 'Мбанк', _('Мбанк')
        OPTIMA24 = 'Optima 24', _('Optima 24')
        ODENGI = 'О! Деньги',_('О! Деньги')
        BAKAI24 = 'Bakai 24',_('Bakai 24')
        ERROR = 'Ошибка', _('Ошибка')
        UNKNOWN = 'Неизвестно', _('Неизвестно')
    class BillingTypeChoices(models.TextChoices):
        LEADGENERATION = 'Лидогенерация', _('Лидогенерация')
        BILLING = 'Биллинг', _('Биллинг')
    billing_type = models.CharField(
        max_length=100, choices=BillingTypeChoices.choices,
        default=BillingTypeChoices.LEADGENERATION,
        verbose_name='Тип биллинга'
    )
    billing_receipt_type = models.CharField(
        max_length=100, choices=BillingReceiptTypeChoices.choices,
        default=BillingReceiptTypeChoices.UNKNOWN,
        verbose_name='Вид получения товара',
    )
    billing_status = models.CharField(
        max_length=100, choices=BillingStatusChoices.choices,
        default=BillingStatusChoices.INBACKET,
        verbose_name='Статус заказа'
    )
    billing_payment_status = models.CharField(
        max_length=100, choices=BillingPaymentStatusChoices.choices,
        default=BillingPaymentStatusChoices.PERFORMED,
        verbose_name='Статус оплаты'
    )
    billing_payment = models.CharField(
        max_length=100, choices=BillingPaymentChoices.choices,
        default=BillingPaymentChoices.UNKNOWN,
        verbose_name='Способы оплаты'
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        related_name="billing_user",
        verbose_name="Пользователь",
        blank=True, null=True
    )
    email = models.EmailField(
        verbose_name="Почта",
        blank=True, null=True
    )
    first_name = models.CharField(
        max_length=255, verbose_name="Имя",
        blank=True, null=True
    )
    last_name = models.CharField(
        max_length=255, verbose_name="Фамилия",
        blank=True, null=True
    )
    phone = models.CharField(
        max_length=255, verbose_name="Телефонный номер",
        blank=True, null=True
    )
    payment_code = models.CharField(
        max_length=20, unique=True,
        verbose_name="Код оплаты биллинга",
        blank=True, null=True
    )
    country = models.CharField(
        max_length=255, 
        verbose_name="Страна",
        blank=True, null=True,
        default="Кыргызстан"
    )
    city = models.CharField(
        max_length=255, 
        verbose_name="Город",
        blank=True, null=True,
        default="Ош"
    )
    region = models.CharField(
        max_length=255,
        verbose_name="Регион",
        blank=True, null=True
    )
    street = models.CharField(
        max_length=255, 
        verbose_name="Улица",
        blank=True, null=True
    )
    apartment = models.CharField(
        max_length=255,
        verbose_name="Квартира",
        blank=True, null=True
    )
    zip_code = models.CharField(
        max_length=20,
        verbose_name="Индекс",
        blank=True, null=True
    )
    delivery_price = models.PositiveIntegerField(
        verbose_name="Стоимость доставки",
        default=0, blank=True, null=True
    )
    discount_price = models.IntegerField(
        verbose_name="Скидка",
        default=0, blank=True, null=True
    )
    delivery_date_time = models.DateField(
        verbose_name="Дата время доставки",
        blank=True, null=True
    )
    client_gave_money = models.IntegerField(
        verbose_name="Клиент дал денег",
        default=0, blank=True, null=True
    )
    change_price = models.IntegerField(
        verbose_name="Сдача клиенту",
        default=0, blank=True, null=True
    )
    total_price = models.PositiveIntegerField(
        verbose_name="Итоговая сумма",
        default=0, blank=True, null=True
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания биллинга"
    )

    def __str__(self):
        return f"{self.billing_receipt_type} {self.payment_code}"
    
    def save(self, *args, **kwargs):
        if not self.payment_code:
            self.payment_code = str(uuid.uuid4().int)[:10]  
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Биллинг"
        verbose_name_plural = "Биллинги"

class BillingProduct(models.Model):
    billing = models.ForeignKey(
        Billing, on_delete=models.CASCADE, 
        related_name='billing_products', verbose_name="Биллинг"
    )
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, 
        related_name='products_billings', verbose_name="Товар"
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество товаров"
    )
    price = models.PositiveBigIntegerField(
        verbose_name="Итоговая цена товара", default=0
    )
    status = models.BooleanField(
        verbose_name="Статус", default=False
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )

    def __str__(self):
        return f"{self.billing} - {self.product} ({self.quantity} шт.)"
    
    class Meta:
        verbose_name = "Биллинг товара"
        verbose_name_plural = "Биллинги товаров"
        
class SaleSummary(Billing):
    class Meta:
        proxy = True
        verbose_name = 'Отчет продажа товар'
        verbose_name_plural = 'Отчеты продажи товаров'