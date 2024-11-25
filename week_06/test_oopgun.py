class GUN:
    def __init__(self,name,ammo):
            self.name = name
            self.ammo = ammo
    def add_ammo(self,ammo):
            self.ammo += ammo
    def fire_ammo(self):
            if self.ammo > 0:
                self.ammo -= 1

                
gun1 = GUN('M1911',7+1)
while True:
    gun1.fire_ammo()
    print(gun1.ammo)
    if gun1.ammo <= 0:
        r = str(input("wanna reloand? : "))
        if r == 'y' or r == 'yes':
            gun1.add_ammo(7+1)
        elif r == 'n' or r == 'no':
            print('กระสุนหมด')
        