
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

% V.1
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
A = double(xor(A1,A2)); % XOR operation between A1 and A2

A = rot90(A,1);

figure
imshow(mat2gray(A));

% V.2 (Alternative code for constructing the grating)
% O = ones(FFy.*Py, FFx.*Px);
% Z = ones(FFy.*Py, Px - FFx.*Px);
% O1 = ones(FFy.*Py, Px - FFx.*Px);
% Z1 = ones(FFy.*Py, FFx.*Px);
% unit = [Z O; O1 Z1];
% s = size(unit);
% 
% A = repmat(unit,N/s(1),N/s(2));

%% Observing the grating output in the far field
E = fftshift(fft2(A)); % fftshift is used to re-order the terms in their natural order
IN = (abs(E)/(N*N)).*(abs(E)/(N*N)); % Calculating intensity

figure;
colormap(gray);
imagesc(IN);

figure
plot(IN(round(N/2) + 1,:));