from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    emailid = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=15, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.name

class Enquiry(models.Model):
    name = models.CharField(max_length=150, null=True)
    mobile = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    age = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=150, null=True)
    price = models.CharField(max_length=100, null=True)
    unit = models.CharField(max_length=50, null=True)
    purchasedate = models.DateField(null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=150, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=10, null=True)
    plan = models.CharField(max_length=100, null=True)
    joindate = models.DateField(null=True)
    initamount = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=150, null=True)
    amount = models.CharField(max_length=15, null=True)
    duration = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True , default=uuid.uuid4)
    craeted_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Question(BaseModel):

    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question
class Answer(BaseModel):
    question = models.ForeignKey(Question , related_name='questionS', on_delete = models.CASCADE)
    answer = models.CharField(max_length=100)


    def __str__(self):
        return self.answer





