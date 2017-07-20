from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import CreateView
from . import views
urlpatterns = [
        url(r'^bucketlists/$',views.CreateView.as_view(), name="create"),
        url(r'^$', views.BucketlistView.as_view(), name ="list")
    ]

#urlpatterns = format_suffix_patterns(urlpatterns)