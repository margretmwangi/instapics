from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    liked = models.ManyToManyField(User,default=None,blank=True , related_name='liked')

    def __str__(self):
        return self.caption
    @property   
    def num_likes(self):
        return self.liked.all().count()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

LIKE_CHOICES=(
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like',max_length=10)

    def __str__(self):
        return str(self.post)

class Comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content =  models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post)