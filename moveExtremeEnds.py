import random as rd

from matplotlib.pylab import rand


list = [1,2,3,4,5,6,7,8]

# generate any random index

rand_idx = rd.randint(0,7)
print("random index",rand_idx)

if rand_idx == 0 or rand_idx == 7:
    print("I am already at one extreme end :",rand_idx)

# if this index is not at extreme end then move it to one of the extreme ends
#but towards the end which is closer to it

else:
    if rand_idx < 4:
        print("I am moving to left extreme end")
        list.insert(0,list[rand_idx])
        list.pop(rand_idx+1)
    else:
        print("I am moving to right extreme end")
        list.append(list[rand_idx])
        list.pop(rand_idx)