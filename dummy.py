import json
from faker import Faker
import random

fake = Faker()

def generate_dummy_data(num_entries=20):
    data = []
    
    for _ in range(num_entries):
        name = fake.name()
        email = fake.email()
        gender = random.choice(["MALE", "FEMALE"])
        
        entry = {
            "name": name,
            "email": email,
            "level": "ICHOOSE",
            "gender": gender
        }
        data.append(entry)
    
    return data

# Generate data
dummy_data = generate_dummy_data()

# Save to JSON file
output_file = "dummy_data.json"
with open(output_file, "w") as f:
    json.dump(dummy_data, f, indent=2)

print(f"Dummy data saved to {output_file}")
