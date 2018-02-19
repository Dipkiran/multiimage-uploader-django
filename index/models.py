from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save

from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse("user:detail", kwargs={"id":self.id})

def get_image_filename(instance, filename):
    title = instance.post.id
    return "%s/%s" % (title, filename)



class Images(models.Model):
    post = models.ForeignKey(Post, default=None,on_delete=models.CASCADE,)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image', blank=True,)
