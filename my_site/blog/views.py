from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView, DeleteView
from django.views import View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.

# all_posts = [
    # {
    #     "slug": "hike-in-the-mountains",
    #     "image": "uyghur.jpg",
    #     "author": "Uyghur",
    #     "date": date(2021, 7, 21),
    #     "title": "Mountain Hiking",
    #     "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
    #     "content": """
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #     """
    # },
    # {
    #     "slug": "programming-is-fun",
    #     "image": "coding.jpg",
    #     "author": "Uyghur",
    #     "date": date(2022, 3, 10),
    #     "title": "Programming Is Great!",
    #     "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
    #     "content": """
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #     """
    # },
    # {
    #     "slug": "into-the-woods",
    #     "image": "woods.jpg",
    #     "author": "Uyghur",
    #     "date": date(2020, 8, 5),
    #     "title": "Nature At Its Best",
    #     "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
    #     "content": """
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #     """
    # }
# ]

class StartingPageView(ListView):
    template_name  = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     # sorted_posts = sorted(all_posts,key=get_date)
#     # latest_posts = sorted_posts[-3:]

#     return render(request, "blog/index.html",{
#         "posts": latest_posts
#     })

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# def posts(request):
#     all_posts = Post.objects.all().order_by('-date')
#     return  render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })



class SinglePostView(View):
    template_name = "blog/post-detail.html"
    model = Post
    
    def get(self, request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)
        
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if  comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            
            return HttpResponseRedirect(reverse("post_detail_page",args=[slug]))
        
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        
        return render(request, "blog/post-detail.html", context)
        
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context

# def post_detail(request,slug):
#     all_posts = Post.objects.all().order_by('-date')
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html",{
#         "post": identified_post,
#         "post_tags":identified_post.tags.all()
#     })