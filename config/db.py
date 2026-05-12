from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGODB_URL", "mongodb+srv://user:password@host/notes")
conn = MongoClient(MONGO_URI)