from rest_framework import serializers
from Customer_app.models import Customer_Movie_Booking
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email"]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Movie_Booking
        fields = "__all__"

    # in order to perform any updates in the API, it is required to create the below functions to execute CRUD operations
    def create(self, validated_data):
        movie_selected = validated_data["movie_selected"]
        num_seats = validated_data["num_seats"]

        cust_obj = Customer_Movie_Booking.objects.create(
            movie_selected = movie_selected, 
            num_seats = num_seats
        )
        cust_obj.save()
        return cust_obj

    def update(self, instance, validated_data):
        instance.movie_selected = validated_data.get("movie_selected", instance.movie_selected)
        instance.num_seats = validated_data.get("num_seats", instance.num_seats)
        instance.save()
        return instance

    def list(self, request):
      movie_bookings = Customer_Movie_Booking.objects.filter(active=False)
      serializer = BookingSerializer(movie_bookings, many=True)
      return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None):
        try:
            movie = Customer_Movie_Booking.objects.get(id=pk)
            serializer = BookingSerializer(movie)
            return JsonResponse(serializer.data, safe=False)
        except Customer_Movie_Booking.DoesNotExist:
            return HttpResponse(status=404)

    def destroy(self, request, pk=None):
        movie_booking = get_object_or_404(Customer_Movie_Booking, id = pk)
        movie_booking.delete()