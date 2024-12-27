# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.


class Train:
    def __init__(self,number,name,seats,fare):
        self.number = number
        self.name = name
        self.seats = seats
        self.fare =fare

    def available_seats (self):
        return self.seats
    
    def book_seats (self,req_seats):
        if (self.seats >= req_seats):
            self.seats -= req_seats
            print(f"{req_seats} seats booked & total cost is {self.fare*req_seats}")
        else:
            print("not enough seats available")
    
    def get_fare(self):
        return self.fare
    
    def get_train_details(self):
        print(f"{self.number}    #  {self.name}  #  {self.seats}   # {self.fare}")

t1 = Train(22956,"Kutchh express",300,550)
t2 = Train(12789,"chennai express",500,850)
t3 = Train(29671,"kashmir express",800,1000)

user_option = 0

while (user_option !=4):
    user_option = int(input(
        """
        select the option
        1. get the information about the trains
        2. get fare information 
        3. book train tickets 
        4. exit

        """
    ))
    if (not(user_option in [1,2,3,4])):
        print("incorrect input! re-run the program")
        break
    elif (user_option ==4):
        break
    elif (user_option ==1 or user_option==2):
        print(f"Train number #  Train Name # Available seats # Fare")
        print(f"***************************************************")
        print("1.",end="")
        t1.get_train_details()
        print("2.",end="")
        t2.get_train_details()
        print("3.",end="")
        t3.get_train_details()
    elif (user_option==3):
        user_input_train_num =int(input("enter a train number to book tickets: "))
        user_input_req_seats =int(input("enter number of seats reuqired to book: "))
        if (user_input_train_num == t1.number):
            t1.book_seats(user_input_req_seats)
        elif (user_input_train_num == t2.number): 
            t2.book_seats(user_input_req_seats)
        elif (user_input_train_num == t3.number ):
            t3.book_seats(user_input_req_seats)
        else:
            print("incorrect input! re-run the program")
            break
    else:
        user_option==4









