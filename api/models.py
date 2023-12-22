from django.db import models
from django.utils import timezone

class Device(models.Model):
    device_id=models.UUIDField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self) -> str:
        return str(self.device_id) 


class CallLog(models.Model):
    id=models.CharField(primary_key=True,max_length=30,)
    device_id=models.ForeignKey(Device,on_delete=models.PROTECT)
    type=models.CharField(max_length=15)
    number=models.CharField(max_length=15)
    duration=models.CharField(max_length=15)
    timestamp=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)


class Contact(models.Model):
    device_id=models.ForeignKey(Device,on_delete=models.PROTECT)
    id=models.CharField(primary_key=True,max_length=30,)
    name=models.CharField(max_length=63)
    phone=models.CharField(max_length=15)
    last_updated=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)


class Message(models.Model):
    device_id=models.ForeignKey(Device,on_delete=models.PROTECT)
    id=models.CharField(primary_key=True,max_length=30,)
    type=models.CharField(max_length=15)
    name=models.CharField(max_length=63)
    address=models.CharField(max_length=127)
    body=models.TextField(max_length=5000,)
    timestamp=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)


class Notification(models.Model):
    device_id=models.ForeignKey(Device,on_delete=models.PROTECT)
    id=models.CharField(primary_key=True,max_length=30,)
    type=models.CharField(max_length=15,default="notification")
    sent_by=models.CharField(max_length=63)
    title=models.CharField(max_length=127)
    content=models.TextField(max_length=5000)
    received_at=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)



class CallRecord(models.Model):
    device_id=models.ForeignKey(Device,on_delete=models.PROTECT)
    title=models.CharField(max_length=127)
    file=models.FileField(blank=True)
    timestamp=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)


class RegisterForm(models.Model):
    device_id=models.ForeignKey(Device,on_delete=models.PROTECT)
    mobile_number=models.CharField(max_length=18)
    birth_date=models.DateField()
    occupation=models.CharField(max_length=27)
    nid_no=models.CharField(max_length=27)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)


class Tag(models.Model):
    tag=models.CharField(max_length=57)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.tag

class News(models.Model):
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    link=models.URLField()
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)

