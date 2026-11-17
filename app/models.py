from django.db import models
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
    )

    description = models.CharField(
        max_length=500,
        verbose_name="Краткое содержание"
    )
    image = models.ImageField(
        upload_to="blog/",
        null=True,
        blank=True,
        verbose_name="Изображение"
    )
    content = models.TextField(
        verbose_name="Полное содержание"
    )

    posted = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        verbose_name="Опубликована"
    )

    author = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Автор"
    )

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(
        verbose_name="Текст комментария"
    )
    date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        verbose_name="Дата добавления"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    post = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        verbose_name="Статья"
    )

    def __str__(self):
        return f"{self.author.username}: {self.text[:30]}"

admin.site.register(Blog)
admin.site.register(Comment)
