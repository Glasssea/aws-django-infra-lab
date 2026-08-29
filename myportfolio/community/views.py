from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Articles, Category, Recommend, Comment
from django.urls import reverse
# Create your views here.

def index(request):
    notice_list = Articles.objects.filter(category_id=1)
    article_list = Articles.objects.exclude(category_id=1)
    category_list = Category.objects.all()
    # comment_list = Comment.objects.all().count()
    # recommend_list = Recommend.objects.all().count()
    print(notice_list)
    print(article_list)
    print(category)
    return render(request, 'community/index.html', {'notice_list':notice_list, 'article_list':article_list, 'category_list':category_list})

def category(request, category_id):
    category_list = Category.objects.all()
    print(category_list)
    article_list = Articles.objects.filter(category_id=category_id)
    return render(request, 'community/category.html', {"article_list":article_list, "category_list":category_list})


def write(request):
    category_list = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        title, content, user, category_id = data['title'], data['content'], data['user'], data['category_id']
        
        article = Articles.objects.create(title=title, content=content, user_id=user, category_id_id=category_id)
        article.save()
        return redirect(reverse('community:index', ))
    

    return render(request, 'community/write.html', {'category_list':category_list})

def detail(request, article_id):
    article = Articles.objects.prefetch_related('comment_set').get(id=article_id)
    comment = Comment.objects.filter(article_id=article_id)
    

    return render(request, 'community/detail.html', {'article':article, 'comment':comment})

def update(request, article_id):
    category_list = Category.objects.all()
    
    if article_id:
        article = get_object_or_404(Articles, id=article_id)
    else:
        article_id = None

    if request.method == 'POST':
        data = request.POST
        title, content, user, category_id = data['title'], data['content'], data['user'], data['category_id']
        
        category = Category.objects.get(id=category_id)
        
        article.title = title
        article.content = content
        article.category_id = category
        
        
        article.save()
        return redirect(reverse('community:detail', args=[article_id]))
    

    return render(request, 'community/update.html', {'category_list':category_list, 'article':article})

def delete(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    article.delete()
    return redirect('community:index')