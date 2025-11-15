from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Optional: clear existing data
        Listing.objects.all().delete()

        hosts = User.objects.filter(is_staff=False)[:5]  # pick 5 users as hosts
        locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret']

        for i in range(10):
            Listing.objects.create(
                title=f"Sample Listing {i+1}",
                description="This is a sample listing.",
                host=random.choice(hosts),
                price=random.randint(50, 500),
                location=random.choice(locations)
            )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
