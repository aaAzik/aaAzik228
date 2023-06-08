class Azamat:

    def club(self):
        result = None
        if self.age < 15:
            result = f'{self.name} вы не можете получить доступ!'
        else:
            result = f'{self.name} Добро пожаловать!'
        return result

    def __init__(self, name, surname, age):
        self.name = name
        self.age = age
        self.surname = surname

    def sd(self):
        return f'{self.surname} - {self.name} - {self.age}'


azamat = Azamat(name='Azamat', surname='Urazimbetov', age=15)
print(f'{azamat.sd()} {azamat.club()}')

izzat = Azamat(name='Izzat', surname='Orifjonivich', age=15)
print(f'{izzat.sd()} {izzat.club()}')

sultan = Azamat(name='Sultan', surname='Abdiramanov', age=15)
print(f'{sultan.sd()} {sultan.club()}')
