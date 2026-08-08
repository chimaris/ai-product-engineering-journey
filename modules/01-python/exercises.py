farmer = {
    "name" : "Stella maris",
    "crop" : "corn",
    "state" : "California",
    "farm_size" : "100 acres"
}

crops = ["corn", "wheat", "soybeans", "rice", "barley"]

aI_confidence = 0.85


def greet_farmer(name):
    return f"Hello {name}!, welcome to AI Plant Doctor!"


print(greet_farmer(farmer["name"]))


if(aI_confidence >= 0.80):
    print("Diagnosis confidence is high.")
else:
    print("Diagnosis requires further investigation.")