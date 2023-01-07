import random
class Dog:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_play(self):
        print("Time to play")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
    def to_wash(self):
        print("Need to wash")
        self.gladness += 2
        self.progress += 1
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress ={round(self.progress, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_play()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_wash()
        elif live_cube == 4:
            self.to_chill()
            self.end_of_day()
            self.is_alive()

patron = Dog(name="Patron")

for day in range(365):
    if patron.alive == False:
        break
    patron.live(day)