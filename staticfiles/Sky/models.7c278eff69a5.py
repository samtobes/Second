from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES=(
    ("Breaking","Breaking"),
    ("Entertainment","Entertainment"),
    ("Politics","Politics")
)

class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="news_images")
    other_image = models.ImageField(upload_to="other_images",blank=True,null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="News"

    def __str__(self):
        return self.title

class Subscribers(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name_plural="Subscribers"

    def __str__(self):
        return self.email