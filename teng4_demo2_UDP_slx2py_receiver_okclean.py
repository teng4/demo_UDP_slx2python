#
#
# UDP data Simulink to python -- Demo (ok! verified!)
# ---------------------------------------------------------------------
# Description: 
# UDP Receive data from Simulink.
# Here python code receive UDP data from Simulink, and do real-time plot.
# ---------------------------------------------------------------------
# teng4 modified, 2023-02-23, Thursday. Remain Problem: The py receiver sampling time (>0.08s) is not accurate and cannot be controlled.
# teng4 created, 2023-02-22, Wed.
# ---------------------------------------------------------------------
# (0) using VScode to run this python file. (suggested)
# (1) using conda env "test2" (or create a new env and install the required pkgs.)
# (2) conda env list
# (3) conda deactivate
# (4) conda activate test2
# (5) conda list  #check all installed pkgs in the current env.
#
#


print('hello, world')

from datetime import datetime 
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


## ------------------------------------------
## below code come from live data plot
## ------------------------------------------

import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
from drawnow import drawnow

# time
start_time = time.time()
end_time = time.time()
elapsed_time =  end_time - start_time
print("Used time: {:.4f}".format(end_time - start_time))


def makeFig():
    if len(xList)<105:
        plt.plot(xList,y2List,'ro-', label='line 1', linewidth=1) #
        plt.plot(xList,y3List,'b.:', label='line 2', linewidth=2) #s,square marker; .,point marker; o, circle marker
        plt.plot(xList,y4List,'gs--', label='line 3', linewidth=2, markersize=4) #color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12
    else:
        plt.plot(xList[-101:-1:5],y2List[-101:-1:5],'ro-', label='line 1', linewidth=1) #x[low:high:stride]  # [x[low], x[low+stride], ..., x[high-1]]
        plt.plot(xList[-101:-1:5],y3List[-101:-1:5],'b.:', label='line 2', linewidth=2) #s,square marker; .,point marker; o, circle marker
        plt.plot(xList[-101:-1:5],y4List[-101:-1:5],'gs--', label='line 3', linewidth=2, markersize=4) #color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12


fig = plt.figure() # make a figure

# setting title
plt.title("teng4 UDP live data ploting...", fontsize=16)
# setting x-axis label and y-axis label
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

xList=list()
yList=list()
count1 = 0
x1List=list()
y1List=list()
y2List=list()
y3List=list()
y4List=list()


## ------------------------------------------
## below code for UDP setup and receive data.
## ------------------------------------------

import keyboard
import socket
import numpy as np
import struct

UDP_IP = "192.168.1.102" #teng4 note, local IP address
UDP_PORT = 25000 #teng4 note, local port number

sock = socket.socket(socket.AF_INET, # Internet
                   socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# time
start_time2 = time.time() #used to calculate the while-loop time cost.
#
print("Note: you can press button 'a' to interrupt the program.")
while True:
    end_time2 = time.time()
    elapsed_time2 =  end_time2 - start_time2
    print("while-loop used time2: {:.4f}".format(end_time2 - start_time2))

    if keyboard.is_pressed("a"): #teng4 note, always listen to keyboard input.
        print("You pressed 'a'.")
        # Close socket
        sock.close()
        print("UDP sock closed.")
        break

    #teng4 note, the UDP in Simulink is sending a 4-by-1 data vector.
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes, max 1024/8=128chars.

    data_block = data
    output_x1 = struct.unpack_from('<d', bytearray(data_block[0:8])) #x[a:b] #[x[a], x[a+1],..., x[b-1]]
    output_x2 = struct.unpack_from('<d', bytearray(data_block[8:16])) #x[a:b] #[x[a], x[a+1],..., x[b-1]]
    output_x3 = struct.unpack_from('<d', bytearray(data_block[16:24])) #x[a:b] #[x[a], x[a+1],..., x[b-1]]
    output_x4 = struct.unpack_from('<d', bytearray(data_block[24:32])) #x[a:b] #[x[a], x[a+1],..., x[b-1]]

    #print(len(data_block))
    print(output_x1)
    #print(output_a2)
    #print(output_a3)
    #print(output_a4)
    #print(type(output_a4))
    output_xall = output_x1 + output_x2 + output_x3 + output_x4
    #print(output_all)
    arrconv_tuple = np.array(output_xall)
    #print(type(arrconv_tuple))
    #print(arrconv_tuple)

    count1 = count1 +1
    
    #plt.pause()
    #plt.pause(0.01)   #teng4test, will make the while-loop cost about 0.08s.
    #plt.pause(0.0001)  #teng4test, will make the while-loop cost about 0.08s.
    #IF NO PAUSE, teng4test, will make the while-loop cost about 0.06-0.07s.

    end_time = time.time()
    elapsed_time =  end_time - start_time

    xList.append(count1)
    yList.append(arrconv_tuple[2]) #arr[0],arr[1],arr[2],arr[3]
    y1List.append(arrconv_tuple[0]) #arr[0],arr[1],arr[2],arr[3]
    y2List.append(arrconv_tuple[1]) #arr[0],arr[1],arr[2],arr[3]
    y3List.append(arrconv_tuple[2]) #arr[0],arr[1],arr[2],arr[3]
    y4List.append(arrconv_tuple[3]) #arr[0],arr[1],arr[2],arr[3]

    drawnow(makeFig)
    #makeFig()      The drawnow(makeFig) command can be replaced
    #plt.draw()     with makeFig(); plt.draw()

print('END-2023.02.23')