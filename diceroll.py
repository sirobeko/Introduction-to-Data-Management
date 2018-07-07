import numpy as np
dice = np.random.randint(1,6,2)
for i in range(2):print("Die%d:"%int(i+1),dice[i])
print("Total value:",sum(dice))

