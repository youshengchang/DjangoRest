from .models import Author,Book
from .serializer import AuthorSerializer,BookSerializer
from rest_framework import  generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
#from rest_framework.authentication import BasicAuthentication
#from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions

# Create your views here.
class BookPagination(LimitOffsetPagination):
    default_limit = 3

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
#    authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
