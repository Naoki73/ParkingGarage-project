#This can be a little flexible
# 3 Methods: takeTicket, parForParking, leaveGarage
# few attributes: tickets - list, parkingSpaces - list, currentTicket - dictionary


class Garage():


    def __init__(self, tickets, parkingSpaces):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = {}

    def TakeTicket(self):
        if self.parkingSpaces <= 0:
            print("Sorry, there is no parking space left.")
            return
        
        if self.tickets > 0:
            self.tickets -= 1
        else:
            print("You have no tickets to give.")
            
        self.parkingSpaces -=1
        

       
    
    def payForParking(self, pay=None):
        
        pay = input("How much would you like to pay?: ")

        if int(pay) > 0:
            self.currentTicket['paid'] = True
            print("Thank you for paying! You have 15 minutes to exit the garage.")

        elif pay is None:
            print("We have not yet recieved payment.")

        elif int(pay) <= 0:
            print("We have not yet recieved payment.")

    

    def leaveGarage(self):
        if self.currentTicket.get('paid'):
            print("Thank you, have a nice day!")

            
            
        else:
            pay = input("Please enter payment: ")
            
            while int(pay) <= 0:
                pay = input("Please enter a payment of 1 or more: ")
            else:
               print("Thank you, have a nice day!")
               
       
        self.parkingSpaces += 1
        self.tickets += 1    


garage = Garage(10,0)
garage.TakeTicket()
garage.payForParking()
garage.leaveGarage()


