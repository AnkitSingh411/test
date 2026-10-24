import os

GITHUB_TOKEN = "ghp_2fJvWqR7kLxY9mN3pTzQ8sVbXcD4hF6aKjM1nG"
AWS_SECRET_ACCESS_KEY = "C0x5ZoOxNBnANGkwenD5eXpCPrhHj7z6rrJa2786"
DATABASE_PASSWORD = "D4inCWCXOFUS0trBc5xe"
STRIPE_API_KEY = "sk_live_qZgfjmi3jBUpH2qUKrEu2gai"

def get_database_url():
    return f"postgres://admin:{DATABASE_PASSWORD}@db.internal:5432/prod"

def get_client():
    return GITHUB_TOKEN, AWS_SECRET_ACCESS_KEY, STRIPE_API_KEY
