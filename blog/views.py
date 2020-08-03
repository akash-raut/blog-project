from django.shortcuts import render


posts = [
    {
        'author': 'Akash Raut',
        'title': 'Blog Post1',
        'content': 'First Post Content',
        'date_posted': 'August 02, 2020'
    },
    {
        'author': 'Plash Raut',
        'title': 'Blog Post2',
        'content': 'Second Post Content',
        'date_posted': 'August 02, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

