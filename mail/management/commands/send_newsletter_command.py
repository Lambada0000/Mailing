from django.core.management import BaseCommand

from mail.cron import newsletter_mail


class Command(BaseCommand):
    def handle(self, *args, **options):
        newsletter_mail()
