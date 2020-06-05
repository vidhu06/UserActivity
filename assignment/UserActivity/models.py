from django.db import models

class User(models.Model):
    id = models.CharField(primary_key= True,max_length = 255)
    real_name = models.TextField(max_length = 255)
    tz = models.TextField(max_length = 255)

class ActivityPeriod(models.Model):
    id = models.AutoField(primary_key = True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User,default=1,on_delete = models.SET_DEFAULT)
