from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import BookSerializer
from.models import Book

class BookCreateView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookDetailView(APIView):
    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)
        
class BookUpdateView(APIView):
    def put(self, request, id):
        try:
            instance = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response(instance.errors, status=status.HTTP_204_NO_CONTENT)
        serializer = BookSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BookDeleteView(APIView):
    def delete(self, request, id):
        try:
            # Retrieve the object by its primary key
            instance = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_204_NO_CONTENT)
        # Delete the object
        instance.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_200_OK)