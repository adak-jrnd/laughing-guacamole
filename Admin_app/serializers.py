from rest_framework import serializers
from Admin_app.models import Audi, Movie
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404

class AudiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audi
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    audi = AudiSerializer(many = True, allow_null = True) #since it follows many-to-many relationship
    class Meta:
        model = Movie
        fields = "__all__"

    # in order to perform any updates in the API, it is required to create the below functions to execute CRUD operations
    def create(self, validated_data):
        audis = validated_data.pop("audi")
        movie_title = validated_data["movie_title"]
        movie_duration = validated_data["movie_duration"]
        movie_price = validated_data["movie_price"]

        movie_obj = Movie.objects.create(
            movie_title = movie_title, 
            movie_duration = movie_duration, movie_price = movie_price
        )
        for audi in audis:
            movie_obj.audi.add(Audi.objects.create(**audi))
        movie_obj.save()
        return movie_obj

    def update(self, instance, validated_data):
        audis = validated_data.pop("audi")
        instance.movie_title = validated_data.get("movie_title", instance.movie_title)
        instance.movie_duration = validated_data.get("movie_duration", instance.movie_duration)
        if audis is not None:
            for audi in audis:
                instance.audi.add(Audi.objects.create(**audi))
        instance.save()
        return instance

    def list(self, request):
      movies = Movie.objects.filter(active=False)
      serializer = MovieSerializer(movies, many=True)
      return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None):
        try:
            movie = Movie.objects.get(id=pk)
            serializer = MovieSerializer(movie)
            return JsonResponse(serializer.data, safe=False)
        except Movie.DoesNotExist:
            return HttpResponse(status=404)

    def destroy(self, request, pk=None):
        movie = get_object_or_404(Movie, id = pk)
        movie.delete()