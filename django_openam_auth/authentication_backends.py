from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
import openam

try:
    OPENAM_ENDPOINT = settings.OPENAM_ENDPOINT
except AttributeError:
    raise ImproperlyConfigured("You must set OPENAM_ENDPOINT in the applications's settings")

user_model = get_user_model()

OPENAM_DJANGO_ATTRIBUTES_MAP = (
    ('givenName', 'first_name'),
    ('sn', 'last_name'),
    ('mail', 'email')
)

class OpenAMJSONBackend(object):
    """
    Uses python-openam to authenticate against an openam server using the
    OpenAM json API
    """

    supports_inactive_user = False

    def authenticate(self, username=None, password=None):

        oam = openam.OpenAM(OPENAM_ENDPOINT)

        try:
            token = oam.authenticate(username, password)
            attrs = oam.attributes(token)
            user, _ = user_model.objects.get_or_create(username=username)
            user.is_staff = True
            user.is_superuser = True

            # update Django user attrs
            for oam_att, django_att in OPENAM_DJANGO_ATTRIBUTES_MAP:
                if hasattr(user, django_att) and attrs.attributes.get(oam_att, None):
                    val = attrs.attributes.get(oam_att)
                    setattr(user, django_att, val[0])

            user.save()
            return user
        except openam.AuthenticationFailure:
            return None


    def get_user(self, username):
        try:
            return user_model.objects.get(pk=username)
        except user_model.DoesNotExist:
            return None
