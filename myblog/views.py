from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from .models import Post

class MainView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        paginator = Paginator(post, 6)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'myblog/home.html', context={
            'page_obj': page_obj
        })