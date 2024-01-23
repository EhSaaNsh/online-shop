from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin




def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('6D4D7465676536312F6E75584B484B6E36414431664E6B77414C70382B2F4B7942746656426B51395055383D')
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
