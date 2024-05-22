% Multifunctional DOE – Blazed circular grating and blazed 1D grating clear
%
%
clc
clear
close all

% Define grating parameters
N = 500; % Define Matrix size
Pr = 20;
P = 10;

% Blazed axicon and grating construction
x = 1:N; % Sampling
y = 1:N;
[X,Y] = meshgrid(x,y); % Сетка

%% 
r = sqrt((X-N/2).*(X-N/2) + (Y-N/2).*(Y-N/2));
figure;
mesh(r);

P1 = rem(r,Pr); % Construction of blazed axicon
A1 = (P1/Pr)*2*pi;
figure;
mesh(A1);

P2 = rem(X,P); % Construction of blazed 1D grating on X
A2 = (P2/P)*2*pi;
figure;
mesh(A2);

figure
plot(A2(1,:));

P3 = rem(Y,P); % Construction of blazed 1D grating on Y
A3 = (P3/P)*2*pi;

A = rem(A2 + A3,2*pi); % Modulo-2pi phase addition of the two phase profiles 
figure(4);
mesh(A);

figure
imshow(mat2gray(A));

B = exp(1i*A);
% B(r > 150)=0;
% figure(5);
% mesh(real(B));

figure(6);
subplot(1,2,1);
imshow(mat2gray(real(B)));
title('Real part of Blazed axicon');
subplot(1,2,2);
imshow(mat2gray(angle(B)));
title('Phase part of Blazed axicon');

% Reconst
% pic1 = ifftshift(B);
reconst = fft2(B);
reconst = fftshift(reconst);

figure(7);
subplot(1,2,1);
imshow(mat2gray(real(reconst)));
title('Real part of reconst Blazed axicon');
subplot(1,2,2);
imshow(mat2gray(angle(reconst)));
title('Phase part of reconst Blazed axicon');

figure
plot(max(real(reconst)));

IN = (abs(reconst)/(N*N)).*(abs(reconst)/(N*N)); % Calculating intensity

figure;
colormap(gray);
imagesc(IN);
figure
plot(max(IN));
