import scipy.io.wavfile
import math
from PIL import Image

def sigmoid(x): # condense variables down to 0<x<1   
    if x < -700:
        x = -700
 
    ans = 1/(1 + math.e ** (-x))
    
    return ans
        
       




out = scipy.io.wavfile.read("rickroll.wav", mmap=False) # read file
a,b = out
print(out)

list1 = b.tolist()
print(list1)
list2 = []

if isinstance(list1[0],list): # if 2d array average elements in subarrays to make 1d array
    for i in range(len(list1)):
        total = 0
        for j in range(len(list1[i])):
            total += list1[i][j]
        list2.append(total/len(list1[i]))
        
if isinstance(list1[0],list):
    list1 = list2
    


for i in range(len(list1)):
    list1[i] = int(255*sigmoid(list1[i])) # compressing array down to 0<x255
 

img = Image.new('RGB',(300,300)) # image creation -- 300,300 is arbitrary
pixels = img.load()
count = 0

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i,j] = (list1[count],list1[count+1],list1[count+2]) # setting rgb values equal to values from list1
        count += 3
print("done")
img.show()
