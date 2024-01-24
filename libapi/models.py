from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Author(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile_images/',null=True)
    author_id = models.CharField(max_length=15, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.author_id:
            city_code = self.city[:3].upper()
            last_author = Author.objects.filter(city=self.city).order_by('-id').first()
            if last_author:
                last_id = int(last_author.author_id[-4:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.author_id = f"AR{city_code}{new_id:04}"
        super().save(*args, **kwargs)

class Book(models.Model):
    name = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    num_pages = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='book_covers/',null=True)
