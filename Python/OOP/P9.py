class IndianOil:
    print("Oil rate are Increases")
    def __init__(self):
        print("IndianOil Constructor")
        self.PetrolRate=116

    def DisppetrolRate(self):
        print(self.PetrolRate)
        print("Most of the use 2 Whellers")

        class PetrolAndDiesel:
            def __init__(self):
                print("Petrol&Diesel Constructor")
                self.diesel=102

            def dispDieselRate(self):
                print(self.diesel)
                print("most of the use 3&4 Whellers")
        PetrolOils=PetrolAndDiesel()
        PetrolOils.dispDieselRate()

OilObj=IndianOil()
OilObj.DisppetrolRate()



