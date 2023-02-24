# demo_UDP_slx2python
This demo is to (1) send UDP data from Matlab/Simulink and (2) receive the UDP data by python code and do live data plot.


# Description
(1) Matlab .m code for UDP sender (sending a 4-by-1 double array).

(2) Simulink .slx model for UDP sender (sending a 4-by-1 double array).

(3) Simulink .slx model for UDP sender (in DESKTOP REAL-TIME mode) (sending a 4-by-1 double array).

(4) python .py code for UDP receiver (receiving a 4-by-1 double array).

(5) Note that the 4-by-1 double array is \[time, sine1, sine2, sine3\].


# Platform
Matlab/SIMULINK: R2020a 64bit;

Visual Studio Code (VScode), for running python code;


# Instruction
In order to run the python code in VScode, you need first to do the following,

(1)
$\textcolor{gray}{\text{\tt conda create -n test2 python=3.7}}$
$\textcolor{green}{\text{ (Note: create a new env named "test2" (or you name it))}}$.

(2)
$\textcolor{gray}{\text{\tt conda activate test2}}$
$\textcolor{green}{\text{(Note: activate the env "test2")}}$.

(3)
$\textcolor{gray}{\text{\tt pip install matplotlib}}$
$\textcolor{green}{\text{(Note: using pip to install all required packages when you run the .py file in VScode)}}$.

(4)
Run the Matlab/Simulink and VScode on the same pc, and run Matlab/Simulink the first, and VScode the second.


# Example Results
(1) Demo live plot result screenshot.

![teng4_demo2_example_screenshot_20230223_171019](https://github.com/teng4/demo_UDP_slx2python/blob/main/teng4_demo2_example_screenshot_20230223_171019.png)


# (-The End-)


$\textcolor{green}{\text{ Uploaded 2023-02-23. }}$
