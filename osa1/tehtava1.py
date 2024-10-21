import numpy as np

teht_1 = np.array([2.493, 0.911])
print("Tehtävä 1:")
for i in teht_1:
    print(str(np.degrees(i)) + "°")


teht_2 = np.array([137.7, 62.3])

print("\nTehtävä 2:")
for i in teht_2:
    print(str(np.radians(i)) +  " rad")


teht_3 = np.array([30,45,60,90,120,135,150,180,270,360])

print("\nTehtävä 3:")
for i in teht_3:
    print(str(np.radians(i)) +  " rad")
