from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = ['author', 'title', 'synopsis', 'published', 'edited']
        fields = '__all__'
