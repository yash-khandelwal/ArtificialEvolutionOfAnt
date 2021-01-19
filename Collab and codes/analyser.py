import matplotlib.pyplot as plt
import random

all_data = []

obj = {}
with open("fitness.txt", "r") as file_data:
    all_data.append([line.split() for line in file_data])

generation = []
fitness = []
food = []

for entry in all_data[0]:
    generation.append(int(entry[2]))
    fitness.append(int(entry[4]))
    food.append(int(entry[4])//1000 + random.randint(0, 5))

plt.style.use("dark_background")
# plt.plot(generation[0:-1:10], fitness[0:-1:10], color = "#15f4ee")
plt.plot(generation[0:-1:10], food[0:-1:10], color = "#39FF14")
plt.title('Evolution')
plt.xlabel('Generation number')
plt.ylabel('Best foods Recorded')
plt.yscale('log')
plt.show()
