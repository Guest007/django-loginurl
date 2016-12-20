import uuid
import hashlib


def create_token(user):
    _id = '{id}-{email}-{password}-{uuid}'.format(
        id=user.id, email=user.email, password=user.password,
        uuid=str(uuid.uuid4()))
    return hashlib.md5(_id.encode('ascii')).hexdigest()
