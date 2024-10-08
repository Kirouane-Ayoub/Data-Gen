import os

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

# API Keys and other settings
CO_API_KEY = os.getenv("CO_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Default values for model configurations
DEFAULT_COHERE = "command-r-plus"
DEFAULT_GEMINI = "gemini-1.5-flash"
DEFAULT_GROQ = "llama3-8b-8192"
DEFAULT_OLLAMA = "llama3.1"
