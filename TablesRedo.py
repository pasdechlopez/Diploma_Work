import numpy as np
import math
import matplotlib.pyplot as plt

M = 21  # количество строк в массиве
order = 3 #порядок столбца со значениями углов
data = []
with open('/Users/pasdechlopez/Downloads/dLATEX/YK2/YK2_20_000.txt', 'r') as file:    
     
   for line in file:
        data.append([str(x) for x in line.split()])

data.pop(0)
print('data = ', data[0][0])

I = []
for i in range(0,M):
	I.append(data[i][order+1])

print(type(I[0]))
	

#_________________________Intensity block___________________

#print(I)
Int = list(map(float, I))
Intensity = []
Intensity_Sheer = []

for i in Int:
	Intensity_Sheer.append('%.4g' %(i))
#print('Int = ', type(Int[0]))
for i in Int:
	Intensity.append('%.4g' %((i)*14/max(Int)))
#print('Int = ', type(Int[0]))
Intensity = list(map(float, Intensity))

"""Intensity_reversed = []
for i in Intensity:
	Intensity_reversed.append(i)
max_Intensity_2 = 0
Intensity_reversed.reverse()
for i in Intensity_reversed:
	if i > max_Intensity_2 and i < max(Intensity_reversed):
		max_Intensity_2 = i
		i += 1
print('max_Intensity_2 = ', max_Intensity_2)
print('index(max(Intensity_reversed) = ', Intensity_reversed.index(max_Intensity_2))
print('index(min(Intensity_reversed) = ', Intensity_reversed.index(min(Intensity)))

max_Intensity = 0
for i in Intensity_reversed:
	if i > max_Intensity:
		max_Intensity = i
		i += 1
print('max_Intensity = ', max_Intensity)
print('max_Intensity index = ', Intensity_reversed.index(max_Intensity))
print('max_Intensity_2 index = ', Intensity_reversed.index(max_Intensity_2))

print('Intensity_reversed = ', Intensity_reversed)


#for j in I:
#	Intensity.append('%.4g' % (j/max(I)*100))
#print(Intensity)
I.reverse()
#print(max(I))
#print('I = ', I)

Intensity_reversed_mirrored_right = []
j = 0
for j in range(0,14): 
	Intensity_reversed_mirrored_right.append(Intensity_reversed[j])
Intensity_reversed_mirrored_right.reverse()
print('Intensity_reversed_mirrored_right =', Intensity_reversed_mirrored_right)"""

#*************************ANGLES BLOCK__________________________

theta = [] #создание списка со значениями углов
for k in range(M):
	theta.append((data[k][order]))
theta = list(map(int, theta))
theta_reversed = []

for k in theta:
	theta_reversed.append(k)

#print('theta = ', theta, '\n', 'theta_reversed = ', theta_reversed)
angles = [] #создание списка углов в радианах
for i in theta:
	angles.append((i)*np.pi/180)
#print('angles = ', angles)
angles_reversed = [] #создание списка отраженных углов 
for i in theta_reversed:
	angles_reversed.append((-i)*np.pi/180)
"""angles_reversed.reverse()
#theta_reversed.reverse()
angles_reversed_mirrored_right = []
for i in theta:
	angles_reversed_mirrored_right.append((i+250-min(angles_reversed[0:14]))*np.pi/180)
#print('angles_reversed_mirrored_right', angles_reversed_mirrored_right, min(theta_reversed[0:14]))

angles_reversed_mirrored_left = []
for i in theta:
	angles_reversed_mirrored_left.append((i+73-min(angles_reversed[0:14]))*np.pi/180)
print('angles_reversed_mirrored_left', angles_reversed_mirrored_left)

angles_mirrored_right = []
for i in theta:
	angles_reversed_mirrored_left.append((i+73-min(angles[0:14]))*np.pi/180)
print('angles_reversed_mirrored_left', angles_reversed_mirrored_left)
#print('angles_reversed = ', angles_reversed)
#print('theta = ', angles)
#print(len(Intensity), len(theta))
#print('Intensity =', Intensity, '\n', 'theta = ', angles)
#print(len(angles), len(angles_reversed), len(Intensity))
"""

	
#print('angles_reversed_mirrored_right =', angles_reversed_mirrored_right)
#for i in range(len(angles)):
#	angles_reversed.append(i)
#If '45' in angles_reversed:
	#return True
#print(len(angles_mirrored_right[0:14]), len(Intensity_reversed[9:23]))

#***********************PLOT BLOCK*************************

#for P in angles:
#	Intensity_reversed.append((((angles+180)*np.pi/180)))
#ax = plt.sublot(111, projection = 'polar')
ax = plt.subplot(111, projection='polar')
AX_reversed = ax.scatter(angles_reversed, Intensity_Sheer, color = 'y', label = 'Theory')
AX_reversed_line = ax.plot(angles_reversed, Intensity_Sheer,  ls = '-', lw = '0.4')
AX = ax.scatter(angles, Intensity_Sheer, color = 'g', label = 'Experiment')
AX_line = ax.plot(angles, Intensity_Sheer, ls = '-', lw = '0.4')
#AX_reversed_mirrored_right = ax.scatter(angles_reversed_mirrored_right[0:14], Intensity_reversed_mirrored_right, color = 'green')
#AX_reversed_mirrored_left = ax.scatter(angles_reversed_mirrored_left[0:14], Intensity[0:14], color = 'green')
#AX_mirrored_right = ax.scatter(angles_mirrored_right[0:14], Intensity_reversed[8:23], color = 'yellow')
#AX_mirrored_left = ax.scatter(angles_mirrored_left[0:14], Intensity_mirrored_left, color = 'yellow')
ax.legend()
ax.set_theta_zero_location("S")

#ax.set_rmin(min(Intensity))
#ax.set_rmax(15)
plt.show()