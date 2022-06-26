from rest_framework import serializers
from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd"
        )
        
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
        
        
#! get yaptığımızda flight_id ve user_id gözükmüyorken neden koydum. Çünkü reservation instance ı oluştururken (post yaparken) read_only olan StringRelatedField ler flight ve user ı kullanamıyorum. O yüzden reservation oluştururken write only olan flight_id ve user_id yi kullanıyorum. writeonly olan bunlarla oluşturuyor ama read only olan flight ve user la read işlemi yapıyorum

#! Ama 4 ünü de fiels tupple ı içine yazmak lazım. Yoksa hata verir

#! Eğer aşağıdaki nested yapıyı yapmasaydık serializer bize sadece {"flight_id": 1, "user_id": 1, "passenger": [3, 6] } gibi okuyan için anlamsız gelecek bir output dönecekti. Nested serializer ile okunaklı bi çıktı verdik

class ReservationSerializer(serializers.ModelSerializer):

    passenger = PassengerSerializer(many=True, required=False)
    flight = serializers.StringRelatedField()  # default read_only=True
    user = serializers.StringRelatedField()  # default read_only=True
    flight_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True, required=False) # Manuel oluşturmayıp otomatik çekeceğimiz için required=False yaptık
    class Meta:
        model = Reservation
        fields =(
            "id",
            "flight",
            "flight_id",
            "user",
            "user_id",
            "passenger"
        )
    
    #! passenger ve reservation tabloları ayrı ve kayıtlarının da ayrı yapılması lazım. Aşağıdaki override ile birlikte tek işlemle ikisine birden instance oluşturuyoruz 

    def create(self, validated_data):
        passenger_data = validated_data.pop('passenger')
        validated_data['user_id'] = self.context['request'].user.id
        reservation = Reservation.objects.create(**validated_data)
        for passenger in passenger_data: # 1 reservasyonda birden çok kişi olabildiği içir for kullandık
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas)
        reservation.save()
        return reservation
    
    #def update() #todo
    
class StaffFlightSerializer(serializers.ModelSerializer):
    
    reservations = ReservationSerializer(many=True, read_only=True) # Reservation serializer ında flight field i için oluşturulan related_name i kullanıyoruz. readonly olmasının sebebi flight oluştururken reservasyon oluşturabilmesini engellemek
    
    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd",
            "reservations",
        )
        