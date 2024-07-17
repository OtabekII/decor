from .models import Blog
from django.shortcuts import redirect

def isOwner(func):
    def wrapper(request, id, *args, **kwargs):
        post = Blog.objects.get(id=id)
        if post.author!=request.user.id:
            return redirect('index')
        return func(request, id, *args, **kwargs)
    return wrapper