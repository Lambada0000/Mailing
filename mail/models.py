from django.db import models


NULLABLE = {"blank": True, "null": True}

frequency_choices = (
    ("Ежедневно", "Ежедневно"),
    ("Еженедельно", "Еженедельно"),
    ("Ежемесячно", "Ежемесячно"),
)

status_choices = (
    ("Создана", "Создана"),
    ("Запущена", "Запущена"),
    ("Завершена", "Завершена"),
)


class Client(models.Model):
    email = models.EmailField(
        verbose_name="Email",
        help_text="Введите email клиента",
        unique=True,
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Имя клиента",
        help_text="Введите имя клиента",
    )
    comment = models.TextField(
        verbose_name="Комментарий",
        help_text="Введите комментарий к клиенту",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.email} ({self.name})"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Newsletter(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название рассылки", default="Рассылка", **NULLABLE
    )
    start_date = models.DateField(verbose_name="Дата и время первой рассылки")
    frequency = models.CharField(
        max_length=50,
        verbose_name="Периодичность",
        default="Ежедневно",
        choices=frequency_choices,
    )
    status = models.CharField(
        max_length=50,
        verbose_name="Статус рассылки",
        default="Создана",
        choices=status_choices,
    )
    clients = models.ManyToManyField(
        Client, verbose_name="Клиенты", related_name="clients"
    )
    message = models.OneToOneField(
        "Message",
        verbose_name="Сообщение",
        related_name="message",
        on_delete=models.SET_NULL,
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class Message(models.Model):
    subject = models.CharField(max_length=100, verbose_name="Тема сообщения")
    text = models.TextField(verbose_name="Текст сообщения")

    def __str__(self):
        return f"{self.subject}: {self.text}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Attempt(models.Model):
    date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время последней рассылки"
    )
    mailing_status = models.BooleanField(
        default=False, verbose_name="Успешна ли попытка"
    )
    server_response = models.TextField(
        default=False, verbose_name="Ответ почтового сервера"
    )
    newsletter = models.ForeignKey(
        Newsletter,
        verbose_name="Рассылка",
        on_delete=models.CASCADE,
        related_name="newsletter",
    )

    def __str__(self):
        return f"Попытка рассылки {self.date}: {self.mailing_status}"

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
