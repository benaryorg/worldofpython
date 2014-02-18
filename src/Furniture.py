from Object import Object

class Furniture(Object):
    def __init__(self,mass,material,color):
        Object.__init__(self,mass=mass,color=color)
        self.setMaterial(material)

    def __str__(self):
        return ';'.join([self.material,Object.__str__(self)])

    def setMaterial(self,material):
        self.material=str(material)

class Sittable(Furniture):
    def __init__(self,mass,material,maxpersons,color,sitting=0):
        Furniture.__init__(self,mass,material,color)
        self.setMaxPersons(maxpersons)
        self.setSitting(sitting)

    def __str__(self):
        return ';'.join([str(self.sitting),str(self.maxpersons),Furniture.__str__(self)])

    def setMaxPersons(self,persons):
        persons=int(persons)
        if persons>=0:
            self.maxpersons=persons
        else:
            raise ValueError('Value cannot be negative!')

    def setSitting(self,sitting):
        sitting=int(sitting)
        if sitting>=0:
            if sitting<=self.maxpersons:
                self.sitting=sitting
            else:
                raise ValueError('No space left!')
        else:
            raise ValueError('Value cannot be negative!')

    def sitDown(self,count=1):
        count=int(count)
        self.setSitting(count+self.sitting)

    def standUp(self,count=1):
        count=int(count)
        self.setSitting(self.sitting-count)

class Chair(Sittable):
    def __init__(self,mass,material,color,maxpersons=1,sitting=0):
        Sittable.__init__(self,mass,material,maxpersons,color,sitting)

