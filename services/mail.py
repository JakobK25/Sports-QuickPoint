import smtplib, ssl
from dotenv import load_dotenv
from pathlib import Path
import os




# Load the environment variables
env_path = Path('.') / '.env'
load_dotenv(env_path)

# Get environment variables
smtp_password= os.getenv("SMTP_PASSWORD")


port = 465  # For SSL
password = smtp_password

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)
    # TODO: Send email here