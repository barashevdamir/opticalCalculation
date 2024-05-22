
%% 1D Rectangular Phase Grating
clc
% close all
clear all

%% Defining Grating Parameters
N = 500; % Define Matrix size
A = zeros(1,N); % Define a row Matrix by assigning 0 to all pixels
P = 50; % Define the period of the grating
FF = 0.75; % Define fill factor

%% Constructing the Grating
% V.1
% for q = 1:N;
%     if rem(q,P) < P*FF; %Use remainder function ‘rem’ to construct
%                       %the grating
%        A(1,q) = 1;
%     end
% end
%     A = repmat(A,N,1); %replicate the row to create a 2D grating

% V.2 (Alternative code for constructing the grating)
O = ones(N,round(FF*P));
Z = zeros(N, P-round(FF*P));
unit = [O Z];
A = repmat(unit,1,N/P); % Replicate to create a 1D grating

figure
plot(A(1,:));

%% Creation of a phase grating
B = exp(1i.*A');

figure;
plot(angle(B(1,:)));

figure;
imshow(mat2gray(angle(B)));

%% Observing the grating output in the far field
E = fftshift(fft(B)); % fftshift is used to re-order the terms in their natural order
IN = (abs(E)/(N)).*(abs(E)/(N)); % Calculating intensity

figure;
colormap(gray); %colormap(gray) is used to display grayscale
imagesc(A);% imagesc is used to display a high constrast image

figure;
colormap(gray);
imagesc(IN);

figure
plot(IN(:,round(N/2) + 1)); % round(N/2) + 