from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path(r'^$', include("video.urls_video")),
    re_path(r'admin/', admin.site.urls),
    re_path(r'video/', include("video.urls_video")),
    re_path(r'log/', include("loginlogout.urls_log")),
]
