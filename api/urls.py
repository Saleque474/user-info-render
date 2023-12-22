from django.urls import path
from . import views
urlpatterns = [
    
 path("save-call-logs/",views.CreateCallLogs.as_view(),),
 path("call-log-apis/<pk>/",views.CallAPIS.as_view(),),
 path("all-call/",views.ListCall.as_view(),),
 path("save-contacts/",views.CreateContacts.as_view(),),
 path("all-contacts/",views.ContactListAPIS.as_view(),),
 path("contact-apis/<pk>/",views.ContactAPIS.as_view(),),
 path("all-messages/",views.MessageListAPIS.as_view(),),
 path("save-messages/",views.CreateMessages.as_view(),),
 path("message-apis/<pk>/",views.MessageAPIS.as_view(),),
 path("save-notifications/",views.CreateNotifications.as_view(),),
 path("all-notifications/",views.NotificationListAPIS.as_view(),),
 path("notification-apis/<pk>/",views.NotificationAPIS.as_view(),),
 path("upload-record/",views.SaveCallRecord.as_view(),),
 path("all-call-record/",views.CallRecordListAPIS.as_view(),),
 path("register/",views.RegisterFormView.as_view(),),
 path("all-personal-info/",views.PersonalInfoList.as_view(),),
 path("tags/",views.TagView.as_view(),),
 path("news/",views.NewsView.as_view(),),
 path("create-news/",views.NewsCreateView.as_view(),),
 path("devices/",views.ListDevice.as_view(),),


]