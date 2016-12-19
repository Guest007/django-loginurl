from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Clean up expired one time keys."

    def handle(self, *args, **kwargs):
        from loginurl import utils
        utils.cleanup()

