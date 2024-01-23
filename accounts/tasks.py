from accounts.models import OtpCode
from datetime import datetime, timedelta
import pytz
from celery import shared_task


@shared_task
def remove_expired_otp_codes():
    expire_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)  ## codhaei ke az 2 daghighe bishtar omr kardan
    OtpCode.objects.filter(created__lt=expire_time).delete()
