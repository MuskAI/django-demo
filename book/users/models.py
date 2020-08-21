from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    """
    用户
    """
    APIkey = models.IntegerField(max_length=30,verbose_name='APIkey',default='abcde')
    money = models.IntegerField(default=10,verbose_name='余额')
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
class Book(models.Model):
    """
    书籍信息
    """
    title = models.CharField(max_length=30,verbose_name='书名',default='')
    isbn = models.CharField(max_length=30,verbose_name='isbn',default='')

    class Meta:
        verbose_name = '书籍信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title