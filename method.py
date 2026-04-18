class A:
    def first_method(self):
        print("METHOD OF CLASS A..")
class B(A):
    def second_method(self):
        print("METHOD OF CLASS B...")
class C(B):
    def third_method(self):
        print("METHOD OF CLASS C...")

ob=C()
ob.first_method()
ob.second_method()
ob.third_method()
C().third_method()
C().first_method()
C().second_method()
    
