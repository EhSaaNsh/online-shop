from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime, timedelta
import pytz


class Command(BaseCommand):
    help = 'remove all expired otp codes'

    def handle(self, *args, **options):
        expire_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2) ## codhaei ke az 2 daghighe bishtar omr kardan
        OtpCode.objects.filter(created__lt = expire_time).delete()
        self.stdout.write('expired codes deleted')
