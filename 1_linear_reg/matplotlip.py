import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10]) #this assumes x-points (1,2,3,4, ... etc)
plt.plot(ypoints, marker = 'd',linestyle="dotted", c="k") ; plt.show()

""" We can also use a shortcut formate in order to detect the marker shape and color"""
plt.plot(ypoints, 'd-.r'); plt.show() #1 marker shape, 2 the line style, 3 color


"""
Marker face color (mfc)= the color of the marker (the face color)
marker edge colr (mec) = the color of the edge surrounding the marker
marker size (ms)= the size of marker
linestyle
line width (linewidth)= the width of line
"""
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'hotpink', mec='b',linestyle=":",linewidth='20')
plt.show()

""" Drawing Multiple lines """
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1); plt.plot(y2); plt.show()

# we are here plotted each line separately, hence it asumes that x=(1,2,3,4, ... etc)
#you may notice that the previous and the following exmple is the same
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2); plt.show()

""" Tilte Creation and axis labeling"""
ex = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
whay = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font_label={'family':'Times New Roman', 'color':'darkred','size':20}
font_title={'family':'Calibri Light (Headings)','color':'black','size':30}

plt.plot(ex,whay) 

plt.title("sports data",fontdict=font_title,loc='center')
#the locattion attribute (loc) for title is only [center,right,left]

plt.xlabel("Average Pulse",fontdict=(font_label),loc='right')
#the locattion attribute (loc) for X-axis is only [right,center,left]

plt.ylabel('Calorine Burnage',fontdict=(font_label),loc='bottom')
#the locattion attribute (loc) for Y-axis is only [top,center,bottom]

plt.grid(axis='both',color = 'green', linestyle = '--', linewidth = 1) 
#the attribute of axis= 'x' or 'y' or 'both'
plt.show()
"""note that xlabel and ylabel is a fixed attributes 
even x-axis and y-axis has different names"""


""" we use subplot in order to plot more than one plot"""
#plot 1:
x = np.array([0, 1, 2, 3]); y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1); plt.title('one'); plt.plot(x,y) #plot in the first graph
"""
1 is the number of raw (so I have only one raw)
2- is the number of columns (so I have two columns)
3- where to plot this plot (the position);the first, the second or the tird column
"""
#plot 2:
x = np.array([0, 1, 2, 3]); y = np.array([10, 20, 30, 40])
plt.subplot(2,3,2); plt.title('two'); plt.plot(x,y) #plot in the second graph

#plot 3 
x = np.array([0, 1, 2, 3]); y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3); plt.title('three'); plt.plot(x,y)  #plot in the third graph

#plot4
x = np.array([0, 1, 2, 3]); y = np.array([10, 20, 30, 40])
plt.subplot(2,3,4); plt.title('four'); plt.plot(x,y) #plot in the fourth graph

#plot 5
x = np.array([0, 1, 2, 3]); y = np.array([3, 8, 1, 10])
plt.subplot(2,3,5); plt.title('five'); plt.plot(x,y)  #plot in the fifth graph

#plot 6 
x = np.array([0, 1, 2, 3]); y = np.array([10, 20, 30, 40])
plt.subplot(2,3,6); plt.title('six'); plt.plot(x,y) #plot in the sixth graph
plt.suptitle("the six graphs"); plt.show() 


""" Scatter Plot """
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y,)
#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y,)

plt.show()
"""  some attributes to the scatter display:
1-  cmap= range of colors that varies according to the value and is attached by 
22- column-bar which has the syntax plt.colorbar() 
3- s=size of the point (2,4,7, etc)--> could be variable
4- alpha is the transparency, alpha = 0.2, 0.5, 0.8 """

x = np.random.randint(100, size=(50))
y = np.random.randint(100, size=(50))
colors = np.random.randint(100, size=(50))
sizes = 10 * np.random.randint(100, size=(50))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar(); plt.show()


""" Bar Grpahs """
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y); plt.show() #plt.barh makes the bar chart horizontal
""" some syntax: 
1- bar width(width=0.1,0.4,0.8) 
note that if we use horziontal bar,the this attriburte would be hight= instead of width """


""" Histograms """
"""
For simplicity we use NumPy to randomly generate an array with 250 values, 
where the values will concentrate around 170, and the standard deviation is 10
"""
x=np.random.normal(170,10,250)
plt.hist(x); plt.show
    
    
""" Bar Chart """
    
y = np.array([7, 8, 3, 50])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels=mylabels); plt.show()

""" Some attributes regarding the pie chart : 
1- labels = [list of the names of my values]
2- startangle = the angle at which I start the proportion
3- explode = [list for the proportions you want to take it out]
4- shadow = True or False
5- colors = [make a list of colors to the different proportions]
5- plt.legend() is to make a legend for the various proportions
"""

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0.5, 2, 0.7]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y,explode=myexplode, labels=mylabels, startangle=90, colors=mycolors, shadow=True, )
plt.legend(title="Fruits"); plt.show() 