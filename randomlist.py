#create a random list in python
import random as r

list = [3,7,10,12,3,36,80,78,22,34]

print("List is :\n",list)

# for i in list:
#     print(list.count(i))
#print(count)


for num in list:
    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

    if prime:
        #print(num, "is a prime number")
        #count frequency of prime numbers in the list
        frequency = list.count(num)
        print( num, " is a prime number :", frequency,"times")

#add an element at random position in the list so that mean of list should be reduced by actual mean of list


actual_mean = sum(list) / len(list)
print("Actual mean :", actual_mean)

# Generate a random element that is less than the actual mean
random_element = r.uniform(0, actual_mean)

# Insert the random element at a random position in the list
random_position = r.randint(0, len(list))
list.insert(random_position, random_element)

print("List after adding random element :\n", list)
print("New mean :", sum(list) / len(list))