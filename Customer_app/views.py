from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.parsers import JSONParser
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from rest_framework.decorators import permission_classes, api_view

from .models import Customer_Movie_Booking
from Customer_app import serializers

class CustomerDetailViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.AllowAny]
    permission_classes_by_action = {
        'list': [permissions.IsAdminUser],
        'create': [permissions.AllowAny],
        'update': [permissions.IsAdminUser, permissions.IsAuthenticated],
        'destroy': [permissions.IsAdminUser]
        }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            permissions=[permission() for permission in self.permission_classes_by_action[self.action]]
            print(f'permissions= {permissions}')
            return permissions
        except KeyError: 
            # action is not set return default permission_classes
            permissions=[permission() for permission in self.permission_classes]
            print(f' [ERROR] Default permissions= {permissions}')
            return permissions

    def list(self, request):
        users = User.objects.all()
        serializer = serializers.CustomerSerializer(users, many=True)
        print(serializer)
        return JsonResponse(serializer.data, safe = False)

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = serializers.CustomerSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe = False)
        return JsonResponse(serializer.errors, status=400, safe = False)
    
    def retrieve(self, request,pk=None):
        try:
            user = User.objects.get(id = pk)
            serializer = serializers.CustomerSerializer(user)
            return JsonResponse(serializer.data, safe = False)
        except User.DoesNotExist():
            return HttpResponse(status = 404)

    def update(self, request, pk=None):
        user = User.objects.get(id = pk)
        data = JSONParser().parse(request)
        serializer = serializers.CustomerSerializer(user, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe = False)
        return JsonResponse(serializer.errors, status = 400, safe = False)

    def destroy(self, request, pk = None):
        user = User.objects.get(id = pk)
        user.delete()
        return HttpResponse(status=204)

class MovieBookingViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.AllowAny]
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated],
        'create': [permissions.IsAuthenticated],
        'update': [permissions.IsAuthenticated],
        'destroy': [permissions.IsAuthenticated], }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            permissions=[permission() for permission in self.permission_classes_by_action[self.action]]
            print(f'permissions= {permissions}')
            return permissions
        except KeyError: 
            # action is not set return default permission_classes
            permissions=[permission() for permission in self.permission_classes]
            print(f' [ERROR] Default permissions= {permissions}')
            return permissions

    # def allowed_methods(self):
    #     """
    #     Return the list of allowed HTTP methods, uppercased.
    #     """
    #     self.http_method_names.append("POST")
    #     return [method for method in self.http_method_names
    #             if hasattr(self, method)]

    def list(self, request, user):
        try:
            movie_booking = Customer_Movie_Booking.objects.filter(booking_owner__username__iexact = user)
            serializer = serializers.BookingSerializer(movie_booking, many=True)
            print(serializer)
            return JsonResponse(serializer.data, safe = False)
        except:
            return JsonResponse("No Booking Found", status=404, safe=False)

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = serializers.BookingSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe = False)
        return JsonResponse(serializer.errors, status=400, safe = False)
    
    def retrieve(self, request,pk=None):
        try:
            booking = Customer_Movie_Booking.objects.get(id = pk)
            serializer = serializers.BookingSerializer(booking)
            return JsonResponse(serializer.data, safe = False)
        except:
            return JsonResponse("No Booking Found", status=404, safe=False)

    def update(self, request, pk=None):
        booking = Customer_Movie_Booking.objects.get(id = pk)
        data = JSONParser().parse(request)
        serializer = serializers.BookingSerializer(booking, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe = False)
        return JsonResponse(serializer.errors, status = 400, safe = False)

    def destroy(self, request, pk = None):
        booking = Customer_Movie_Booking.objects.get(id = pk)
        booking.delete()
        return HttpResponse(status=204)