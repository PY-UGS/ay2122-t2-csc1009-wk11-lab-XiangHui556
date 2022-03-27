# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class calculator:
    def adder(self):
        print("Adder")
        input1 = float(input("Please enter input1: "))
        input2 = float(input("Please enter input2: "))
        return input1 + input2
        
    def subtractor(self):
        print("Subtractor")
        input1 = float(input("Please enter input1: "))
        input2 = float(input("Please enter input2: "))
        return input1 - input2
        
    def multiplier(self):
        print("Multiplier")
        input1 = float(input("Please enter input1: "))
        input2 = float(input("Please enter input2: "))
        return input1 * input2
        
    def divider(self):
        print("Divider")
        input1 = float(input("Please enter input1: "))
        input2 = float(input("Please enter input2: "))
        return input1 / input2
        
    def clear():
        return 0

cal = calculator()

print("Adder:" + str(cal.adder()))
print("Subtractor:" + str(cal.subtractor()))
print("Multiplier:" + str(cal.multiplier()))
print("Divider:" + str(cal.divider()))
print("Clear:" + str(cal.clear()))