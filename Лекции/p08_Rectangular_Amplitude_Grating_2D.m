%% 2D Rectangular Amplitude grating
clc
close all
clear all

%% Defining Grating Parameters
N = 500; %Define Matrix size
A = zeros(N,N); %Define a Matrix by assigning 0 to all pixels
Px = 100; Py = 100; %Define the period of the grating
FFx = 0.5; FFy = 0.5; %Define fill factor

%% Constructing the Grating

% V.1 
O1 = ones(N,FFx*Px);
Z1 = zeros(N, Px - FFy*Px);
unit1 = [O1 Z1];
A1 = repmat(unit1, 1, N./Px); % Replicate to create a 1D grating

figure
imshow(mat2gray(A1));

O2 = ones(FFy.*Py, N);
Z2 = zeros(Py - FFy.*Py, N);
unit2 = [O2; Z2];
A2 = repmat(unit2,N/Py,1);

figure
imshow(mat2gray(A2));

A = A1.*A2;

% V.2 (Alternative code for constructing the grating)

% for p = 1:N
%     for q = 1:N
%         if rem(q,Px)<Px*FFx && rem(p,Py)>Py*FFy
%            A(p,q) = 1;
%         end
%     end
% end

%% Observing the grating output in the far field
E = fftshift(fft2(A)); % fftshift is used to re-order the terms in their natural order
IN = (abs(E)/(N*N)).*(abs(E)/(N*N)); % Calculating intensity

figure;
colormap(gray); %colormap(gray) is used to display grayscale
imagesc(A);% imagesc is used to display a high constrast image

figure;
colormap(gray);
imagesc(IN);

figure
plot(IN(round(N/2) + 1,:));