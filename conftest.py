from dotenv import load_dotenv

# On your laptop, read APP_USERNAME and APP_PASSWORD from .env.
# GitHub Actions has no .env file: it sets the same names from repository secrets and variables.
load_dotenv()
