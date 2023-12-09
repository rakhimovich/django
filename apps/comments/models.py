from django.db import models
from django.contrib.auth.models import User

from apps.blogs.models import Blog


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        verbose_name="Блог",
        related_name="comments"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    text = models.CharField(
        max_length=500,
        verbose_name="Текст",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время добавления",
    )

    def __str__(self):
        return f"{self.user} - {self.blog.title}"
    

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
