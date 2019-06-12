import random 

samples=int(input("Number of samples: "))
highest_num=int(input("Range: 0-"))
ones=0

for q in range(samples):
    x = random.randint(0,highest_num)
    if x==1:
        ones+=1

print("\n\n",ones/samples)
