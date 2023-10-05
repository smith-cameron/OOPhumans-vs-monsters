from classes.player import Player
class Human(Player):
  total_humans = 0
  def __init__(self):
    super().__init__()
    Human.total_humans += 1
    Player.total_players += 1

  def attack ( self , victim, weapon = False ):
    return super().attack( victim, weapon)

  def show_stats(self):
    print(f"{self.total_humans} Humans left \n Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nIsLiving: {self.isLiving}\n")


# print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nIsLiving: {self.isLiving}\n")