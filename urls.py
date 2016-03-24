from django.conf.urls import url
from views import RootFolderView
from views import SubFolderView
urlpatterns = [
    url(r'^$', RootFolderView.as_view()),
    url(r'^subfolder/(?P<pk>[\w]+)/$', SubFolderView.as_view()),
]