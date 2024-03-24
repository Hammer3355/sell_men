from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  # null=True, blank=True - Если поле не заполнено то значение null
    featured_image = models.ImageField(upload_to='projects/%Y/%m/%d/', default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.ImageField(default=0)
    vote_ratio = models.ImageField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
