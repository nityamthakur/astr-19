class Animal:
    def __init__(self,arms,legs,eyes,tail,furry):
        self.arms= float(arms)
        self.legs= float(legs)
        self.eyes= int(eyes)
        self.tail= bool(tail)
        self.furry= bool(furry)

    def describe(self):
        print('Length of arms:',self.arms)
        print('Length of legs:',self.legs)
        print('Number of eyes:',self.eyes)
        print('Does it have a tail?:',self.tail)
        print('Is it furry?:',self.furry)
