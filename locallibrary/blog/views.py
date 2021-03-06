from django.shortcuts import render,reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post,Comment,Category
from .forms import PostForm,CommentForm
from django.db.models.query_utils import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger,InvalidPage

# area_board = {'area':['Americas','Asia','Europe','Africa','Oceania'],'path':['media/uploads/icon/americas.png','media/uploads/icon/asia.png','media/uploads/icon/europe.png',
            # 'media/uploads/icon/oceania.png','media/uploads/icon/africa.png','media/uploads/icon/oceania.png']}
area_board = ['Americas','Asia','Europe','Africa','Oceania']
# area_path = ['media/uploads/icon/americas.png','media/uploads/icon/asia.png','media/uploads/icon/europe.png',
#             'media/uploads/icon/oceania.png','media/uploads/icon/africa.png','media/uploads/icon/oceania.png']
categories = ['Course reviews','Daily life','Foods','Entertainment','Laws','Transportation','Customs,traditions',
            'Expenses','Accomodation','Travel','School reviews','Climate']
posts = Post.objects.all()
# def home(request):
    # context = {
        # 'posts':Post.objects.all()
    # }
    # return render(request, 'blog/home.html',context)
    # image = models.ImageField(default = 'default.jpg', upload_to='page_pics')
    # return render(request, 'blog/mainpage_new.html',context)

# 管理貼文呈現的狀態
class PostListView(ListView):
    model = Post                         # 以Post為基礎建立
    template_name = 'blog/mainpage_new.html' # <app>/<model>_<viewtype>.html 尋找樣板顯示(顯示主頁)
    context_object_name = 'posts'
    
    ordering = ['-date_posted']          # 讓貼文以時間排序
    paginate_by = 4                    # 每頁只顯示四個貼文
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['area_board'] = area_board
        # print(context)
        print(**kwargs)
        return context



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
    form_class = PostForm #forms.py裡的PostForm已經有fields了，所以只要留這行
    template_name = 'blog/add_post.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # fields = ['title','content']


def articleSearch (request):
    searchTerm=request.GET.get('searchTerm')
    articles=Post.objects.filter(Q(title__icontains=searchTerm))
    context={'articles':articles, 'searchTerm': searchTerm}
    return render(request, 'blog/articleSearch.html', context)
    


class AddCommentView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    #fields = '__all__'
    
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        form.instance.name = self.request.user
        return super().form_valid(form)

def AreaView(request,areas):
    area_posts = Post.objects.filter(area=areas).order_by('-date_posted')
    paginator=Paginator(area_posts, 4 )
    #count_number=visit_num.objects.get()
    #count_number.viewed()
    current_page=request.GET.get('page')
    
    try:
        post_s=paginator.page(current_page)
    except PageNotAnInteger:
        post_s=paginator.page(1)
    except EmptyPage:
        post_s=paginator.page(paginator.num_pages)

    return render(request,'blog/area.html',{'areas':areas,'area_posts':area_posts,'post_s':post_s,'categories':categories})


def AreaCategoryView(request,areas,cats):
    area_posts = Post.objects.filter(area=areas,tags__name__in=[cats.replace('-',' ')]).order_by('-date_posted')
    paginator=Paginator(area_posts, 4 )
    #count_number=visit_num.objects.get()
    #count_number.viewed()
    current_page=request.GET.get('page')
    try:
        post_s=paginator.page(current_page)
    except PageNotAnInteger:
        post_s=paginator.page(1)
    except EmptyPage:
        post_s=paginator.page(paginator.num_pages)

    return render(request,'blog/area_category.html',{'areas':areas,'cats':cats,'area_posts':area_posts,'categories':categories,'post_s':post_s})

    

def areaArticleSearch (request):
    searchTerm=request.GET.get('searchTerm')
    articles=Post.objects.filter(Q(category__icontains=searchTerm))
    context={'articles':articles, 'searchTerm': searchTerm}
    return render(request, 'blog/areaArticleSearch.html', context)

def news(request):
    return render(request, 'newsboard/news.html')



def index(request):
    posts_list=Post.objects.all().order_by('-id')
    paginator=Paginator(posts_list , 1 )
    #count_number=visit_num.objects.get()
    #count_number.viewed()
    current_page=request.GET.get('page')
    
    try:
        post_s=paginator.page(current_page)
    except PageNotAnInteger:
        post_s=paginator.page(1)
    except EmptyPage:
        post_s=paginator.page(paginator.num_pages)

    return render(request,'blog/mainpage_new.html',{'post_s':post_s})
    
