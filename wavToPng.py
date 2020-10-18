import scipy.io.wavfile
import math
from PIL import Image
import averageAmplitude

def sigmoid(x):
    if x < -700:
        x = -700
 
    ans = 1/(1 + math.e ** (-x))
    
    return ans
        
       




out = scipy.io.wavfile.read("StarWars60.wav", mmap=False)
a,b = out
print(out)

list1 = b.tolist()
print("len")
print(len(list1))
for i in range(len(list1)):
    list1[i] = int(255*sigmoid(list1[i]))
 
#print(list1[:100])
img = Image.new('RGB',(300,300))
pixels = img.load()
count = 0
for i in range(img.size[0]):
    print(i)
    for j in range(img.size[1]):
        pixels[i,j] = (list1[count],list1[count+1],list1[count+2])
        count += 3
print("done")
img.show()

averageAmplitude.averageAmplitude(b)