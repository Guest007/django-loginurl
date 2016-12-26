from django.utils.http import int_to_base36

from loginurl.utils import _create_token


def create_key(user):
    token = _create_token(user)
    b36_uid = int_to_base36(user.id)
    key = '--{}-{}'.format(b36_uid, token)

    return key
