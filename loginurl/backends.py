from django.contrib.auth import get_user_model

from loginurl.models import Key


class LoginUrlBackend(object):
    """
    Authentication backend that checks the given ``key`` to a record in the
    ``Key`` model. If the record is found, then ``is_valid()`` method is called
    to check if the key is still valid.
    """
    supports_object_permissions = False
    supports_anonymous_user = False

    def authenticate(self, key):
        """
        Check if the key is valid.
        """
        data = Key.objects.filter(key=key)
        if len(data) == 0:
            return None

        data = data[0]
        if not data.is_valid():
            return None

        return data.user

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
