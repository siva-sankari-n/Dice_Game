import random

class Dice:

    def __init__(self):
        self._value=None

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value=random.randint(1,6)
        self._value=new_value
        return new_value
    


class Player:

    def __init__(self,die,is_computer=False):
        self._die=die
        self._is_computer=is_computer
        self._counter=10

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter+=1

    def decrement_counter(self):
        self._counter-=1

    def roll_dice(self):
        return self._die.roll()
    
class DiceGame:

    def __init__(self,player,computer):
        self._player=player
        self._computer=computer

    def play(self):
        print("="*40)
        print("Welcome to Dice Game")
        print("="*40)

        round=1
        while True:
            self.play_round(round)
            game_over=self.check_game_over()
            round+=1
            if game_over:
                break


    def play_round(self,round):
        
        self.print_round_welcome(round)

        #Roll the dice  
        player_value=self._player.roll_dice()
        computer_value=self._computer.roll_dice()

        #Show the values
        self.show_dice(player_value,computer_value)


        if player_value > computer_value :
            print("You won the Game")
            self.update_counters(winner=self._player,loser=self._computer)

        elif computer_value > player_value :
            print("The Computer won the game . try again")
            self.update_counters(winner=self._computer,loser=self._player)

        else:
            print ("It's a tie !")

        #Show Counters
        self.show_counter()
        

    def print_round_welcome(self, round_no):
        print(f"\n--------- Round {round_no} ---------")
        input("🎲 press any key to role the Dice 🎲")

    def show_dice(self,player_value,computer_value):
        print(f"\nYour Die : {player_value}")
        print(f"Computer Die: {computer_value}")

    def update_counters(self,winner,loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counter(self):
        print(f"\nYour Score : {self._player.counter}")
        print(f"Computer Score : {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False
        
    def show_game_over(self,winner):
        if winner.is_computer:
            print("\n=========================================")
            print("🎮 G A M E O V E R 🎮")
            print("\n=========================================")
            print("Computer Won the game ! Try Again")
            print("="*40)
        else:
            print("\n=========================================")
            print("🎮 G A M E O V E R 🎮")
            print("\n=========================================")
            print("You Won the game!! Congratulations")
            print("="*40)



player_die=Dice()
computer_die=Dice()

my_player=Player(player_die,is_computer=False)
computer_player=Player(computer_die, is_computer=True)

game = DiceGame(my_player,computer_player)

# game.play()

a=257
b=257

print(a is b)


