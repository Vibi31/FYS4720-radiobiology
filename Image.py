import matplotlib.pyplot as plt
import numpy as np
import imageio as io

#importing the  blotting images as grey scales
img = io.imread("im.jpg", as_gray=True)

#convert to numpy array for speeding up programme 
im_ar = np.array(img) 
"""
print('image shape = ', np.shape(im_ar)) #Checking if we get 2d image shape ie. no colour channels
plt.figure()
plt.imshow(img, cmap = 'gray', vmin = 0, vmax =255)
plt.title('Western blotting')
plt.show()
"""

group_1x = [138, 119, 258, 317, 375, 435]   #xposition of viculin line strip
vic_1y, p53_1y = 118, 270                 #our y starting positions for viculing strip and p53 strip

group_2x = [214, 261, 322, 386, 448, 513]
vic_2y, p53_2y = 218, 852

group_3x = [160, 221, 288, 344, 405, 468]
vi_3y, p53_3y = 1150, 1326

"""
the above values represent the top right corner for our sample area,
in the forloop, the sample square will be calculated
"""
def val(name,x,y):
    vals = []

    for i in range(40):  #44*7 is our sample size of the flourescent parts
        for j in range(4):
            vals.append(im_ar[y+j, x+i])

    average = np.average(vals)

    print(f'piksel value for {name} is {average:.1f}')
    return average
    

def sample(name, x_list, y):
    points = []
    for x in x_list:
        points.append(val(name, x, y))
    
    return points

#sample('viculin strip group 1', group_1_x, strip_1y)

print(' ')
g1 = sample('p53 strip group 1', group_1x, p53_1y)

print(' ')
g2 = sample('p53 strip group 2', group_2x, p53_2y)

print(' ')
g3 = sample('p53 strip group 3', group_3x, p53_3y)

dose = [0, 0.5, 1.0, 1.5, 2.0, 2.5]

plt.title('group 1, Dose respons curve 2 hours after irradiation')
plt.ylabel('pixel value')
plt.xlabel('dose')
plt.plot(dose, g1)
plt.savefig('g1')
plt.show()

plt.title('group 2, Time curve after 2Gy irradiation')
plt.ylabel('pixel value')
plt.xlabel('hours')
plt.plot(dose, g2)
plt.savefig('g2')
plt.show()

plt.title('group 3')
plt.ylabel('pixel value, Time curve after 2Gy irradiation')
plt.xlabel('hours')
plt.plot(dose, g3)
plt.savefig('g3')
plt.show()





