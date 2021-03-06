from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView
from .models import Askpost,AskComment
from .forms import PostForm,CommentForm
from django.db.models.query_utils import Q

class AskView(ListView):
    model = Askpost
    context_object_name = 'askposts'
    template_name = 'ask/ask.html'
    ordering = ['-date_posted']
    paginate_by = 2                    # 每頁只顯示四個貼文

class AskDetailView(DetailView):
    model = Askpost

class AskPostView(LoginRequiredMixin,CreateView):
    model = Askpost
    form_class = PostForm #forms.py裡的PostForm已經有fields了，所以只要留這行
    template_name = 'ask/ask_post.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AskCommentView(LoginRequiredMixin,CreateView):
    model = AskComment
    form_class = CommentForm
    template_name = 'ask/ask_comment.html'
    #fields = '__all__'
    
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)
   
def askSearch(request):
    searchTerm = request.GET.get('searchTerm')
    askposts = Askpost.objects.filter(Q(title__icontains = searchTerm) | Q(content__icontains=searchTerm))
    context = {'askposts':askposts,'searchTerm':searchTerm}
    return render(request, 'ask/askSearch.html',context)