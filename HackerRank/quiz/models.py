from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
    
class Questions(models.Model):
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)   
    options=(
        ('easy','easy'),
        ('medium','medium'),
        ('hard','hard')
           ) 
    mode=models.CharField(max_length=200,choices=options,default='easy')
    mark=models.PositiveIntegerField(default=2)
    question=models.CharField(max_length=200)

    
    @property
    def choices(self):
        return Answers.objects.filter(question=self)
    
    @property
    def answer(self):
        return Answers.objects.get(question=self,is_correct=True)

    def __str__(self) -> str:
        return self.question
    

class Answers(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    options=models.CharField(max_length=200) 
    is_correct=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.options 

class QuizRecord(models.Model):
    marks_obtained=models.PositiveIntegerField()  
    right_answer_count=models.PositiveIntegerField()
    wrong_answer_count=models.PositiveIntegerField()
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    date=models.DateField(auto_now_add=True)

