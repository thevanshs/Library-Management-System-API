from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse, JsonResponse
import csv
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Genre, Author, Book
from .serializers import GenreSerializer, AuthorSerializer, BookSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def author_signup(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def author_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token})

    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAdminUser])
def add_genre(request):
    serializer = GenreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_all_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_author_details(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_books_by_author(request, author_id):
    books = Book.objects.filter(author_id=author_id)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    return Response({'message': 'Genre deleted successfully'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_book(request):
    data = request.data.copy()
    data['author'] = request.user.id  
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_book(request, book_id):
    author_instance = get_object_or_404(Author, id=request.user.id)

    book = get_object_or_404(Book, id=book_id, author=author_instance)
    serializer = BookSerializer(book, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def export_books_data(request, genre_id):
    books = Book.objects.filter(genre_id=genre_id)
    serializer = BookSerializer(books, many=True)

    data = serializer.data

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename=books_export.csv'

    writer = csv.writer(response)
    writer.writerow(['Book Name', 'Author Name', 'Number of Pages'])

    for book_data in data:
        writer.writerow([book_data['name'], book_data['author']['name'], book_data['num_pages']])

    return response

class AuthorLoginView(TokenObtainPairView):
    pass

class TokenRefreshView(TokenRefreshView):
    pass
