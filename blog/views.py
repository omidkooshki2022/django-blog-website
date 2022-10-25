from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy

from .forms import NewPostForm
from .models import Post


class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/add_post.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/add_post.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('posts_list')

# Create your views here.
# def post_list_view(request):
#     #posts = Post.objects.all()
#     posts = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html',  {'posts_list': posts})

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except ObjectDoesNotExist:
#     #     post= None
#     return render(request, 'blog/post_detail.html', {'post':post})

# def add_post_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#             #form = NewPostForm()
#     else:
#         form = NewPostForm()
#
#     return render(request, 'blog/add_post.html', context={'add_post_form': form})
    # if request.method == 'POST':
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     user = User.objects.all()[0]
    #     Post.objects.create(title=post_title, text=post_text, author=user, status='pub')
    # else:
    #     print('get request')
    # return render(request, 'blog/add_post.html')

# def update_post_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#
#     return render(request, 'blog/add_post.html', context={'add_post_form': form})

# def delete_post_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == "POST":
#         post.delete()
#         return redirect('posts_list')

#     return render(request, 'blog/delete_post.html', context={'post':post})
