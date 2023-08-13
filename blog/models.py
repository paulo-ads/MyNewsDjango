from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=155)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='post_images', default='default-image.png')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

