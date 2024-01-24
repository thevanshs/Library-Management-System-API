from django.urls import path
from django.contrib import admin
from libapi.views import (
    author_signup,
    author_login,
    add_genre,
    get_all_authors,
    get_author_details,
    get_books_by_author,
    delete_genre,
    add_book,
    edit_book,
    export_books_data,
    AuthorLoginView,
    TokenRefreshView,
)
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('author/signup/', author_signup, name='author_signup'),
    path('author/login/', author_login, name='author_login'),
    path('admin/add-genre/', add_genre, name='add_genre'),
    path('admin/get-all-authors/', get_all_authors, name='get_all_authors'),
    path('admin/get-author/<int:author_id>/', get_author_details, name='get_author_details'),
    path('admin/get-books/<int:author_id>/', get_books_by_author, name='get_books_by_author'),
    path('admin/delete-genre/<int:genre_id>/', delete_genre, name='delete_genre'),
    path('author/add-book/', add_book, name='add_book'),
    path('author/edit-book/<int:book_id>/', edit_book, name='edit_book'),
    path('admin/export-books/<int:genre_id>/', export_books_data, name='export_books_data'),
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

