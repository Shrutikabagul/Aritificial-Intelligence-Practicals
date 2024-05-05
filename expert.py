class Hospital:
    def __init__(self, name, services):
        self.name = name
        self.services = services

hospitals = [
    Hospital("General Hospital", ["Emergency Care", "Surgery", "Internal Medicine"]),
    Hospital("City Medical Center", ["Pediatrics", "Radiology", "Laboratory Services"]),
    Hospital("Community Clinic", ["Primary Care", "Family Medicine", "Pharmacy"]),
    Hospital("Specialty Hospital", ["Cardiology", "Neurology", "Orthopedics"])
]

class ExpertSystem:
    def __init__(self):
        self.symptoms = []
    
    def add_symptom(self, symptom):
        self.symptoms.append(symptom)
    
    def find_hospitals(self):
        matching_hospitals = []
        for hospital in hospitals:
            if all(service in hospital.services for service in self.symptoms):
                matching_hospitals.append(hospital)
        return matching_hospitals

    def display_hospitals(self, hospitals):
        if hospitals:
            print("Recommended hospitals for your symptoms:")
            for hospital in hospitals:
                print("- " + hospital.name)
                print("  Services offered:", ", ".join(hospital.services))
        else:
            print("No hospitals found matching your symptoms.")

# Example usage
print("Welcome to the Hospital Recommendation System!")
print("Please enter your symptoms (separated by commas):")
user_symptoms = input().split(",")

expert_system = ExpertSystem()
for symptom in user_symptoms:
    expert_system.add_symptom(symptom.strip())

matching_hospitals = expert_system.find_hospitals()
expert_system.display_hospitals(matching_hospitals)

