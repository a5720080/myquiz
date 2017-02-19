from django.db import models

class Exam(models.Model):
   name = models.CharField(max_length=150)
   description = models.TextField(null=True, blank=True)
   published = models.BooleanField(default=False)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)

   def __str__(self):
     return self.name

class Quiz(models.Model):
   exam = models.ForeignKey(Exam)
   quiz_name = models.CharField(max_length=200)

   def __str__(self):
     return self.quiz_name 

class Choice(models.Model):
   quiz = models.ForeignKey(Quiz)
   choice_name = models.CharField(max_length=200)
   corrected = models.BooleanField(default=False)

   def __str__(self):
     return self.choice_name
