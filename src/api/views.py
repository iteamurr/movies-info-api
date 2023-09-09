from rest_framework import filters, generics, pagination

from .models import Movie
from .serializers import MovieSerializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 100


class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Movie.objects.all().order_by("-the_amount_of_the_fee")

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)

    search_fields = ("name", "distribution_id")
