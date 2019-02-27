from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class Notice(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(unique=True, blank=True)
    Description=models.TextField(max_length=500)
    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Notice.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def get_absoulate_url(self):
        return reverse('notice_details', args=[self.slug])



class Sociallink(models.Model):
    name= models.CharField(max_length=100)
    link=models.URLField(max_length=300)
    def __str__(self):
        return self.name
