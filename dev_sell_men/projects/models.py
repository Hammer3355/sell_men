from django.db import models
from users.models import Profile


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name="Тег")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Владелец")
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")  # null=True, blank=True - Если поле не заполнено то значение null
    featured_image = models.ImageField(upload_to='projects/%Y/%m/%d/', default="default.jpg", verbose_name="Изображение")
    demo_link = models.CharField(max_length=2000, null=True, blank=True, verbose_name="Ссылка на демо")
    source_link = models.CharField(max_length=2000, null=True, blank=True, verbose_name="Ссылка на источник")
    tags = models.ManyToManyField('Tag', blank=True, verbose_name="Теги")
    vote_total = models.IntegerField(default=0, verbose_name="Количество голосов")
    vote_ratio = models.IntegerField(default=0, verbose_name="Рейтинг")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created']
