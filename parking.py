#This can be a little flexible
# 3 Methods: takeTicket, parForParking, leaveGarage
# few attributes: tickets - list, parkingSpaces - list, currentTicket - dictionary


class Garage():


    def __init__(self):
        self.tickets = []
        self.parkingSpaces = []
        self.currentTicket = {}

    def TakeTicket(self):
        if ticket in self.tickets:
            self.tickets - 1
        else:
            print("You have no tickets to give.")
        
        self.parkingSpaces - 1
    
    def payForParking(self, pay):
        
        payment = input("How much would you like to pay?")
        
        if pay in payment:
            print("Thank you for paying! You have 15 minutes to exit the garage.")
            currentTicket(paid) = True

    

    def leaveGarage(self):
        if pay not in payment:
            print("We have not yet recieved payment.")
            self.payForParking(pay)
            
        elif pay in payment:
            print("Thank you, have a nice day!")

            self.parkingSpaces + 1
            self.tickets + 1

