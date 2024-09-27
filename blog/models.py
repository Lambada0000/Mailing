from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    content = models.TextField(
        verbose_name="Содержание статьи",
        help_text="Введите содержание",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    views = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
    )
    publication_date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата публикации",
        help_text="Укажите дату публикации",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
