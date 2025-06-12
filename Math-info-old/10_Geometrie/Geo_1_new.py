# Z = (z² + i)/(z - i)
# determiner le lieu des points M d'affixe z
# - Lorque Im(Z) = 0
# - Lorque Re(Z) = 0

import numpy as np
import matplotlib.pyplot as plt

tolerance = 0.005
val_min = -4
val_max = 4
nb_pts = 2000

variation_re = np.linspace(-val_max, val_max, nb_pts)
variation_im = np.linspace(-val_max, val_max, nb_pts)

x_when_im_zero = []
y_when_im_zero = []

x_when_re_zero = []
y_when_re_zero = []

for x in variation_re: # x = partie reelle de z:
    for y in variation_im: # y = partie imaginaire de z:
        
        z = x + y * 1j # z minuscule
        Z = (z**2 + 1j) / (z - 1j) # Z majuscule
        
        if abs(Z.imag) <= tolerance: # Si l'imaginaire de Z est proche de 0
            x_when_im_zero.append(x)
            y_when_im_zero.append(y)
        
        if abs(Z.real) <= tolerance: # Si le reel de Z est proche de 0
            x_when_re_zero.append(x)
            y_when_re_zero.append(y)


plt.scatter(x_when_im_zero, y_when_im_zero, color='r', s=1, label='Im(Z) = 0')
plt.scatter(x_when_re_zero, y_when_re_zero, color='b', s=1, label='Re(Z) = 0')
plt.legend()
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.title('Lieux des points M d\'affixe z')
plt.axis('equal')
plt.show()
