%% 1D Sin Amplitude grating
clc
clear
close all

%% Defining Grating Parameters
N = 500; % Define Matrix size
A = ones(1,N); % Define a Matrix by assigning 1 to all pixels
P = 500; % Define the period of the grating

%% Constructing the Grating

for q = 1:N
    A(1,q) = (1 + sin(rem(q,P)*(2*pi)/P))/2;
end

A = repmat(A,N,1); %replicate the row to create a 2D grating
%Observing the grating output in the far-field

figure;
plot(A(round(N/2),:));

%% Observing the grating output in the far field
E = fftshift(fft2(A)); % fftshift is used to re-order the terms in their natural order
IN = (abs(E)/(N*N)).*(abs(E)/(N*N)); % Calculating intensity

figure
colormap(gray);
imagesc(IN)

figure; 
plot(1:500, IN(251,:));