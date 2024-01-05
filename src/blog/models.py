from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager

from blog.utils import validate_title

User = get_user_model()


class Post(models.Model):
    title = models.CharField(validators=[validate_title], max_length=128, unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    likes = models.ManyToManyField(User, related_name="liked_posts")
    tags = TaggableManager()

    @property
    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
