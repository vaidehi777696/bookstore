from typing import Self
from django.db import models

# Create your models here.
class Booksavailable(models.Model):
 def __str__(Self)-> str:
  return Self.bookname
 
 bookname=models.CharField(max_length=225)
 authorname=models.CharField(max_length=225)
 '''
 publisher=models.CharField(max_length=225)
price=models.IntegerField(null=True)
language=models.CharField(max_length=225)
sub_title=models.CharField(max_length=225)
'''

 