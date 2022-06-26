from django.contrib import admin
from django.urls import path
from myApp.views import *
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index-page'),
    path('load_region/',load_zone,name='load-region'),
    path('load_org/',load_org,name='load-org'),
    path('load_post/',load_post,name='load-post'),
    path('statistics/',static,name='static'),
]
admin.site.site_header = "Muzaffar"
handler404 = error_404

