from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    # return render(request, 'blog/home.html',context)
    image = models.ImageField(default = 'default.jpg', upload_to='page_pics')
    return render(request, 'blog/mainPage.html',context)

# 管理貼文呈現的狀態
class PostListView(ListView):
    model = Post                         # 以Post為基礎建立
    template_name = 'blog/mainPage.html' # <app>/<model>_<viewtype>.html 尋找樣板顯示(顯示主頁)
    context_object_name = 'posts'
    ordering = ['-date_posted']          # 讓貼文以時間排序
    # paginate_by = 2                    # 每頁指顯示兩個貼文

# 管理點入貼文後的詳細資訊
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html',{'title':'about'})
    # return HttpResponse('<h1>Blog About</h1>')

class AddPostView(LoginRequiredMixin,CreateView):
    model = Post
    # form_class = PostForm
    template_name = 'blog/add_post.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    fields = ['title','content']
    
