from django.db import models

# Create your models here.
class Audi(models.Model):
    audi_id = models.AutoField(primary_key=True, editable=False)
    audi_name = models.CharField(verbose_name="Audi Name", max_length=100, unique=True)
    audi_total_seats = models.IntegerField(verbose_name="Total number of seats available")
    audi_opening_time = models.TimeField()
    audi_closing_time = models.TimeField()

    def __str__(self):
        return f"{self.audi_name} has a total of {self.audi_total_seats} seats."


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True, editable=False)
    movie_title = models.CharField(verbose_name="Movie Title", max_length=100)
    movie_duration = models.TimeField(verbose_name="Movie Duration", max_length=100)
    movie_audi = models.ManyToManyField(Audi, related_name="movie_audi_rel", verbose_name="Movie Audi", max_length=100)
    movie_price = models.FloatField(verbose_name="Price of each ticket")
    
    def __str__(self):
        return f"{self.movie_title} is of {self.movie_duration} duration."
