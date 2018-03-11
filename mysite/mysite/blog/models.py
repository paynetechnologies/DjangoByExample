# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    '''
    author: This field is ForeignKey. This field defines a many-to-one relationship. We are
    telling Django that each post is written by a user and a user can write several posts. For
    this field, Django will create a foreign key in the database using the primary key of the
    related model. In this case, we are relying on the User model of the Django authentication
    system. We specify the name of the reverse relationship, from User to Post, with the
    related_name attribute.
    '''
    author = models.ForeignKey(User, related_name='blog_posts', on_delete='PROTECT')

    body = models.TextField()

    # This datetime indicates when the post was published. We use Django's timezone
    # now method as default value. This is just a timezone-aware datetime.now.
    publish = models.DateTimeField(default=timezone.now)

    # This datetime indicates when the post was created. Since we are using
    # auto_now_add here, the date will be saved automatically when creating an object
    created = models.DateTimeField(auto_now_add=True)

    # This datetime indicates the last time the post has been updated. Since we are 
    # using auto_now here, the date will be updated automatically when saving an object
    updated = models.DateTimeField(auto_now=True)

    # This is a field to show the status of a post. We use a choices parameter, so the 
    # value of this field can only be set to one of the given choices
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # sort results by the publish field in descending order by default when we query the database. 
    # We specify descending order by using the negative prefix.
    class Meta:
        ordering = ('-publish',)
    
    # default human-readable representation of the object.
    def __str__(self):
        return self.title