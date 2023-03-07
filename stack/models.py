from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

class Questions(models.Model):
    question=models.CharField(max_length=200)
    image=models.ImageField(upload_to="image",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    

    @property
    def fetch_answers(self):
        answer=self.answers_set.all().annotate(up_count=Count('up_vote')).order_by('-up_count')
        return answer

    def __str__(self):
        return self.question

class Answers(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    up_vote=models.ManyToManyField(User,related_name="upvotes") 

    def __str__(self):
        return self.answer
