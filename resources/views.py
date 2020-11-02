from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView
from .models import Book,Lecture,Course
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class BookListView(ListView):
    model = Book
    template_name='resources/books.html'
    context_object_name = 'books'
    paginate_by= 4

class LectureListView(ListView):
    model = Lecture
    template_name='resources/lectures.html'
    context_object_name = 'lectures'
    paginate_by= 4

class CourseListView(ListView):
    model = Course          
    template_name='resources/courses.html'
    context_object_name = 'courses'
    paginate_by= 4

