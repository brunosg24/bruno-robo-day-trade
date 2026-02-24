# Configuration settings for FastAPI application

DATABASE_URL = "sqlite:///./test.db"

# Security settings
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Email settings
EMAIL_HOST = "smtp.example.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "user@example.com"
EMAIL_HOST_PASSWORD = "password"
USE_TLS = True

# Other settings
DEBUG = True