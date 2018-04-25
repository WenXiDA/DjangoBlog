from django.db import models

# Create your models here.
class Blog(models.Model):
    """docstring for [object Object]."""
    user_name = models.CharField(null = True, blank = True, max_length = 50 )
    name = models.CharField(null = True, blank = True, max_length = 50 )
    summary = models.TextField(null =True)
    content = models.TextField(null =True)
    def __str__(self):
        return self.name

class User(models.Model):
    """docstring for [object Object]."""

    name = models.CharField(null = True, blank = True, max_length = 50)
    passwd = models.CharField(null = True,blank = True, max_length = 50)
    email = models.CharField(null = True, blank = True, max_length = 50)
    def __str__(self):
        return self.name

class Comment(models.Model):
    """docstring for [object Object]."""

    user_name = models.CharField(null = True, blank = True, max_length = 50)
    belong = models.ForeignKey(to=Blog, null=True,blank=True,related_name="under_comment",on_delete=models.CASCADE)
    comment = models.TextField(null = True)

    def __str__(self):
        return self.comment[:100]
