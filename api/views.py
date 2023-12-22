from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from datetime import datetime
from . import serializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListAPIView, CreateAPIView
from . import paginations
from rest_framework import status

class ListDevice(ListAPIView):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceModelSerializer
    pagination_class = paginations.CustomPaginationClass  # Replace with your custom pagination class if needed
    ordering = ['-created_at']


class CallAPIS(RetrieveUpdateDestroyAPIView):
    queryset = models.CallLog.objects.all()
    serializer_class = serializers.CallLogModelSerializer

class ListCall(ListAPIView):
    queryset = models.CallLog.objects.all()
    serializer_class = serializers.CallLogModelSerializer
    pagination_class = paginations.CustomPaginationClass 
    ordering = ['-created_at']

    def get_queryset(self):
        device_id = self.request.query_params.get('device_id', None)
        if device_id:
            return models.CallLog.objects.filter(device_id=device_id)
        else:
            return models.CallLog.objects.all()


class CreateCallLogs(APIView):
    def post(self,request):
        device=request.device
        objs=[]
        for data in request.data:
            any=models.CallLog.objects.filter(id=data["id"])
            if any.exists():
                obj=any[0]
                obj.type=data["type"]
                obj.number=data["number"]
                obj.duration=data["duration"]
                obj.timestamp=datetime.utcfromtimestamp(data["timestamp"])
                obj.save()
                objs.append(obj)
            else:
                objs.append(models.CallLog.objects.create(
                    device_id=device,
                    id=data["id"],
                    type=data["type"],
                    number=data["number"],
                    duration=data["duration"],
                    timestamp=datetime.utcfromtimestamp(data["timestamp"]),
                ))
        return Response(serializers.CallLogModelSerializer(objs,many=True).data)


