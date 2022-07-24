import os



class Config:
    API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-super-secret-key")
    # BUCKET_NAME = os.getenv("BUCEKT_NAME", "chillax")
    # S3_LOCATION = os.getenv("S3_LOCATION", "eu-central-1")