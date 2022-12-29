from django.shortcuts import render
from rest_framework import viewsets
from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, ReservationSerializer, StaffFlightSerializer
from .permissions import IsStafOrReadOnly
from datetime import datetime, date
from rest_framework.permissions import IsAuthenticated


class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStafOrReadOnly,)

#! aşağıda user adminse uçuşları reservasyonları ile göster, değilse sadece flightları göster diyorum. burada yaptığım object level permission la aynı ama daha kısası
    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffFlightSerializer
        return serializer
    
#! aşağıda user admin se bu günden önce ve sonra bütün uçuşları göster, değilse sadece bugun-bu saatten sonrakileri göster
    def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        today = date.today()
        
        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            queryset = Flight.objects.filter(date_of_departure__gt=today)
            if Flight.objects.filter(date_of_departure=today):
                today_qs = Flight.objects.filter(date_of_departure=today).filter(etd__gt=current_time)
                queryset = queryset.union(today_qs)
            return queryset

class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes=(IsAuthenticated,)
    
    #! user, staff ise bütün reservasyonları göster, değilse sadece kendi yaptığı reservasyonları göster  
    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = Reservation.objects.all() # üsttekiyle bu aynı ama üstteki dinamik olduğu için daha fazla kullanılıyormuş, bu hardcoded oluyor 
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)

