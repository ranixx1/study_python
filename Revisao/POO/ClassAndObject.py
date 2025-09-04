class Pessoa:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def dispaly_info(self):
        print(f'nome: {self.name} e idade: {self.age}')

person_1 = Pessoa("Ranilton",20)
person_2 = Pessoa("Maneo",19)

person_1.dispaly_info()
person_2.dispaly_info()
