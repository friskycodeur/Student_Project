from django.urls import path
from .views import LectureListView,BookListView,CourseListView
from . import views


urlpatterns = [
    path('books/', BookListView.as_view(),name='books'),
    path('lectures/', LectureListView.as_view(),name='lectures'),
    path('courses/', CourseListView.as_view(),name='courses'),   
]