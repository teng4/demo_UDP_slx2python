% #
% # UDP data send from Simulink to python -- Demo (ok! verified!)
% # ---------------------------------------------------------------------
% # Description:
% # UDP send data from Simulink to python code.
% # ---------------------------------------------------------------------
% # teng4 modified, 2023-02-23, Thursday.
% # teng4 created, 2023-02-22, Wed.
% #

clc;
clear;
close all;

% % UDP send data to python code (ok! teng4 verified 2023-02-23.)
udps = dsp.UDPSender('RemoteIPAddress','192.168.1.102','RemoteIPPort',25000);

bytesSent = 0;
dataLength = 128;

% send data in a for-loop, 
% and send a 4-by-1 double vector in each loop.
for k = 1:1e5 
    x1 = cos(10*k/100); %teng4 modified, k/1000 is the real time with Ts=0.001s.
    x2 = cos(20*k/100); %teng4 modified, k/1000 is the real time with Ts=0.001s.
    x3 = cos(40*k/100); %teng4 modified, k/1000 is the real time with Ts=0.001s.
    %X = [k,2.2,3.3,4.4]; %teng4 added, make the sending data X to be 4-by-1 vector for test
    dataX = [k,x1,x2,x3]; %teng4 added, make the sending data X to be 4-by-1 vector for test
    bytesSent = bytesSent + length(dataX); %calculate the amount of the sended data.
    udps(dataX); %UDP send data.
    disp(dataX); %display the sending data in the Command Window.
    
    pause(0.01) %in seconds
end

% % Release the UDP objects.
release(udps);
%release(udpr); %udpr no used.

% %
% Some of the packets sent can be lost during transmission
% due to the lossy nature of the UDP protocol.
% To check for loss, compare the bytes sent to the bytes received.
fprintf('Bytes sent:     %d\n', bytesSent);
%fprintf('Bytes received: %d\n', bytesReceived); %udpr no used.



disp('End of file, 2023.02.23.')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%





