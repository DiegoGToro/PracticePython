class A():
    def primera(self):
        return "Esta es la clase A"
class B():
    def segunda(self):
        return "Esta es la clase B"
    
class C(A, B):
    pass

claseC = C()
print(claseC.primera())
print(claseC.segunda())