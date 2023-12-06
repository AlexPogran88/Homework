import django_filters
from rest_framework import viewsets
from .models import Books
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import BookSerializers
from rest_framework import filters


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [filters.OrderingFilter]
    search_fields = ['book_title', 'author', 'book_genre', 'price']

