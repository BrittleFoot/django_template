from books.api.serializers import BookSerializer
from books.models import Book
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


class BookViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
