class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self, oh):
        print(f"Opening Hours: {oh}")

kfc = Restaurant('kfc', 'Kentucky')
oh = "\nMo - Fr: \n8:00 - 16:00 \n\nSa - Su: \n9:00 - 17:00"
kfc.describe_restaurant()
kfc.open_restaurant(oh)
