products = ["Shirt", "Pants", "Shoes", "Sunglasses", "Watch"]
colors = ["Red", "Blue", "Green", "Yellow", "Black", "White"]
sizes = ["Small", "Medium", "Large", "X-Large"]

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
        
    def __eq__(self, other):
        return (self.name.lower() == other.name.lower() and
                self.color.lower() == other.color.lower() and
                self.size.lower() == other.size.lower())

inventory = [
    Product("Shirt", "Blue", "Large"),
    Product("Pants", "Black", "Medium"),
    Product("Shoes", "Red", "X-Large"),
    Product("Sunglasses", "Green", "Small"),
    Product("Watch", "Yellow", "Large"),
]

print("Welcome to our Clothes store! How can I help you?")
user_input = input()

while user_input.lower() != "no":
    if user_input.lower() == "yes":
        print("Let me ask you a few questions to help narrow down our recommendations.")
        print("What type of product are you looking for? We have the following options:")
        for product in products:
            print("- " + product)
        customer_product = input()

        print("What color do you prefer? We have the following options:")
        for color in colors:
            print("- " + color)
        customer_color = input()

        print("What size do you need? We have the following options:")
        for size in sizes:
            print("- " + size)
        customer_size = input()

        customer_preference = Product(customer_product, customer_color, customer_size)

        print("Here are our recommendations based on your preferences:")
        product_found = False
        for product in inventory:
            if product == customer_preference:
                print("- " + product.color + " " + product.size + " " + product.name)
                product_found = True

        if not product_found:
            print("Sorry, we don't have that product.")  # Added a complete print statement
    else:
        print("I'm sorry, I didn't understand your inquiry. Please try again.")
    
    print("Do you want to continue the purchase: yes/no")
    user_input = input()

print("Thank you for shopping with us! Visit Again.")

