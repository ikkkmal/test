import sys
class cars:

        def __init__(self, car_list):
                self.av_car= car_list
                av_car=("Proton Wira", "Perodua Myvi")

        def display_avcars(self):
                print("<<< The available car are as >>>")
                print(35* "= ")
                print()
                for car in self.av_car:
                        print(car)

        def lend_car(self, req_car):
                if req_car in self.av_car:
                        print()
                        print("Car is rented!")
                        print()
                        self.av_car.remove(req_car)
                else:
			print("Sorry, this car is unavailable")

        def add_car(self, returned_car):
                self.av_car.append(returned_car)
                print()
                print("Thanks for using our service. Have a good day!")

        #PAYMENT

        print("Each car payment starts from $35 per day, the total price will be counted with the appropriate discount.")
        days=int(input("How many days do you want to rent the car?"))
        name=input("Enter your full name: ")

        def car_cost(days):
                if days<= 3:
                        return(days*35)
                elif days<= 7:
                        return(days*35)-15
		else:
			return(days*35)-40

        print("Total amount: RM", (car_cost(days)))
        print("Deposit: RM", int(car_cost(days)/3))

        cash= int(input("Amount of cash to be deposit: RM"))

        if cash>= (car_cost(days)/3):
                print("Amount due: RM", (car_cost(days)-cash))

        else:
                print("Insufficient amount, insert the required amount")

class tenant:

        def req_car(self):
                print("<<< Enter name of the car that you chosse same as it was displayed >>>")
                self.car=input()
                return self.car

def main():
        vehicles= cars(["Proton Wira", "Perodua Myvi"])
        person= tenant()
        done= False
        while done== False:
                print()
                print("********")
                print("1. Display all available cars")
                print("2. Rent car")
                print("3. Return car")
                print("4. Exit")
                choice= int(input("Choose the car of your choice: "))
                if choice== 1:
                        vehicles.display_avcars()
                elif choice== 2:
                        vehicles.lend_car(person.req_car())
                elif choice== 3:
                        vehicles.add_car(person.return_car())
                elif choice== 4:
                	sys.exit()

main()
