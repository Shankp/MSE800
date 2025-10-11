from datetime import timezone
from pymongo import MongoClient, ASCENDING
# from .config import settings

client = MongoClient("mongodb://localhost:27017", tz_aware=True, tzinfo=timezone.utc)
db = client["ExerciseApp"]