# Encapsulation Examples
# Parent class
class Player:
    def play(self):
        pass
    
# Child class inherits parent class method
class FootballPlayer(Player):
    def __init__(self, plays="Football"):
        self._plays = plays
    # inherits parent class method but implements differently
    def play(self):
        print(f"Football player plays {self._plays} with 'Football'")
        
class CricketPlayer(Player):
    def __init__(self, plays="Cricket"):
        self._plays = plays
    # Inherits parent class method but implements differently
    def play(self):
        print(f"Cricket player plays {self._plays} with 'Bat &  Cricket-Ball'")
        
# Create objects of child class
player_type_1 = FootballPlayer()
player_type_2 = CricketPlayer()

""" 
    Call the play method that is same in 
    parent & child class but acts differently
"""
player_type_1.play()
player_type_2.play()