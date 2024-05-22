
%% Checkerboard Amplitude grating
clc
close all
clear all

%% Defining Grating Parameters
N = 500; %Define Matrix size
A1 = zeros(N,N); %Define Matrices by assigning 0 to all pixels
A2 = zeros (N,N);
A = zeros (N,N);
Px = 100; %Define the periods of the gratings
Py = 100;
FFx = 0.5; %Define fill factors
FFy = 0.5;

% Constructing the grating

for p = 1:N
    for q = 1:N
        if rem(q,Px) < Px.*FFx
           A1(p,q) = 1;
        end
        if rem(p,Py) < Py.*FFy
           A2(p,q) = 1;
        end
    end
end
A = xor(A1,A2); % XOR operation between A1 and A2

%% Creation of a phase grating
B = exp(1i*pi.*A);

figure
imshow(angle(B));

%% Observing the grating output in the far field
E = fftshift(fft2(B)); % fftshift is used to re-order the terms in their natural order
IN = (abs(E)/(N*N)).*(abs(E)/(N*N)); % Calculating intensity


figure;
colormap(gray);
imagesc(IN);
