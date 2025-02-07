# since we use rest api in django , and data will be sent in json form,that's why this file is necessary 
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        