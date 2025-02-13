class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
        print(self.number_served)

    def open_restaurant(self, oh):
        print(f"Opening Hours: {oh}")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant('kfc', 'Kentucky', number_served=17500)
restaurant.set_number_served(20000)
restaurant.describe_restaurant()
