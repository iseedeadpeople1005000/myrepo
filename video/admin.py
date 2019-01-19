from django.contrib import admin
from video.models import Video, Comment


class VideoInline(admin.StackedInline):  # указывает связь
    model = Comment
    extra = 2  # колличество коментариев под статьей


class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
    list_filter = ['Video_date']


admin.site.register(Video, VideoAdmin)