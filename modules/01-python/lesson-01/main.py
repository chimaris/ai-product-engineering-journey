## 💻 Practical Exercise ##

name = "Stella maris"
crop = "corn"
state = "California"
farm_size = 100
diagnosis = "Healthy"
confidence = 0.85
image_uploaded = True


# Part 1 — Create these variables with type hints:

farmer_name: str = "Stella maris"
crop: str = "corn"
farm_size: str = "20 plots"
confidence: float = 0.85
image_uploaded: bool = True

# Part 2 — Type Conversion

farm_size = "4"
confidence = "0.87"

# Convert the variables to the correct data types then print their types
# farm_size → integer
#confidence → float

farm_size = int(farm_size)
confidence = float(confidence)

print(type(farm_size))  # Output: <class 'int'>
print(type(confidence))  # Output: <class 'float'>


# Part 3 — Investigation
#What do you think this produces?

print(bool("False"))
print(bool("")) 
print(bool(0))
print(bool(1))

