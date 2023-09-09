import csv

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from api.models import Movie


def from_csv(file_path: str, with_header: bool = True) -> list[bool]:
    result = []
    with open(file_path) as file:
        reader = csv.reader(file)
        if with_header:
            next(reader, None)

        with transaction.atomic():
            for row in reader:
                _, created = Movie.objects.get_or_create(
                    name=row[0],
                    distribution_id=row[1],
                    the_amount_of_the_fee=row[2],
                    movie_type=row[3],
                    age_limit=row[4],
                )
                result.append(created)
    return result


class Command(BaseCommand):
    help = "Imports data from a .csv file if it fits the database format."

    def add_arguments(self, parser):
        parser.add_argument(
            "file_path", nargs="+", type=str, help="Paths to .csv files."
        )

        parser.add_argument(
            "--without-header",
            action="store_true",
            help=(
                "Select if there is no header in the .csv file. "
                "Will start reading the file from the first line."
            ),
        )

    def handle(self, *args, **options):
        for file_path in options["file_path"]:
            try:
                result = from_csv(file_path, not options["without_header"])
            except:
                raise CommandError(
                    f"An error occurred while importing data from '{file_path}'."
                )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully added {sum(result)}/{len(result)} rows."
                )
            )
