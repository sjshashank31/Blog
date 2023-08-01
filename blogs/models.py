from django.db import models
import itertools
from django.utils.text import slugify


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=1083)
    slug = models.CharField(max_length=1100)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True)

    def _generate_slug(self):
        title = str(self.title).split()
        title = "-".join(title)
        slug_candidate = slug_original = slugify(title, allow_unicode=True)
        for i in itertools.count(1):
            if not Blog.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def __str__(self):
        return self.title

    def slug_save(self, *args, **kwargs):
        self._generate_slug()

        super().save(*args, **kwargs)





