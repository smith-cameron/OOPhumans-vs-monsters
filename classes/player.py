class Player:
    total_players = 0
    def __init__(self):
        self.health = 100
        self.isLiving = True

    def show_stats( self ):
        raise NotImplementedError
        

    def attack ( self , victim, weapon = False ):
        if self.can_attack(self):
            if victim.isLiving:
                if weapon:
                    victim.health -= (weapon.damage*self.speed)
                else:
                    victim.health -= (self.strength*self.speed)
                if victim.health <= 0:
                    victim.isLiving = False
                    print(f"{self.name} is the victor over {victim.name}.\n")
                    if self.total_monsters:

                        print(self.total_monsters)
                    else:
                        print(self.total_humans)
            else:
                print(f"Dont kick a dead {victim.name}.\n")
        else:
            print(f"You cant attack {victim.name}... your dead.\n")
        return self

    @staticmethod
    def can_attack(attacker):
        if attacker.isLiving:
            return True