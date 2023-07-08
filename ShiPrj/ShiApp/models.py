from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture = models.ImageField()
    password = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    status = models.TextField()
    school_name = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=50)
    joined_date = models.DateField()

class Follow(models.Model):
    follower_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    followee_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateField()
    media = models.ImageField()

class Comments(models.Model):
    content = models.TextField()
    time_commented = models.TimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class Post_like(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Post_type(models.Model):
    type = models.CharField(max_length=30)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class Hashtags(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    hashtag_name = models.CharField(max_length=50)

class Notification(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    type = models.CharField(max_length=30)

class Messages(models.Model):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateField()
