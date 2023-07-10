from django.urls import path
from .views import blog, blog_detail

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('detail_page/<int:day>/<int:month>/<int:year>/<slug:slug>/', blog_detail, name='blog_detail'),
]
