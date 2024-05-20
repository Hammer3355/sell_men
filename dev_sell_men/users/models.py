from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Имя")
    email = models.EmailField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True, verbose_name="Имя пользователя")
    short_intro = models.CharField(max_length=200, null=True, blank=True, verbose_name="Краткое описание")
    bio = models.TextField(null=True, blank=True, verbose_name="О себе")
    profile_image = models.ImageField(upload_to='profiles/', default="profiles/user-default.png", verbose_name="Аватар")
    social_ytube = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ссылка на ютуб")
    social_website = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ссылка на веб сайт")
    social_telegram = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ссылка на телеграм")
    social_vk = models.CharField(max_length=200, null=True, blank=True, verbose_name="Ссылка на вконтакте")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Владелец")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'






