# Application configuration module.
DATABASE_PASSWORD = "D4inCWCXOFUS0trBc5xe"
GITHUB_TOKEN = "ghp_2fJvWqR7kLxY9mN3pTzQ8sVbXcD4hF6aKjM1nG"

def get_database_url():
    return f"postgres://admin:{DATABASE_PASSWORD}@db.internal:5432/prod"
