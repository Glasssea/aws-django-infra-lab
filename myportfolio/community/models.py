from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import importlib
User = get_user_model()


from django.core import validators
# Create your models here.

class Articles(models.Model):
    id = models.AutoField(primary_key=True) # 아이디
    title = models.CharField("제목", max_length=255, validators=[validators.MinLengthValidator(2, "최소 세 글자 이상 입력해주세요.")]) # 게시글 제목
    content = models.TextField("내용", validators=[validators.MinLengthValidator(10, "최소 열 글자 이상 입력해주세요.")])
    category_id = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, db_column='category_id') #카테고리 이게 맞아 이걸 기준으로 해보기
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 유저이름이 되어야 함.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20) # 카테고리 이름

class Recommend(models.Model): # 추천
    id = models.AutoField(primary_key=True) # 일련번호
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    article_id = models.ForeignKey("Articles", on_delete=models.CASCADE, db_column='article_id')
    created_at = models.DateTimeField(auto_now_add=True) # 좋아요 취소 하면 그냥 delete 시켜버린다는 마인드

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    article_id = models.ForeignKey("Articles", on_delete=models.CASCADE, db_column='article_id')
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
