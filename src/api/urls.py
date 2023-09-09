from django.urls import path

from .views import MovieDetail, MovieList


urlpatterns = [
    path("", MovieList.as_view()),
    path("<str:pk>/", MovieDetail.as_view(), name="retrieve-movie"),
]
