from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views


urlpatterns = [
    path('', views.home,name='blog-home'),
    path('doubts/', PostListView.as_view(),name='doubts'),
    path('search/',views.search,name='search'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name='post-delete'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]