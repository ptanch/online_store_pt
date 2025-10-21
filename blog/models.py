from django.db import models


class Blog(models.Model):
    """Класс для представления блога"""
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое', blank=True, null=True)
    preview = models.ImageField(upload_to='blog/photo', blank=True, null=True, verbose_name='Предварительный просмотр',)
    creation_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False)
    views_number = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ['title', 'creation_date']

    def __str__(self):
        return self.title
