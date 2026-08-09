# 💻 Practical Exercise

## Part 1 — List

# Create a list containing five crops.

# Then:

# Print the first crop.
# Add another crop.
# Remove one crop.
# Print the final list.

crops = ["corn", "wheat", "soybeans", "rice", "barley"]

print(crops[0])  # Output: corn
crops.append("oats")
crops.remove("wheat")
print(crops) 


# Part 2 — Dictionary

# Create a farmer dictionary containing:

# name
# crop
# state
# farm_size
# farm_size_unit

# Then print the farmer's crop. 

farmer = {
    "name": "Stella maris",
    "crop": "corn",
    "state": "California",
    "farm_size": 100,
    "farm_size_unit": "acres"
}

print(farmer["crop"])



# Part 3 — Nested Data

# Create:

# plant_case = {
#     "farmer": ...,
#     "plant": ...,
#     "symptoms": ...
# }

# The farmer should have:

# name
# location

# The plant should have:

# crop
# age_days

# And symptoms should be a list containing at least three symptoms.

plant_case = {
    "farmer": {
        "name": "Stella maris",
        "location": "California"
    },
    "plant": {
        "crop": "corn",
        "age_days": 30
    },
    "symptoms": ["yellowing leaves", "stunted growth", "leaf spots"]    
}