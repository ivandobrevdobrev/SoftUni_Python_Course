class Car:
    cars_counter = 0  # отнасясе само за класа - атрибут на класа който се отнсася  и ползва за всички инстанции
    def __init__(self, brand, model, year): # Metod ( kogato se namira v Class se naricha metod),instanciq ,constructor - zadavat se instance atributite
        self.brand = brand  # brand, model,year sa атрибути на инстанцията
        self.model = model  # self - означава че работи за обекта ( car1, car2..)za който съм го извикал
        self.year = year


car1 = Car("Mercedes",190,1998)   #car1 e instanciq, obekt по тозо начин извикваме обекта car1 от класа Car
print(car1.brand)
print(car1.model)
car1.brand = "BMW"
print(car1.brand)
car1.cars_counter = 2 # изпозваме го като инстанс атрибут и му променяме ст-ста
print(car1.cars_counter) # викаме cars_counter като атрибут на Инстанцията
print(Car.cars_counter) # викаме cars_counter като атрибут на Класа


