from django.urls import path
from.views import BookCreateView, BookListView, BookDetailView

urlpatterns = [
    path('books/', BookCreateView.as_view()),
    path('books/getList/', BookListView.as_view()),
    path('books/<int:todo_id>/', BookDetailView.as_view()),
]