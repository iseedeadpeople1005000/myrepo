from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Video, Comment
from . import forms
from django.template.context_processors import csrf
from django.contrib import auth


def addlike(request):
    if request.GET:
        idlike = request.GET["addlike"]
        video = Video.objects.get(id=idlike)
        video.Video_likes += 1
        video.save()
    return HttpResponse(video.Video_likes)


def hello(request):
    print(request.GET["addlike"])
    names = ["Egor", "Petr", "Fedor", "Elena"]
    return render(request, "video.html", {"content": names})

def showall(request):
    videos = Video.objects.all()
    content = []#[(video,[(com,user),(),(),(),...]),(),(),(),.....]
    for vid in videos:
        list_com = []
        comments = Comment.objects.filter(Comment_Video_id = vid.id)
        for com in comments:
            user = User.objects.get(id = com.Comment_User_id)
            list_com.append((com, user))
        content.append((vid, list_com))
    return render(request, "video.html", {"content":content,
                                          "username":auth.get_user(request).username})

def showone(request, video_id):
    video = Video.objects.get(id = video_id)
    comment = Comment.objects.filter(Comment_Video_id=video_id)
    users = []
    args = {}
    args.update(csrf(request))
    comment_form = forms.CommentForm
    for com in comment:
        user = User.objects.get(id=com.Comment_User_id)
        users.append(user)
    return render(request, "showone.html", {"video":video,
                                            "comment":list(zip(comment,users)),
                                            "form":comment_form,
                                            "csrf":args,
                                            "username":auth.get_user(request).username})

def addcom(request, video_id):
    if request.POST:
        if auth.get_user(request).username:
            forma = forms.CommentForm(request.POST)
            if forma.is_valid():
                comment = forma.save(commit=False)
                comment.Comment_Video = Video.objects.get(id=video_id)
                comment.Comment_User = User.objects.get(id=request.user.id)
                forma.save()
                return redirect("/video/get/" + str(video_id) + "/")
        else:
            return redirect("/log/register/")




# Create your views here.
