
%% 1D Rectangular Amplitude Grating
clc
close all
clear all

%% Defining Grating Parameters
N = 500; % Define Matrix size
A = zeros(1,N); % Define a row Matrix by assigning 0 to all pixels
P = 100; % Define the period of the grating
FF = 0.5; % Define fill factor

%% Constructing the Grating
% V.1

for q = 1:N
    if rem(q,P) < P*FF %Use remainder function ‘rem’ to construct
                      %the grating
       A(1,q) = 1;
    end
end
A = repmat(A,N,1); %replicate the row to create a 2D grating

% V.2 (Alternative code for constructing the grating)
% O = ones(N,FF*P);
% Z = zeros(N, P-FF*P);
% unit = [O Z];
% A = repmat(unit,1,N/P); % Replicate to create a 1D grating

figure
plot(A(1,:));

figure
imshow(mat2gray(A));

%% Observing the grating output in the far field
E = fftshift(fft2(A)); % fftshift is used to re-order the terms in their natural order
IN = (abs(E)/(N*N)).*(abs(E)/(N*N)); % Calculating intensity

% figure;
% colormap(gray); %colormap(gray) is used to display grayscale
% imagesc(A);% imagesc is used to display a high constrast image

figure;
subplot(2,1,1)
colormap(gray);
imagesc(real(E));
subplot(2,1,2)
plot(real(E(round(N/2) + 1,:)));

figure;
subplot(2,1,1)
colormap(gray);
imagesc(angle(E));
subplot(2,1,2)
plot(angle(E(round(N/2) + 1,:)));

figure;
subplot(2,1,1)
colormap(gray);
imagesc(IN);
subplot(2,1,2)
plot(IN(round(N/2) + 1,:));