import random

ranNum = []


for x in range(100):
  numbers = (random.randint(10,100))
  ranNum.append(numbers)
print(ranNum)
print("")
print("")
print("")




my_dictionary = {
"favFood": "Sushi",
"favMovie": "Finding Nemo",
"favCar": "Lincoln MKZ",
"favScent": "Vanilla",
"favNum": "823"
}
print("My favourite things:")
print("")
for key in my_dictionary.items():
  print(key)