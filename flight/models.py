from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    operation_airlines = models.CharField(max_length=15)
    departure_city = models.CharField(max_length=30)
    arrival_city = models.CharField(max_length=30)
    date_of_departure = models.DateField()
    etd = models.TimeField()

    def __str__(self):
        return f'{self.operation_airlines} - {self.flight_number} - {self.departure_city} - {self.arrival_city}'

class Passenger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    cretad_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


#! niye related_name kullanıyorum: Flight parent gibi Reservation chield gibi. Chield a parenti bağladık ama parent in bundan haberi yok. parent dan child e ulaşmak için related_name i kullanıyorum

#! çünkü Reservation a ait bir res objesi üzerinden res.flight.arrival_city deyince chield (reservation)dan parent(flight) a ulaşabiliyorum. Aynı şekilde parentten chield a ulaşmak için releated_name'i (burada reservations) kullanıyoruz. Flight objesi f1 olsun f1.reservations.all() diyerek ulaşıyoruz

#? iki related name vermek çok doğru değl ama. bu projede öyle verdim.

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    passenger = models.ManyToManyField(Passenger, related_name='reservations')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reservations')




