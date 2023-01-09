# arc 12 30 2020 compute inner product between two vectors 

# read the x,y,z coordinates of vector 1
# note that we read all 3 coordinates as a string, and then 
# use the split function to separate them by the ','
# the split function is a very useful function for string manipulation
# TODO - error handling
v1=input("enter x1,y1,z1 :: ").split(',')
v2=input("enter x2,y2,z2 :: ").split(',')

# what is the data type of v1 after line 7 executes?
# convert v1 to a list of floats
v1=list(map(float,v1))
v2=list(map(float,v2))
# print(v1) # printf debug line

# repeat for v2

# compute inner product
innerProduct = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
print('inner product of v1='+str(v1)+', v2='+str(v2)+' is '+str(innerProduct))

# print v1,v2 and inner product using a 1 line formatted print statement
