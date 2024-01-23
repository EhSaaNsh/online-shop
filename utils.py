from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin

import A.settings


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI(A.settings.KAVENEGAR_API_KEY)
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'{code}کد تایید شما '
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)

class IsUserAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin ## ham login karde bashe va ham admin bashe
