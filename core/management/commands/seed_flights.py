from django.core.management.base import BaseCommand
from core.models import Flight 
from django.utils import timezone
import datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Xóa dữ liệu cũ để tránh trùng lặp Mã chuyến bay (unique=True)
        Flight.objects.all().delete()

        flights = [
            {"num": "SK101", "from": "TP. Hồ Chí Minh (SGN)", "to": "Hà Nội (HAN)", "price": 1200000},
            {"num": "SK202", "from": "Hà Nội (HAN)", "to": "Đà Nẵng (DAD)", "price": 850000},
            {"num": "SK303", "from": "TP. Hồ Chí Minh (SGN)", "to": "Phú Quốc (PQC)", "price": 950000},
            {"num": "SK404", "from": "Đà Nẵng (DAD)", "to": "Đà Lạt (DLI)", "price": 700000},
            {"num": "SK505", "from": "Hải Phòng (HPH)", "to": "TP. Hồ Chí Minh (SGN)", "price": 1100000},
        ]

        for f in flights:
            Flight.objects.create(
                flight_number=f["num"],
                departure_city=f["from"],    # Đã sửa theo Model của Khôi
                destination_city=f["to"],    # Đã sửa theo Model của Khôi
                departure_time=timezone.now() + datetime.timedelta(days=1),
                price=f["price"]
            )