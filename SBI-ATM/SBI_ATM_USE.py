from SBI_Module import SBI_ATM1 as Sb
# From module import class(pythonFile) as "sb"

name = input("Enter Your Name : ")
obj = Sb.SbiAtmClass(name)  # refrance of module class "sb" & class name "SBI_ATM"
obj.greet_user()
obj.transaction()
obj.exitGreet()
