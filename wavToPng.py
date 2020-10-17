import scipy.io.wavfile
import math
from PIL import Image

def sigmoid(x):
   
    if x < -700:
        x = -700
 
    ans = 1/(1 + math.e ** (-x))
    
    return ans
        
       




out = scipy.io.wavfile.read("rickroll.wav", mmap=False)
a,b = out
print(out)

list1 = b.tolist()
list2 = []

if isinstance(list1[0],list):
    for i in range(len(list1)):
        total = 0
        for j in range(len(list1[i])):
            total += list1[i][j]
        list2.append(total/len(list1[i]))
        
if isinstance(list1[0],list):
    list1 = list2
    


for i in range(len(list1)):
    list1[i] = int(255*sigmoid(list1[i]))
 

img = Image.new('RGB',(300,300))
pixels = img.load()
count = 0

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i,j] = (list1[count],list1[count+1],list1[count+2])
        count += 3
print("done")
img.show()
