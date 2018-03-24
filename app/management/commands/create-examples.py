from django.core.management import BaseCommand
from django_gamification.models import BadgeDefinition, Category, UnlockableDefinition, GamificationInterface

from app.models import ExampleUser


class Command(BaseCommand):
    help = 'Generates fake data for the app'

    def handle(self, *args, **options):
        ExampleUser.objects.create(interface=GamificationInterface.objects.create())

        BadgeDefinition.objects.create(
            name='Badge of Awesome',
            description='You proved your awesomeness',
            points=50,
            category=Category.objects.create(name='Gold Badges', description='These are the top badges'),
        )

        BadgeDefinition.objects.create(
            name='Badge of Coolness',
            description='You proved your coolness',
            points=50,
            category=Category.objects.create(name='Silver Badges', description='These are the secondary badges'),
        )

        UnlockableDefinition.objects.create(
            name='Some super sought after feature',
            description='You unlocked a super sought after feature',
            points_required=50
        )
