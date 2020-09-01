from django.shortcuts import render,reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from django.db.models.query_utils import Q
from .models import Newsarticle
from .forms import Articleform

# def newsarticle(request):
#     newsarticles=Newsarticle.objects.all()
#     context={'newsarticles':newsarticles}
#     return render(request,'newsboard/news.html', context)

# 管理點入貼文後的詳細資訊
class Newshome(ListView):
    model = Newsarticle
    context_object_name = 'newsarticles'
    template_name = 'newsboard/news.html'
    ordering = ['-pubDateTime']
    paginate_by = 2 

class ArticleDetailView(DetailView):
    model = Newsarticle
    template_name = 'newsboard/article_detail.html'

def about(request):
    return render(request, 'blog/about.html',{'title':'about'})
    # return HttpResponse('<h1>Blog About</h1>')

def news(request):
    return render(request, 'newsboard/news.html',{'title':'News'})

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Newsarticle
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Newsarticle
    form_class = Articleform
    template_name = 'newsboard/article_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        newsarticle = self.get_object()
        if self.request.user == newsarticle.author:
            return True
        return False

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Newsarticle
    success_url = '/'

    def test_func(self):
        newsarticle = self.get_object()
        if self.request.user == newsarticle.author:
            return True
        return False

class AddArticleView(LoginRequiredMixin,CreateView):
    model = Newsarticle
    # form_class = PostForm
    template_name = 'newsboard/add_article.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    fields = ['title','body']

def article_search (request):
    searchTerm=request.GET.get('searchTerm')
    articles=Newsarticle.objects.filter(Q(title__icontains=searchTerm) | Q(body__icontains=searchTerm))
    context={'articles':articles, 'searchTerm': searchTerm}
    return render(request, 'newsboard/article_search.html', context)
    