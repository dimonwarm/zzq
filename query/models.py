from django.db import models

class Result(models.Model):
	num=models.CharField(max_length=20,primary_key=True)
	name=models.CharField(max_length=20)
	date=models.CharField(max_length=20)