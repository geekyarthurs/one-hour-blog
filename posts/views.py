from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import CreateView
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from .forms import updateForm


class Home(LoginRequiredMixin, View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'posts/home.html', {'posts': posts})


class PostCreate(LoginRequiredMixin, CreateView):
    url = 'blog:home'
    model = Post
    fields = ['title', 'content', 'author']
    template_name = "posts/create_post.html"


@login_required
def delete(request, pk):
    Post.objects.filter(pk=pk).delete()
    return redirect('blog:home')


def post(request, pk):
    post = Post.objects.get(pk=pk)

    if (request.method == 'POST'):
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)

            comment.post = post
            comment.save()

            return render(request, "posts/post.html", {
                'post': post,
                'commentform': CommentForm()
            })

        else:
            return render(request, "posts/post.html", {
                'post': post,
                'commentform': commentForm
            })

    commentForm = CommentForm()

    return render(request, "posts/post.html", {
        'post': post,
        'commentform': commentForm
    })



def updatePost(request,pk):
    update_item = Post.objects.get(pk=pk)

    form = updateForm(instance=update_item)
    if request.method == 'POST':
        form = updateForm(request.POST,instance=update_item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')


        else:
            form = updateForm()




    context = {

            'forms' : form

    }

    return render(request,'posts/update.html',context) 