from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from . import serializers, models
from .permissions import IsAdminOrAuthenticated

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()
    permission_classes = [IsAdminOrAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        for d in serializer.data:
            d.pop("description")
            d.pop("rented_by")
        return Response(serializer.data)

    @action(detail=True, methods=["get"], permission_classes=[IsAuthenticated])
    def rent(self, request, pk=None):
        book = models.Book.objects.filter(id=pk).first()
        if request.user.is_authenticated and book.rented_by == request.user:
            book.is_rented = False
            book.rented_by = None
            book.save()
            return Response(status=HTTP_200_OK)
        elif request.user.is_authenticated and book.rented_by == None:
            book.rented_by = request.user
            book.is_rented = True
            book.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_401_UNAUTHORIZED)


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AuthorSerializer
    queryset = models.Author.objects.all()
    permission_classes = [IsAdminOrAuthenticated]
