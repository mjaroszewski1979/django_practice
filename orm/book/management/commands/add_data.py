import pandas as pd
from django.core.management.base import BaseCommand
from book.models import Book
from sqlalchemy import create_engine


class Command(BaseCommand):

    def handle(self, *args, **options):
        excel_file = 'output.xlsx'
        df = pd.read_excel(excel_file)
        df.columns=["Id", "Close"]
        df.set_index("Id", inplace=True)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(Book._meta.db_table, if_exists='replace', con=engine)
