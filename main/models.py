from django.db import models


class Article(models.Model):
    picture = models.ImageField(upload_to='static/pictures')
    title = models.CharField('Name', max_length=100)
    body = models.TextField('Article')
    date = models.DateTimeField('Time')

    def __str__(self):
        return self.title

    @property
    def picture_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url




