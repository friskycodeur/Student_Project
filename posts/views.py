from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

def home(request):
    return render(request,'posts/home.html')

class PostListView(ListView):
    model = Post
    template_name='posts/doubts.html'
    context_object_name = 'posts'
    ordering=['-post_date']
    paginate_by= 4




class UserPostListView(ListView):
    model = Post
    template_name='posts/user_posts.html'
    context_object_name = 'posts'
    ordering=['-post_date']
    paginate_by= 4

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-post_date')

class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text=request.POST.get('text')
            comment=Comment.objects.create(post=post,author=request.user,text=text)
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
        return render(request, 'posts/comment_form.html', {'form': form})


def search(request):
    query = request.GET.get('query', None)
    allposts=Post.objects.filter(title__icontains=query)
    params={'allposts':allposts,}
    return render(request,'posts/search.html',params)

