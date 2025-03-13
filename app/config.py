import os
from pathlib import Path
from dotenv import load_dotenv

def load_config():
    # Load environment variables from .env file
    env_path = Path('.') / '.env'
    load_dotenv(env_path)
    
    config = {
        "POSTGRES_DB": os.getenv("POSTGRES_DB"),
        "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD")
    }
    return config
