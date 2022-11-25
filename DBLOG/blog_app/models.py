from django.db import models


class ModelPost(models.Model):
    title = models.CharField('Заголовок записи', max_length=100, null=False)
    description = models.TextField(null=True)
    link = models.TextField(null=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['time_create']
