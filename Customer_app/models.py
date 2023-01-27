from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer_Movie_Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booking_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    movie_selected = models.ForeignKey("Admin_app.Movie", on_delete=models.SET_NULL, null=True)
    audi_selected = models.ForeignKey("Admin_app.Audi", on_delete=models.SET_NULL, null=True)
    num_seats = models.IntegerField(verbose_name="Number of Seats Booked")
    
    @property
    def get_amount(self):
        return self.num_seats

    class Meta:
        verbose_name = "Customer Booking Details"

    def __str__(self):
        return f"{self.num_seats} ticket(s) booked for the movie -> {self.movie_selected}"

