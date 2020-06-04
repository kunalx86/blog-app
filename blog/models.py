from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    '''
    This model represents comment on a post.
    Field #1: post- Foriegn Key reference to the post itself
    Field #2: user- Foreign Key refernce to identify the commenting user
    Field #3: body- The comment itself. Textfield
    Field #4: date_posted- Just a date on when posted
    Field #5?: parent- Reference to itself to refer to replies on each comment (not sure about this one) 
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.TextField(blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'On {self.post.title} by {self.author.first_name}'