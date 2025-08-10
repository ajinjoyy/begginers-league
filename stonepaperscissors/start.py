import random

class Start():
    def __init__(self) -> None:
        print(".................................")
        print("WELCOME TO STONE,PAPER,SCISSORS")
        print(".................................")
        self.times=int(input("enter the destination point:"))
        self.gamestate = True
        self.user_point = 0
        self.system_point = 0
    
    def user_point_increment(self):
        self.user_point += 1

    def system_point_increment(self):
        self.system_point += 1

    def data(self, get):
        self.datadict = {"stone": 1, "paper": 2, "scissors": 3}
        return self.datadict.get(get)

    def display(self):
        print(f"User: {self.user_point}\nSystem: {self.system_point}")

    def game(self):
        avail_list = ["stone", "paper", "scissors"]
        i = 1

        while i < 100 and self.gamestate:
            print("............................................")
            print(f"ROUND {i} first to {self.times} points wins")
            print("............................................")

            print("1-stone\n2-paper\n3-scissors\n")
            user_choice = int(input("Enter your choice (1-3): "))
            if user_choice==1:
                print("user:stone")
            elif user_choice==2:
                print("user:paper")
            else:
                print("user:scissors")
            
            # Validate user input
            if user_choice not in [1, 2, 3]:
                print("Invalid choice. Please enter a number between 1 and 3.")
                continue

            system_choice = random.choice(avail_list)

            print(f"system:{system_choice}")

            if user_choice == self.data(system_choice):
                print("It's a tie!")
            elif (user_choice == 1 and system_choice == "scissors") or \
                 (user_choice == 2 and system_choice == "stone") or \
                 (user_choice == 3 and system_choice == "paper"):
                print("User wins this round!")
                self.user_point_increment()
            else:
                print("System wins this round!")
                self.system_point_increment()

            self.display()

            if self.user_point >= self.times:
                print("///////////////////")
                print("User wins the game!")
                print("///////////////////")
                self.gamestate = False
            elif self.system_point >= self.times:
                print("/////////////////////")
                print("System wins the game!")
                print("/////////////////////")
                self.gamestate = False

            i += 1

start = Start()
start.game()

