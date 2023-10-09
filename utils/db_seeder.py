from django.db import connection
from django.conf import settings

class DatabaseSeeder:
    def __init__(self):
        self.sql_file = settings.BASE_DIR / 'utils' / 'create_tests_base.sql'

    def seed_database(self):
        with connection.cursor() as cursor:
            with open(self.sql_file, 'r') as sql_file:
                sql_statements = sql_file.read()
                cursor.execute(sql_statements)