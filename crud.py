from pymongo import MongoClient

class AnimalShelter:
    def __init__(self, username, password, host='localhost', port=38409):
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/AAC')
        self.db = self.client['AAC']
        self.collection = self.db['animals']

    def create(self, data):
        try:
            self.collection.insert_one(data)
            return True
        except Exception as e:
            print(f"Error inserting document: {e}")
            return False

    def read(self, query):
        try:
            cursor = self.collection.find(query, {'_id': 0})
            return cursor
        except Exception as e:
            print(f"Error querying document: {e}")
            return None
      
    def update(self, query, updated_data):
        try:
            self.collection.update_one(query, {"$set": updated_data})
            return True
        except Exception as e:
            print(f"Error updating document: {e}")
            return False

    def delete(self, query):
        try:
            self.collection.delete_one(query)
            return True
        except Exception as e:
            print(f"Error deleting document: {e}")
            return False
    def find_water_rescue(self, query):
        breeds = ["Labrador Retriever", "Chesapeake Bay Retriever", "Newfoundland"]
        sex = "Intact Female"
        min_age_weeks = 26
        max_age_weeks = 156

        breed_query = [{"breed": {"$regex": f".*{breed}.*"}} for breed in breeds]
        results = self.collection.find({
            **query,
            "animal_type": "Dog",
            "$or": breed_query,
            "sex_upon_outcome": sex,
            "age_upon_outcome_in_weeks": {"$gte": min_age_weeks, "$lte": max_age_weeks},
        }, {"_id": 0})

        return results
    
    def find_mountain_wilderness_rescue(self, query):
        breeds = ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog", "Siberian Husky", "Rottweiler"]
        sex = "Intact Male"
        min_age_weeks = 26
        max_age_weeks = 156

        breed_query = [{"breed": {"$regex": f".*{breed}.*"}} for breed in breeds]
        results = self.collection.find({
            **query,
            "animal_type": "Dog",
            "$or": breed_query,
            "sex_upon_outcome": sex,
            "age_upon_outcome_in_weeks": {"$gte": min_age_weeks, "$lte": max_age_weeks},
        }, {"_id": 0})
        return results

    def find_disaster_rescue(self, query):
        breeds = ["Doberman Pinscher", "German Shepherd", "Golden Retriever", "Bloodhound", "Rottweiler"]
        sex = "Intact Male"
        min_age_weeks = 20
        max_age_weeks = 300

        breed_query = [{"breed": {"$regex": f".*{breed}.*"}} for breed in breeds]
        results = self.collection.find({
            **query,
            "animal_type": "Dog",
            "$or": breed_query,
            "sex_upon_outcome": sex,
            "age_upon_outcome_in_weeks": {"$gte": min_age_weeks, "$lte": max_age_weeks},
        }, {"_id": 0})
        return results
