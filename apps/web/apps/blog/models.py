import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Blog(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        unique=True,
        null=False,
        blank=False
    )
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish', editable=False)
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/', blank=True, null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    draft = models.BooleanField(default=True)


    class Meta:
        ordering = ('-publish', '-updated', '-created')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)    

    def get_absolute_url(self):
        return reverse('blog-detail',args=[self.id])

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)
