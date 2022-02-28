from django.shortcuts import redirect, render, get_object_or_404
from .forms import Postform, Commentform, FreeCommentform, FreePostform
from .models import Post, FreePost
from django.core.paginator import Paginator

def home(request):
  # posts = Post.objects.all()
  posts = Post.objects.filter().order_by('-date')
  paginator = Paginator(posts, 5)
  pagenum = request.GET.get('page')
  posts = paginator.get_page(pagenum)
  return render(request, 'index.html', {'posts': posts})


def postcreate(request):
  # request method가 POST일 경우
    # 입력값 저장
  if request.method == 'POST' or request.method == 'FILES':
    form = Postform(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')
  # request method가 GET일 경우
    # form 입력 html 띄우기
  else:
    form = Postform()
  return render(request, 'post_form.html', {'form' : form})

def freehome(request):
    # posts = Post.objects.all()
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'free_index.html', {'freeposts': freeposts})


def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostform(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user            # user 추가!
            unfinished.save()
            return redirect('freehome')
    else:
        form = FreePostform()
    return render(request, 'free_post_form.html', {'form':form})


def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentform()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form': comment_form})


def new_freecomment(request, post_id):
    filled_form = FreeCommentform(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)


def detail(request, post_id):
  post_detail = get_object_or_404(Post, pk=post_id)
  comment_form = Commentform()
  return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form': comment_form})

# 댓글 저장
def new_comment(request, post_id):
  filled_form = Commentform(request.POST)
  if filled_form.is_valid():
    finished_form=filled_form.save(commit=False)
    finished_form.post = get_object_or_404(Post, pk=post_id)
    finished_form.save()
  return redirect('detail', post_id)

