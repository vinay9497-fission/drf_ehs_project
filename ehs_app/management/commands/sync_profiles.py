from django.core.management.base import BaseCommand
from ehs_app.models import Profile
from django.db import connections

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT * FROM profile;")
            rows = cursor.fetchall()
            for row in rows:
                Profile.objects.create(
                    first_name=row[1],
                    last_name=row[2],
                    dob=row[3],
                    gender=row[4],
                    blood_type=row[5],
                    phone_number=row[6],
                    address=row[7],
                    city=row[8],
                    medical_condition=row[9],
                    doctor_assigned=row[10]
                )
            self.stdout.write(self.style.SUCCESS('Profiles synced successfully'))
