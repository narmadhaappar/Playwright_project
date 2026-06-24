import random
import string
import time

class DataGenerator:
    @staticmethod
    def generate_random_data():
        unique_id = int(time.time())  # Unique ID based on current timestamp in milliseconds

        pet_name = "Zebra_"+"".join(random.choices(string.ascii_letters, k=5))

        category_name = "Category_"+"".join(random.choices(string.ascii_letters, k=5))

        tag_name = "Tag_"+"".join(random.choices(string.ascii_letters, k=5))    

        return {
            "id": unique_id,
            "category":{
                "id":random.randint(1, 1000),
                "name": category_name
            },
            "name": pet_name,
            "photoUrls": [
                "https://example.com/photo1.jpg",
            ],
            "tags": [
                {
                    "id": random.randint(1, 1000),
                    "name": tag_name
                }
            ],
            "status": "available"   
        }
