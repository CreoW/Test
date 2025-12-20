import os

password = os.getenv("APP_PASSWORD")
query = "SELECT * FROM users WHERE id = %s"
