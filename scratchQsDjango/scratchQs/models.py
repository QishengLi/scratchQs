from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=50, unique=True)
	def __str__(self):
		return 'Category: %s' % (self.name)

class Question(models.Model):
	# category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
	title = models.CharField(max_length=200, unique=True)
	content = models.TextField()
	category = models.CharField(max_length=100)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return 'question: %s' % (self.title)

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
	content = models.TextField()
	votes = models.IntegerField(default=0)
	def __str__(self):
		return 'Question: %s (Content: %s)' % (self.question, self.content)

# filter by answer, question=question.object
# "use artist.objects.get(id=1)" to get the object