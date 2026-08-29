from django.urls import path


from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>', views.category, name='category'),
    path('write', views.write, name='write'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('update/<int:article_id>/', views.update, name='update'),
    path('delete/<int:article_id>/', views.delete, name='delete')
    # path('<str:>')
]
