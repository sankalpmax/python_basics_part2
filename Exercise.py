height = int(input("what is your height? "))
unit = input("(F)feet or (M)meters?  ")

if unit.upper == "F":
   converted = height / 1.05
   print("height in Feet" +str(converted))
else:
    converted = height * 1.05   
    print("height in meters" +str(converted))