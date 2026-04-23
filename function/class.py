class InputOutput:
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input("Enter string: ")
    def printString(self):
        return self.s.upper()
        # print(self.s.upper())

obj  = InputOutput()
# print("Enter your String:", obj.getString())
obj.getString()
result = obj.printString()
print("String in upper case:", result)