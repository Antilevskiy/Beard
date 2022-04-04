from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    street = models.CharField(max_length=50, default='')
    suite = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    zipcode = models.CharField(max_length=50, default='')
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    phone = models.CharField(max_length=50, default='')
    website = models.CharField(max_length=50, default='')
    company_name = models.CharField(max_length=50, default='')
    company_catch_phrase = models.CharField(max_length=100, default='')
    bs = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'{self.id}. {self.username}'


class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='')
    completed = models.BooleanField()


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='')
    body = models.TextField(max_length=200, default='')


class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='')


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    body = models.TextField(max_length=200, default='')


class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='')
    url = models.TextField(max_length=50,
                           default='https://placebeard.it/480/640')
    thumbnail_url = models.TextField(max_length=50,
                                     default='https://placebeard.it/120/160')
