farmer = {
    "name" : "Stella maris",
    "crop" : "corn",
    "state" : "California",
    "farm_size" : "100 acres"
}

crops = ["corn", "wheat", "soybeans", "rice", "barley"]

def greet_farmer(name):
    print(f"Hello {name}!, welcome to AI Plant Doctor!")


aI_confidence = 0.85

if(aI_confidence >= 0.80):

    print("Diagnosis confidence is high.")

print("Diagnosis requires further investigation.")