class Alligator:
    def __init__(self,color, length, mood, age):
        self.color= color
        self.length= length
        self.mood= mood
        self.age= age


    def __repr__(self):
            return '({}, {}, {}, {})'.format(self.color, self.length, self.mood, self.age)


Alligator1= Alligator("green", 20, "ferocious", 10)
Alligator2= Alligator("dark green", 15, "calm", 2)
Alligator3= Alligator("black", 45, "angry", 15)

alligators= [Alligator1, Alligator2, Alligator3]

def sortalligators_color(allig):
    return allig.color

def sortalligators_length(allig):
    return allig.length

def sortalligators_mood(allig):
    return allig.mood

def sortalligators_age(allig):
    return allig.age


sorted_alligators_color= sorted(alligators, key= sortalligators_color)
sorted_alligators_length= sorted(alligators, key= sortalligators_length)
sorted_alligators_mood= sorted(alligators, key= sortalligators_mood)
sorted_alligators_age= sorted(alligators, key= sortalligators_age)

print(alligators)

print("Object sorted by color:", sorted_alligators_color)
print("Objects sorted by length:", sorted_alligators_length)
print("Objects sorted by mood:", sorted_alligators_mood)
print("Objects sorted by age:", sorted_alligators_age)
