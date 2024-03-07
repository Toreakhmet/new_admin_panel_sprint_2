from django.urls import path, include

from movies.api.v1 import views

urlpatterns = [
    path("<uuid:pk>", views.MovieDetailApi.as_view()),
    path("", views.MoviesListApi.as_view()),
]
