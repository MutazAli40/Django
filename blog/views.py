from django.shortcuts import render,  get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
#def post_list(request):
#    post_list = Post.objects.all()
#    paginator = Paginator(post_list, 3)
#    page_number = request.GET.get('page', 1)
#
#   try:
#       posts = paginator.get_page(page_number)
#    except PageNotAnInteger:
#        posts = paginator.page(1)    
#    except EmptyPage:
#        posts = paginator.page(paginator.num_pages)    
#    return render(request, 'blog/post/list.html', {'posts': posts})

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request, 'blog/post/detail.html', {'post': post})
  