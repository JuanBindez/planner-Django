from django.shortcuts import render
from .models import Post
from .models import ContaApagar

# Create your views here.
def hello_planer(request):
    list_posts = Post.objects.all()
    data = {'posts': list_posts }

    return render(request, 'index.html', data)


def hello_contas(request):
    list_posts = ContaApagar.objects.all()
    data = {'posts': list_posts }

    return render(request, 'conta.html', data)
