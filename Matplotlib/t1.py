import matplotlib.pyplot as plt
import numpy as np
x =np.array([1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]) 
y = np.array([94, 88, 82, 75, 69, 63, 57, 50, 44, 38, 32, 25, 19, 13, 7, 0,13, 25, 38, 50, 63, 75, 88, 100])
plt.subplot(2, 2, 1)
plt.plot(x,y)
plt.title("Chonapat")
plt.xlabel("TIMES")
plt.ylabel("POWER")

x = np.array([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,1, 2, 3, 4, 5, 6, 7])
y = np.array([95, 89, 84, 78, 73, 67, 62, 56, 50, 45, 39, 34, 28, 23, 17, 12, 6, 0,17, 34, 50, 67, 84, 101])
plt.subplot(2, 2, 2)
plt.plot(x,y)
plt.title("Kong")
plt.xlabel("TIMES")
plt.ylabel("POWER")

x = np.array([1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
y = np.array([94, 88, 82, 75, 69, 63, 57, 50, 44, 38, 32, 25, 19, 13, 7, 0,13, 25, 38, 50, 63, 75, 88, 100])

plt.subplot(2, 2, 3)
plt.plot(x,y)
plt.title("Pai")
plt.ylabel("Times")

x = np.array([1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
y = np.array([95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0,25, 50, 75, 100])

plt.subplot(2, 2, 4)
plt.plot(x,y)
plt.title("Heart")
plt.ylabel("Times")

plt.suptitle("Sleep")

plt.show()