from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data directly into MongoDB
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "password1"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "password2"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "password3"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "password4"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "password5"},
        ]
        db.users.insert_many(users)

        # Create a mapping of usernames to ObjectIds
        username_to_id = {user["username"]: user["_id"] for user in users}

        db.teams.insert_many([
            {"_id": ObjectId(), "name": "Blue Team", "members": [username_to_id["thundergod"], username_to_id["metalgeek"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [username_to_id["zerocool"], username_to_id["crashoverride"], username_to_id["sleeptoken"]]},
        ])

        db.activity.insert_many([
            {"_id": ObjectId(), "user": username_to_id["thundergod"], "activity_type": "Cycling", "duration": "01:00:00"},
            {"_id": ObjectId(), "user": username_to_id["metalgeek"], "activity_type": "Crossfit", "duration": "02:00:00"},
            {"_id": ObjectId(), "user": username_to_id["zerocool"], "activity_type": "Running", "duration": "01:30:00"},
            {"_id": ObjectId(), "user": username_to_id["crashoverride"], "activity_type": "Strength", "duration": "00:30:00"},
            {"_id": ObjectId(), "user": username_to_id["sleeptoken"], "activity_type": "Swimming", "duration": "01:15:00"},
        ])

        db.leaderboard.insert_many([
            {"_id": ObjectId(), "user": username_to_id["thundergod"], "score": 100},
            {"_id": ObjectId(), "user": username_to_id["metalgeek"], "score": 90},
            {"_id": ObjectId(), "user": username_to_id["zerocool"], "score": 95},
            {"_id": ObjectId(), "user": username_to_id["crashoverride"], "score": 85},
            {"_id": ObjectId(), "user": username_to_id["sleeptoken"], "score": 80},
        ])

        db.workouts.insert_many([
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
