from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from core.models import Video, Comment
from userauths.models import Profile
from django.views.decorators.csrf import csrf_exempt
from channel.models import Channel
from django.db.models import Count
from django.db.models import Q
from taggit.models import Tag

from django.core.exceptions import ObjectDoesNotExist


def index(request):
    video= Video.objects.filter(visibility = "public")
    context= {
        "video": video,
    }
    return render(request, 'index.html', context)

def videoDetail(request, pk):
    video = Video.objects.get(id=pk)
    channel = Channel.objects.get(user=video.user)
    
    channel.total_views = channel.total_views + 1
    channel.save()

    video.views = video.views + 1
    video.save()

    # Suggesting Video
    video_tags_id = video.tags.values_list("id", flat=True)
    similar_videos = Video.objects.filter(tags__in=video_tags_id).exclude(id=video.id)
    similar_videos = similar_videos.annotate(same_tags=Count("tags")).order_by("-same_tags", "-date")[:25]

    # Getting all comment related to a video
    comment = Comment.objects.filter(active=True, video=video).order_by("-date")
    print('******************************')
    print(video.id)
    print('******************************')
    # print(similar_videos.id)
    print('******************************')

    context = {
        "video":video,
        "channel":channel,
        "comment":comment,
        "similar_videos":similar_videos,
    }
    return render(request, "video.html", context)



def save_video(request, video_id):
    video = Video.objects.get(id=video_id)

    user = request.user.profile
    # user = Profile.objects.get(user=request.user)

    if video in user.saved_videos.all():
        user.saved_videos.remove(video)
    else:
        user.saved_videos.add(video)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))





def ajax_save_comment(request):
    if request.method=="POST":
        pk= request.POST.get("id")
        comment= request.POST.get("comment")
        video= Video.objects.get(id=pk)
        user= request.user
        
        new_comment= Comment.objects.create(comment=comment, user=user, video=video)
        print(new_comment.active)
        new_comment.active = True
        print(new_comment.active)
        new_comment.save()
        
        response= "comment posted"
        return HttpResponse(response)
    
    
@csrf_exempt
def ajax_delete_comment(request):
    if request.method=="POST":
        # id= request.POST.get("cid")
        # comment = Comment.objects.get(id=id)
        # comment.delete()
        # return JsonResponse({"status":1})
        
        try:
            comment_id = request.POST.get("cid")
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return JsonResponse({"status": 1})
        except ObjectDoesNotExist:
            return JsonResponse({"status": 0, "message": "Comment not found."})
    
    else:
        return JsonResponse({"status":0})


def add_new_subscribers(request, id):
    subscribers= Channel.objects.get(id=id)
    user= request.user
    
    if user in subscribers.subscribers.all():
        subscribers.subscribers.remove(user)
        response= "subscribe"
        return JsonResponse(response, safe= False, status= 200)
    
    else:
        subscribers.subscribers.add(user)
        response= "unsubscribe"
        return JsonResponse(response, safe= False, status= 200)
    
def load_channel_subs(request, id):
    subscribers= Channel.objects.get(id=id)
    sub_lists= list(subscribers.subscribers.values())
    return JsonResponse(sub_lists, safe= False, status= 200)
    
    
    




def add_new_like(request, id):
    video = Video.objects.get(id=id)
    user= request.user
    
    if user in video.likes.all():
        video.likes.remove(user)
        like_response= "like"
        return JsonResponse(like_response, safe= False, status= 200)
    
    else:
        video.likes.add(user)
        like_response= "Dislike"
        return JsonResponse(like_response, safe= False, status= 200)
    
def load_video_likes(request, id):
    video = Video.objects.get(id=id)
    likes_lists= list(video.likes.values())
    return JsonResponse(likes_lists, safe= False, status= 200)
    
    
    
def searchView(request):
    video = Video.objects.filter(visibility="public").order_by("-date")
    query = request.GET.get("q")
    if query:
        video = video.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)
        ).distinct()
    
    context = {
        "video":video,
        "query":query,

    }
    return render(request, "search.html", context)



def tag_list(request, tag_slug=None):
    video = Video.objects.filter(visibility="public").order_by("-date")

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        video = video.filter(tags__in=[tag])

    context = {
    "video":video,
    "tag":tag,

    }
    return render(request, "tags.html", context)



def trending(request):
    video = Video.objects.filter(visibility="public").order_by("-views")
    context = {
        "video":video
    }
    return render(request, "trending.html", context)



def liked_videos(request):
    user= request.user
    video= Video.objects.filter(likes=user.id)
    
    
    context= {
        "video": video
    }
    return render(request, "liked_video.html", context)


def saved_videos(request):
    
    profile= Profile.objects.get(user=request.user.id)
    
    video= profile.saved_videos.all()
    
    print(video)
    
    context= {
        "video": video
    }
    return render(request, "saved-video.html", context)