class A:
    def first_method(self):
        print("METHOD OF CLASS A..")
class B:
    def first_method(self):
        print("METHOD OF CLASS B...")
class C(A,B):
    def third_method(self):
        print("METHOD OF CLASS C...")

ob=C()
ob.first_method()
ob.third_method()
