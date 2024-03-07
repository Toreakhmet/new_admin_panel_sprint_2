from config.settings import env


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_DB"),
        "USER": env.str("POSTGRES_USER"),
        "PASSWORD": env.str("POSTGRES_PASSWORD"),
        "HOST": env.str("POSTGRES_HOST", "127.0.0.1"),
        "PORT": env.int("POSTGRES_PORT", 5432),
        "OPTIONS": {"options": "-c search_path=public,content"},
    }
}