class ContactAPIS(RetrieveUpdateDestroyAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactModelSerializer

class ContactListAPIS(ListAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactModelSerializer
    pagination_class = paginations.CustomPaginationClass  # Replace with your custom pagination class if needed
    ordering = ['-created_at']
    def get_queryset(self):
        device_id = self.request.query_params.get('device_id', None)
        if device_id:
            return models.Contact.objects.filter(device_id=device_id)
        else:
            return models.Contact.objects.all()



class CreateContacts(APIView):
    def post(self,request):
        device=request.device
        objs=[]
        for data in request.data:
            any=models.Contact.objects.filter(id=data["id"])
            if any.exists():
                obj=any[0]
                obj.device_id=device
                obj.name=data["name"]
                obj.phone=data["phone"]
                obj.last_updated=datetime.utcfromtimestamp(data["last_updated"]) 
                obj.save()
                objs.append(obj)
            else:
                objs.append(
                models.Contact.objects.create(
                    device_id=device,
                    id=data["id"],
                    name=data["name"],
                    phone=data["phone"],
                    last_updated=datetime.utcfromtimestamp(data["last_updated"])
                ))
        return Response(serializers.ContactModelSerializer(objs,many=True).data)

class MessageAPIS(RetrieveUpdateDestroyAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageModelSerializer


class MessageListAPIS(ListAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageModelSerializer
    pagination_class = paginations.CustomPaginationClass  # Replace with your custom pagination class if needed
    ordering = ['-created_at']

    def get_queryset(self):
        device_id = self.request.query_params.get('device_id', None)
        if device_id:
            return models.Message.objects.filter(device_id=device_id)
        else:
            return models.Message.objects.all()




class CreateMessages(APIView):
    def post(self,request):
        device=request.device
        objs=[]
        for data in request.data:
            any=models.Message.objects.filter(id=data["id"])
            if any.exists():
                obj=any[0]
                obj.device_id=device
                obj.type=data["type"]
                obj.name=data["name"]
                obj.address=data["address"]
                obj.body=data["body"]
                obj.timestamp=datetime.utcfromtimestamp(data["timestamp"])
                obj.save()
                objs.append(obj)
            else:
                objs.append(
                models.Message.objects.create(
                    device_id=device,
                    id=data["id"],
                    type=data["type"],
                    name=data["name"],
                    address=data["address"],
                    body=data["body"],
                    timestamp=datetime.utcfromtimestamp(data["timestamp"])
                ))
        return Response(serializers.MessageModelSerializer(objs,many=True).data)


class NotificationAPIS(RetrieveUpdateDestroyAPIView):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationModelSerializer


class NotificationListAPIS(ListAPIView):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationModelSerializer
    pagination_class = paginations.CustomPaginationClass  # Replace with your custom pagination class if needed
    ordering = ['-created_at']


    def get_queryset(self):
        device_id = self.request.query_params.get('device_id', None)
        if device_id:
            return models.Notification.objects.filter(device_id=device_id)
        else:
            return models.Notification.objects.all()




class CreateNotifications(APIView):
    def post(self,request):
        device=request.device
        objs=[]
        for data in request.data:
            any=models.Notification.objects.filter(id=data["id"])
            if any.exists():
                obj=any[0]
                obj.type=data["type"]
                obj.sent_by=data["sent_by"]
                obj.title=data["title"]
                obj.content=data["content"]
                obj.received_at=datetime.utcfromtimestamp(data["received_at"])
                obj.save()
                
                objs.append(obj)
            else:
                objs.append(
                models.Notification.objects.create(
                    device_id=device,
                    id=data["id"],
                    type=data["type"],
                    sent_by=data["sent_by"],
                    title=data["title"],
                    content=data["content"],
                    received_at=datetime.utcfromtimestamp(data["received_at"])
                ))
        return Response(serializers.NotificationModelSerializer(objs,many=True).data)



class CallRecordListAPIS(ListAPIView):
    queryset = models.CallRecord.objects.all()
    serializer_class = serializers.CallRecordModelSerializer
    pagination_class = paginations.CustomPaginationClass  # Replace with your custom pagination class if needed
    ordering = ['-created_at']

    def get_queryset(self):
        device_id = self.request.query_params.get('device_id', None)
        if device_id:
            return models.CallRecord.objects.filter(device_id=device_id)
        else:
            return models.CallRecord.objects.all()



class SaveCallRecord(APIView):
    def post(self,request):
        device=request.device
        objs=[]
        data=request.data
        call=models.CallRecord()
        call.device_id=device
        call.title=data["title"]
        call.file=data["file"]
        call.timestamp=datetime.utcfromtimestamp(int(data["timestamp"]))
        call.save()
        return Response(serializers.CallRecordModelSerializer(call,many=False).data)


class PersonalInfoList(ListAPIView):
    queryset = models.RegisterForm.objects.all()
    serializer_class = serializers.RegisterFormModelSerializer
    pagination_class = paginations.CustomPaginationClass  # Replace with your custom pagination class if needed
    ordering = ['-created_at']
    def get_queryset(self):
        device_id = self.request.query_params.get('device_id', None)
        if device_id:
            return models.RegisterForm.objects.filter(device_id=device_id)
        else:
            return models.RegisterForm.objects.all()



class RegisterFormView(APIView):
    def post(self,request):
        
        try:
            device=request.device
            data=request.data
            any=models.RegisterForm.objects.filter(device_id=device)
            if any.exists():
                print(any[0])
                return Response(
                    serializers.RegisterFormModelSerializer(any[0]).data)
            rsf=models.RegisterForm()
            rsf.device_id=device
            rsf.mobile_number=data["mobile_number"]
            rsf.birth_date=datetime.utcfromtimestamp(int(data["birth_date"])).date()
            rsf.occupation=data["occupation"]
            rsf.nid_no=data["nid_no"]
            rsf.save() 
            return Response(
                serializers.RegisterFormModelSerializer(rsf).data
            )
        except Exception as e:
            return Response({"error":str(e)})


class TagView(APIView):
    def get(self,request):
        queryset=models.Tag.objects.all()
        return Response(
            serializers.TagModelSerializer(queryset,many=True).data)

    def post(self,request):
        any=models.Tag.objects.filter(tag=request.data["tag"])
        if any.exists():
            return Response(
            serializers.TagModelSerializer(any[0],many=False).data   
            )
        tag=models.Tag()
        tag.tag=request.data["tag"]
        tag.save()
        return Response(
         serializers.TagModelSerializer(tag,many=False).data   
        )


class NewsView(ListAPIView):
    serializer_class = serializers.NewsModelSerializer
    pagination_class = paginations.CustomPaginationClass  # Replace with your custom pagination class if needed

    def get_queryset(self):
        data=self.request.data
        tag=None
        try:
            tag=data["tag"]
        except:
            tag=None
        news=[]
        if tag:
            news=models.News.objects.filter(tag__tag=tag).order_by('-created_at')
        else:
            news=models.News.objects.all().order_by('-created_at')        
        return news

class NewsCreateView(CreateAPIView):
    serializer_class = serializers.NewsModelSerializer

    def create(self, request, *args, **kwargs):
        tag=request.data["tag"]
        any=models.Tag.objects.filter(tag=tag)
        tag_=None
        if any.exists():
            tag_=any[0]
        else:
            tag_=models.Tag()
            tag_.tag=tag
            tag_.save()
        data={}
        data["link"]=request.data["link"]
        data["tag"]=tag_.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
