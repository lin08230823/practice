from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import WBUser,WeiBo
# Create your views here.



@login_required
def homepage(request):
    user = get_object_or_404(WBUser, id=request.user.id)
    wbs = WeiBo.objects.filter(user__in=user.followers.all()).order_by('-time_create')[:10]
    return render(request, 'weibo/homepage.html',{
        'user': user,
        'wbs': wbs
    })


def user_page(request):
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    user = get_object_or_404(WBUser, id=request.user.id)
    wbs = WeiBo.objects.filter(user=wb_user).order_by("-time_create")
    return render(request,'weibo/user_page.html',{
        'wb_user': wb_user,
        'wbs': wbs,
        'user': user
    })

def wb_update(request):
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    msg = request.POST.get('msg')
    wb = wb_user.update(msg)
    return HttpResponse(render(request, 'weibo/new_wb.html',{
        'wb':wb
    }))

def wb_comment(request):
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    msg = request.POST.get('msg')
    wid = request.POST.get('wid')
    wb = get_object_or_404(WeiBo, id=wid)
    comment = wb.comment_this(user=wb_user,text=msg)
    return HttpResponse(render(request, 'weibo/new_comm.html',{
        'comm': comment
    }))

def wb_forward(request):
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    msg = request.POST.get('msg')
    wid = request.POST.get('wid')
    wb = get_object_or_404(WeiBo, id=wid)
    new_wb = wb_user.forward(wb)
    if msg:
        new_wb.comment_this(user=wb_user, text=msg)
    response = redirect('wb:upage')
    response['Location']+='?uid={uid}'.format(uid=wb_user.id)
    return response

def user_follow(request):
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    user = get_object_or_404(WBUser, id=request.user.id)
    user.follow(wb_user)
    return HttpResponse()

def user_unfollow(request):
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    user = get_object_or_404(WBUser, id=request.user.id)
    user.unfollow(wb_user)
    return HttpResponse()