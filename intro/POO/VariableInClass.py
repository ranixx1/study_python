class Estudante:
    school = 'IFRN'

    def __init__(self,name):
        self.name = name

s1 = Estudante('Ranilton')
s2 = Estudante('Ramon')
s3 = Estudante('Agenor')

print(s1.school)
print(s2.name)