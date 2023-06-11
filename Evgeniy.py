class KgToPounds:
    def __init__(self, kg):
        self.kg = kg

    def to_pounds(self):
        return self.kg * 2.205
   
    def kg(self):
        return self.kg

    def kg(self, new_kg):
        if example(new_kg, (int, float)):
            self.kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')
 
weight = KgToPounds(15)
print(weight.to_pounds())
print(weight.kg)
weight.kg = 35
print(weight.kg)
weight.kg = 'пять'