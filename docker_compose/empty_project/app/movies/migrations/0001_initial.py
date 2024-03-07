import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Filmwork",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="modified"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                ("description", models.TextField(verbose_name="description")),
                ("creation_date", models.DateField(verbose_name="creation date")),
                (
                    "type",
                    models.CharField(
                        choices=[("MOVIE", "movie"), ("TV_SHOW", "tv show")],
                        default="MOVIE",
                        max_length=10,
                        verbose_name="type",
                    ),
                ),
                (
                    "rating",
                    models.FloatField(
                        blank=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="rating",
                    ),
                ),
                (
                    "file_path",
                    models.FileField(
                        blank=True, null=True, upload_to="movies/", verbose_name="file"
                    ),
                ),
            ],
            options={
                "verbose_name": "filmwork",
                "verbose_name_plural": "filmworks",
                "db_table": 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="modified"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
            ],
            options={
                "verbose_name": "genre",
                "verbose_name_plural": "genre",
                "db_table": 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="modified"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "full_name",
                    models.CharField(max_length=120, verbose_name="full name"),
                ),
            ],
            options={
                "verbose_name": "person",
                "verbose_name_plural": "persons",
                "db_table": 'content"."person',
            },
        ),
        migrations.CreateModel(
            name="PersonFilmwork",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("role", models.TextField(null=True, verbose_name="role")),
                (
                    "film_work",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.filmwork",
                        verbose_name="filmwork",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.person",
                        verbose_name="person",
                    ),
                ),
            ],
            options={
                "verbose_name": "person filmwork",
                "verbose_name_plural": "persons filmworks",
                "db_table": 'content"."person_film_work',
            },
        ),
        migrations.AddField(
            model_name="person",
            name="film_work",
            field=models.ManyToManyField(
                through="movies.PersonFilmwork",
                to="movies.filmwork",
                verbose_name="filmwork",
            ),
        ),
        migrations.CreateModel(
            name="GenreFilmwork",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "film_work",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.filmwork",
                        verbose_name="filmwork",
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.genre",
                        verbose_name="genre",
                    ),
                ),
            ],
            options={
                "verbose_name": "genre filmwrok",
                "verbose_name_plural": "genres filmwroks",
                "db_table": 'content"."genre_film_work',
            },
        ),
        migrations.AddField(
            model_name="filmwork",
            name="genres",
            field=models.ManyToManyField(
                through="movies.GenreFilmwork", to="movies.genre", verbose_name="genres"
            ),
        ),
        migrations.AddConstraint(
            model_name="personfilmwork",
            constraint=models.UniqueConstraint(
                fields=("film_work", "person", "role"),
                name="unique_filmwork_person_role",
            ),
        ),
        migrations.AddConstraint(
            model_name="genrefilmwork",
            constraint=models.UniqueConstraint(
                fields=("film_work", "genre"), name="unique_filmwork_genre"
            ),
        ),
    ]
