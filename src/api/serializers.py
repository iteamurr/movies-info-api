from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "movie_id",
            "name",
            "distribution_id",
            "the_amount_of_the_fee",
            "movie_type",
            "age_limit",
        ]
