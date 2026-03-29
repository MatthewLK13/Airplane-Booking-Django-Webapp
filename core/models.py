from django.db import models

class Flight(models.Model):
    flight_number = models.CharField("Mã chuyến bay", max_length=10, unique=True)
    departure_city = models.CharField("Điểm đi", max_length=100)
    destination_city = models.CharField("Điểm đến", max_length=100)
    departure_time = models.DateTimeField("Giờ khởi hành")
    price = models.DecimalField("Giá vé (VNĐ)", max_digits=12, decimal_places=0)

    def __str__(self):
        return f"{self.flight_number}: {self.departure_city} -> {self.destination_city}"

class Feedback(models.Model):
    name = models.CharField("Tên người dùng", max_length=100)
    email = models.EmailField("Email")
    message = models.TextField("Nội dung")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback từ {self.name}"