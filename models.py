from django.db import models

# Create your models here.
from django.db import models

class login(models.Model):
    username=models.CharField(max_length=60)
    password=models.CharField(max_length=60)
    type=models.CharField(max_length=70)

class user(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    name=models.CharField(max_length=60)
    DOB=models.DateField()
    place=models.CharField(max_length=60)
    post=models.CharField(max_length=60)
    pin=models.BigIntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=60)
    image=models.FileField()

class feedback(models.Model):
    lid=models.ForeignKey(user,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=1000)
    date=models.DateField()

class expert(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    DOB = models.DateField()
    place = models.CharField(max_length=60)
    post = models.CharField(max_length=60)
    pin = models.BigIntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=60)
    gender=models.CharField(max_length=60)


class complaint(models.Model):
    lid=models.ForeignKey(user,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    date=models.DateField()

class rating(models.Model):
    lid=models.ForeignKey(user,on_delete=models.CASCADE)
    rating=models.CharField(max_length=100)
    date=models.DateField()
class classvideos(models.Model):
    eid=models.ForeignKey(expert,on_delete=models.CASCADE)
    description=models.CharField(max_length=100)
    video=models.FileField()
    date=models.DateField()

class exam(models.Model):
    eid=models.ForeignKey(expert,on_delete=models.CASCADE)
    examname=models.CharField(max_length=50)
    details=models.CharField(max_length=60)
    date=models.DateField()
    level=models.CharField(max_length=20)


class answer_details(models.Model):
    question=models.FileField()

    answer=models.CharField(max_length=100)

    option1=models.CharField(max_length=100)

    option2=models.CharField(max_length=100)

    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)


    type=models.CharField(max_length=50)
    Exid=models.ForeignKey(exam,on_delete=models.CASCADE)




class attendexam(models.Model):
    qid=models.ForeignKey(answer_details,on_delete=models.CASCADE)
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    mark=models.CharField(max_length=100)

class instructions(models.Model):
    topic=models.CharField(max_length=100)
    instruction=models.TextField()
    date=models.DateField()



class flash_card(models.Model):

    image=models.FileField()
    text=models.CharField(max_length=100)
    EXPERT = models.ForeignKey(expert, on_delete=models.CASCADE)


