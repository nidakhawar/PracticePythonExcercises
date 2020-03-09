class Bird:

    fly=True

    def noise(self):
        print("Birdnoise")
    babies=0
    
    def reproduce(self):
        self.babies+=1
    
    def eat(self):
         pass

extinct=False

class Owl(Bird):

    def reproduce(self):
        self.babies+=6

    def eat(self):
        print("Peck Peck")

class Dodo(Bird):
    fly=False
    extinct=True

    def eat(self):
        print("Non Nom")

    def reproduce(self):
        if self.extinct==False:
            self.babies +=1
        else:
            print("No more dodo's")
Rio=Dodo()
Rio.eat()
Rio.reproduce()
print(Rio.babies)