from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm, PostForm


# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comment = Comment.objects.all()
    form = CommentForm()
    if request.method == "GET":
        return render(request, "post_detail.html", {'post': post, 'form': form, 'comment': comment})
    else:
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment = comment.save()
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=post.slug)

        else:
            return HttpResponse("Invalid Form")


def Add_Post(request):
    form = PostForm()
    if request.method == "GET":
        return render(request, "add_post.html", {'form': form})
    else:
        post = PostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect("home")



def delete(request,email,slug):
    post = Post.objects.get(slug=slug)
    comment = Comment.objects.get(email=email)
    comment.delete()
    return redirect("post_detail", slug = post.slug)