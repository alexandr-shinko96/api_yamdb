from django.contrib import admin
from .models import Category, Genres, Title, Review, Comments
from users.models import User

admin.site.register(Category)
admin.site.register(Genres)
admin.site.register(Review)
admin.site.register(Comments)
admin.site.register(Title)
admin.site.register(User)
