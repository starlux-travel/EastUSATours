from decouple import config

print("ENV =", config("ENV", default="undefined"))
print("DEBUG =", config("DEBUG", default=False, cast=bool))
print("SECRET_KEY =", config("SECRET_KEY", default="(not set)"))
print("ALLOWED_HOSTS =", config("ALLOWED_HOSTS", default="").split(","))
print("DATABASE_URL =", config("DATABASE_URL", default="(not set)"))
