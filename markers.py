import matplotlib.pyplot as plt
import numpy as np

'''
Marker	Description
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
'''

x = np.array([0, 2 ,3])   
y = np.array([0 , 3 ,2])  

# plt.plot(x,y , marker = 'o')
# plt.plot(x,y , marker = '1')
# plt.plot(x,y , marker = 'd')
# plt.plot(x,y , marker = 'p')
# plt.plot(x,y , marker = '+')
# plt.plot(x,y , marker = 's')
# plt.show()


'''
Format Strings fmt
You can also use the shortcut string notation parameter to specify the marker.

This parameter is also called fmt, and is written with this syntax:

marker|line|color
'''

x1 = np.array([4,2,4])
y1 = np.array([2,4,2])

# plt.plot(x1,y1 , "o-.k")
# plt.show()

# plt.plot(x1,y1 , "o-b")
# plt.show()

'''
Line Reference
Line Syntax	Description
'-'	    Solid line	
':'	    Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted lin
'''

'''
olor Reference
Color Syntax	Description
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
'''

'''
Marker Size
You can use 
the keyword argument markersize or the shorter version, ms to set the size of the markers:
'''

# x2 = np.array([3,1,0])
# y2 = np.array([3,-1,3])

# plt.plot(x2,y2 , marker = 'o', ms = 10)
# plt.show()


'''
you can use the keyword 
argument markerfacecolor or the shorter mfc to set the color
inside the edge of the markers:
'''

x2 = np.array([3,1,0])
y2 = np.array([3,-1,3])

plt.plot(x2,y2 , marker = 'o' , ms = 8 ,mec  = 'r', mfc = 'r' )
plt.show()
