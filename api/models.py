from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(u'姓名', max_length=100, default='匿名')
	sex = models.CharField('性别', max_length=100, default='匿名')
	sid = models.CharField('学号', max_length=100, default='0')

	def __str__(self):
		return '{} {} {}'.format(self.name, self.sex, self.sid)