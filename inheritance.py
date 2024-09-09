class Vehical:
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        pass
        print(f"Vehical Name: {self.name}\nModel: {self.model}\nYear: {self.year}")

class Car(Vehical):
    def __init__(self,name,model,year,number_of_doors):
        super().__init__(name,model,year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"No_of_Doors: {self.number_of_doors}")

class Motorcycle(Vehical):
    def __init__(self,name,model,year,engine_type):
        super().__init__(name,model,year)
        self.engine_type = engine_type
    
    def display_info(self):
        super().display_info()
        print(f"Engine_Type: {self.engine_type}")

class Truck(Vehical):
    def __init__(self,name,model,year,payload_capacity):
        super().__init__(name,model,year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        super().display_info()
        print(f"Payload_capacity: {self.payload_capacity}")


class Garage:
    def __init__(self):
        self.vehicals = []

    def add_vehical_details(self,vehical):
        self.vehicals.append(vehical)

    def vehical_info(self):
        for i in self.vehicals:
            i.display_info()
            print('----------')

car = Car("XUV","Zn1000",2024,4)
motorcycle = Motorcycle("TVS Jupite","120CC",2023,"petrol")
truck = Truck("TATA MAHENDHRA",'TOP NOTCH',2024,"4 TONS")

garage = Garage()
garage.add_vehical_details(car)
garage.add_vehical_details(motorcycle)
garage.add_vehical_details(truck)
garage.vehical_info()