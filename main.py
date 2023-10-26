#implement a function that will flatten and sort an array of integers in ascending order
#and which adheres to a functional programming paradigm.
def flatten_and_sort(array):
  # Use list comprehensions to flatten the nested arrays
  arr = []
  for item in array:
    for i in item:
      arr.append(i)
  return sorted(arr)

  # Example usage:


nested_list = [[3, 1, 4], [1, 5, 9], [2, 6, 5]]
sorted_result = flatten_and_sort(nested_list)
print(sorted_result)

#how does this solution ensure data immutability
# this solution ensure data immutability because it doesn't change or delete the data.

#Is this solution a pure function? Why or why not?
#It is a pure function because it produce the same output for the same input and do not have side effects.

#Is this solution a higher order function? Why or why not?
#The soluton is not a higher function because there are no function as arguments and it doesn't return a function as a result.

#Would it have been easier to solve this problem using a different programming style?
#I don't believe so.

#Why in particular is functional programming a helpful paradigm when solving this problem?
#Functional programing is very concise, predictable and it reduces side effects.

#Watto needs a new system for organizing his inventory of podracers.


# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
class Podracer:

  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

#Define a repair() method that will update the condition of the podracer to "repaired".

  def repair(self):
    self.condition = "repaired"


#Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.


class AnakinsPod(Podracer):

  def boost(self):
    self.max_speed *= 2

#Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

class SebulbasPod(Podracer):
  
    def flame_jet(self, other):
      other.condition = "trashed"


# Example usage:
anakins_pod = AnakinsPod(max_speed=600, condition="perfect", price=1000)
sebulbas_pod = SebulbasPod(max_speed=500, condition="perfect", price=800)

print("Anakin's Podracer:")
print(f"Max Speed: {anakins_pod.max_speed}")
print(f"Condition: {anakins_pod.condition}")
print(f"Price: ${anakins_pod.price}")
anakins_pod.boost()
print("After Boost:")
print(f"Max Speed: {anakins_pod.max_speed}")
anakins_pod.repair()
print("After Repair:")
print(f"Condition: {anakins_pod.condition}")

print("\nSebulba's Podracer:")
print(f"Max Speed: {sebulbas_pod.max_speed}")
print(f"Condition: {sebulbas_pod.condition}")
print(f"Price: ${sebulbas_pod.price}")
sebulbas_pod.flame_jet(anakins_pod)
print("Anakin's Podracer Condition After Flame Jet:")
print(f"Condition: {anakins_pod.condition}")
