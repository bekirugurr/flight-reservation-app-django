# dj-rest-auth ile auth

documentation sayfası: https://dj-rest-auth.readthedocs.io/en/latest/index.html



## Signallerle ilgili unutma:

signal oluştururken apps.py dosyasında UserConfig in içine/altına alttakini yazmaz isek signal çalışmaz
"""
    def ready(self):
        import users.signals
"""

## serializers.py da create() methodunu override etme genel mantığı

- önce değiştireceğimiz field i .pop() ile çıkarıp bir variable atıyoruz (line 2/satır 3). satır 2 de gereksiz olanı sildik
- sonra düzeltme yapmadan eklenecek field(lar)ı validated_data'ya ekliyoruz (line 3 / satır 4)
- mevcut validated_data ile objeyi oluşturuyoruz (line 4)
- override yapmamıza sebep olan field ı istediğimiz şekilde düzenleyip objeye ekliyouz (line 5 - 7 /satır 5)
- obje nin son halini kaydediyor (line 8 / satır 6) ve dönüyoruz (line 9 / satır 7)

Örnek-1:
```python 
    def create(self, validated_data):                                    # line 1
            passenger_data = validated_data.pop('passenger')             # line 2
            validated_data['user_id'] = self.context['request'].user.id  # line 3
            reservation = Reservation.objects.create(**validated_data)   # line 4
            for passenger in passenger_data:                             # line 5
                pas = Passenger.objects.create(**passenger)              # line 6
                reservation.passenger.add(pas)                           # line 7
            reservation.save()                                           # line 8
            return reservation                                           # line 9
```

Örnek-21:
```python 
    def create(self, validated_data):                # satır 1
        validated_data.pop('password2')              # satır 2
        password = validated_data.pop('password')    # satır 3
        user = User.objects.create(**validated_data) # satır 4
        user.set_password(password)                  # satır 5
        user.save()                                  # satır 6
        return user                                  # satır 7
```