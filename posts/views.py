from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from posts.models import Post


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def index(request):
    order_by = request.GET.get('order_by', 'date_created')
    # order_by = if order_by == 'date_created' then 'date_created' else '-date_created'
    posts = Post.objects.order_by(order_by)
    context = {'posts': posts, 'order_by': order_by}
    return render(request, 'index.html', context)


@login_required
def add_post(request):
    content = request.POST['content']
    Post.objects.create(content=content, author=request.user)
    return HttpResponseRedirect(reverse('index'))


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # if post.author != request.user:
    #   return HttpResponseRedirect(reverse('index'))
    post.delete()
    return HttpResponseRedirect(reverse('index'))
