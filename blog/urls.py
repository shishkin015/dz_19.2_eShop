from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogUpdateView, BlogDetailView, BlogDeleteView, toggle_activity, IndexView

app_name = BlogConfig.name

urlpatterns =[
    path('', IndexView.as_view(), name='index'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list/', BlogListView.as_view(), name='list'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='update'),
    path('view/<int:pk>', BlogDetailView.as_view(), name='view'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
    path('aktivity/<int:pk>/', toggle_activity, name='toggle_activity'),

]