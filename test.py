import os

password = os.getenv("APP_PASSWORD")

# Parameterized query - to be used with cursor.execute(query, (user_id,))
query = "SELECT * FROM users WHERE id = %s"
