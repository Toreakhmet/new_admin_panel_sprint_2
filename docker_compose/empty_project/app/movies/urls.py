from django.urls import path, include

urlpatterns = [
    path("movies/", include("movies.api.v1.urls")),
]
