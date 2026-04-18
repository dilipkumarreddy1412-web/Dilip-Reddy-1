class A:
    def first_method(self):
        print("METHOD OF CLASS A..")
class B(A):
    def first_method(self):
        print("METHOD OF CLASS B..")
class C(B):
    def first_method(self):
        print("METHOD OF CLASS C1..")
    def third_method(self):
        print("METHOD OF CLASS C2..")
        super().first_method()
        
ob=C()
ob.third_method()
