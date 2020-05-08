from rest_framework import serializers
from . import models


class AuthorSerializer(serializers.ModelSerializer):
    books_id = serializers.ListField(child=serializers.IntegerField(), required=False)

    class Meta:
        model = models.Author
        fields = ["name", "surname", "birth_date", "books_id", "id"]


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(required=False, many=True, read_only=True)
    authors_id = serializers.ListField(
        child=serializers.IntegerField(), required=False, write_only=True
    )
    description = serializers.CharField(
        required=False, allow_blank=True, allow_null=True
    )

    class Meta:
        model = models.Book
        fields = "__all__"

    def create(self, validated_data):
        authors_data = validated_data.get("authors_id")
        book = models.Book.objects.create(**validated_data)
        for a in authors_data:
            book.authors.add(a)
        return book

    def update(self, instance, validated_data):
        authors_data = validated_data.get("authors_id")
        if authors_data:
            validated_data.pop("authors_id")
            instance.authors.clear()
            for a in authors_data:
                instance.authors.add(a)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
