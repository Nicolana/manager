from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(u'姓名', max_length=100, default='匿名')
	sex = models.CharField('性别', max_length=100, default='匿名')
	sid = models.CharField('学号', max_length=100, default='0')

	def __str__(self):
		return '{} {} {}'.format(self.name, self.sex, self.sid)

class User(models.Model):
	username = models.CharField('用户名', max_length=225, default="", unique=True)
	password = models.CharField('密码', max_length=225, default="")
	nickname = models.CharField('用户昵称', max_length=255, default="--")
	avatar   = models.CharField('头像', max_length=255, default="")
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.username

