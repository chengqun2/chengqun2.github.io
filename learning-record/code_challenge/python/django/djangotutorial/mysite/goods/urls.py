from django.urls import path
from.views import BookCreateView, BookListView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookCreateView.as_view()),
    path('books/getList/', BookListView.as_view()),
    path('books/<int:id>/', BookDetailView.as_view()),
    path('books/update/<int:id>/', BookUpdateView.as_view()),
    path('books/delete/<int:id>/', BookDeleteView.as_view()),
]