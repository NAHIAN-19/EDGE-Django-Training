# Polymorphism Examples
# Parent class
class Player:
    def play(self):
        pass
    
# Child class inherits parent class method
class FootballPlayer(Player):
    # inherits parent class method but implements differently
    def play(self):
        print(f"Football player plays football with 'Football'")
        
class CricketPlayer(Player):
    # Inherits parent class method but implements differently
    def play(self):
        print(f"Cricket player plays cricket with 'Bat &  Cricket-Ball'")
        
# Create objects of child class
player_type_1 = FootballPlayer()
player_type_2 = CricketPlayer()

""" 
    Call the play method that is same in 
    parent & child class but acts differently
"""
player_type_1.play()
player_type_2.play()