class car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        if for_sale == True:
            self.sale = "is for sale"
        else:
            self.sale = "is not for sale"

    def drive(self):
        print(f"You are driving the {self.model}")

    def stop(self):
        print(f"You have stopped the {self.model}")

    def describle(self):
        print(f"You have a {self.year} {self.color} {self.model} and it {self.sale}")