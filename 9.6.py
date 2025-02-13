from restaurantsss import Restaurant

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        self.flavors = flavors
        
    def show_flavors(self):
        print(f"Oto dostępne smaki: ")
        for flavor in self.flavors:
            print(f"- {flavor}")

me = IceCreamStand('kfc', 'Kentucky', 'waniliowy', 'śliwkowy')
me.show_flavors()