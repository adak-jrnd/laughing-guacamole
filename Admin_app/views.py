from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.parsers import JSONParser
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import permission_classes
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from .models import Audi, Movie
from Admin_app import serializers

class AudiViewSet(viewsets.ModelViewSet):

    @permission_classes([permissions.AllowAny])
    def list(self, request):
        audi = Audi.objects.all()
        serializer = serializers.AudiSerializer(audi, many=True)
        print(serializer)
        return JsonResponse(serializer.data, safe=False)

    @permission_classes([permissions.IsAdminUser])
    def create(self, request):
        data = JSONParser().parse(request)
        serializer = serializers.AudiSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    @permission_classes([permissions.AllowAny])
    def retrieve(self, request,pk=None):
        try:
            audi = Audi.objects.get(audi_id = pk)
            serializer = serializers.AudiSerializer(audi)
            return JsonResponse(serializer.data)
        except audi.DoesNotExist():
            return HttpResponse(status = 404)

    @permission_classes([permissions.IsAdminUser])
    def update(self, request, pk=None):
        audi = Audi.objects.get(audi_id = pk)
        data = JSONParser().parse(request)
        serializer = serializers.AudiSerializer(audi, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    @permission_classes([permissions.IsAdminUser])
    def destroy(self, request, pk = None):
        audi = Audi.objects.get(audi_id = pk)
        audi.delete()
        return HttpResponse(status=204)


class MovieViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    @permission_classes([permissions.IsAuthenticated])
    def list(self, request):
        movies = Movie.objects.prefetch_related('movie_audi').all()
        serializer = serializers.MovieSerializer(movies, many=True)
        print(serializer)
        return JsonResponse(serializer.data, safe=False)

    @permission_classes([permissions.IsAdminUser])
    def create(self, request):
        data = JSONParser().parse(request)
        serializer = serializers.MovieSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    @permission_classes([permissions.IsAuthenticated])
    def retrieve(self, request,pk=None):
        try:
            movie = Movie.objects.get(movie_id = pk)
            serializer = serializers.MovieSerializer(movie)
            return JsonResponse(serializer.data)
        except Movie.DoesNotExist():
            return HttpResponse(status = 404)

    @permission_classes([permissions.IsAdminUser])
    def update(self, request, pk=None):
        movie = Movie.objects.get(movie_id = pk)
        data = JSONParser().parse(request)
        serializer = serializers.MovieSerializer(movie, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    @permission_classes([permissions.IsAdminUser])
    def destroy(self, request, pk = None):
        movie = Movie.objects.get(movie_id = pk)
        movie.delete()
        return HttpResponse(status=204)