from playsound import playsound

class Animal():
    sound = None
    def make_sound(self):
        playsound(self.sound)

class Dog(Animal):
    sound = 'Lesson7/dog-bark-15.mp3'

class Cat(Animal):
    sound = 'Lesson7/kitten_crying.mp3'
    
class Cow(Animal):
    sound = 'Lesson7/farm-ambience.mp3'

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()

cow = Cow()
cow.make_sound()