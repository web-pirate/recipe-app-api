"""
Django command to wait for the database to be available.
"""
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Waits until a connection can be made."""
    def handle(self, *args, **options):
        """Entrypoint for commmand"""
        # Wait until db is up and running before starting server
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 sec ...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
