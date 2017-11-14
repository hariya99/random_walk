import matplotlib.pyplot as plt
from random_walk import RandomWalk

#make a random walk and plot the points
rw = RandomWalk()
rw.fill_walk()

#plt.scatter(rw.x_values, rw.y_values, s=15)

#creating a colorful scatter
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

#emphasize the first and last point
plt.scatter(0,0,c='green', edgecolor='none',s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

#use the below code if you want to remove axes
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)

#use the below code to resize the window 
#plt.figure(figsize=(10,6))

#use the below code to set pixels for graph 
#plt.figure(dpi=128, figsize=(10,6))

#show the plot
plt.show()
