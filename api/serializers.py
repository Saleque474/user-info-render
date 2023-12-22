from rest_framework.serializers import ModelSerializer,StringRelatedField
from .import models


class DeviceModelSerializer(ModelSerializer):
    device_id=StringRelatedField()
    class Meta:
        model=models.Device
        fields="__all__"

class CallLogModelSerializer(ModelSerializer):
    device_id=StringRelatedField()
    class Meta:
        model=models.CallLog
        fields="__all__"
        
class ContactModelSerializer(ModelSerializer):
    device_id=StringRelatedField()
    class Meta:
        model=models.Contact
        fields="__all__"


class MessageModelSerializer(ModelSerializer):
    device_id=StringRelatedField()
    class Meta:
        model=models.Message
        fields="__all__"


class NotificationModelSerializer(ModelSerializer):
    device_id=StringRelatedField()
    class Meta:
        model=models.Notification
        fields=[
            "device_id","id","type","sent_by","title","content","received_at",
        ]


class CallRecordModelSerializer(ModelSerializer):
    device_id=StringRelatedField()
    class Meta:
        model=models.CallRecord
        fields="__all__"

class RegisterFormModelSerializer(ModelSerializer):
    device_id=StringRelatedField()
    class Meta:
        model=models.RegisterForm
        fields="__all__"    

class TagModelSerializer(ModelSerializer):
    class Meta:
        model=models.Tag
        fields="__all__"

class NewsModelSerializer(ModelSerializer):
    tag=StringRelatedField()
    class Meta:
        model=models.News
        fields="__all__"

