%% Фокусатор в кольцо
clc
close
clear

% Вводные данные
lambda = 0.6328e-3; % Длина волны, [мм]
k = (2*pi)/lambda;

N = 512;
f = 750; % [мм]
a = 25.6/2; % радиус фокусатора, [мм]
r0 = 0.2; % радиус кольца фокусировки, [мм]

% Параметры дискретизации
T = a/N; % мм - шаг 

Tr = a; %Ширина интервала рассмотрения

num = 1/(2*T); % Полуширина спектра
dnu = 1/Tr; % Шаг дискретизации по частоте

% Сетка дискретизации

u = -Tr/2:T:Tr/2 - T; % По координате Х в пл-ти ДОЭ
v = -Tr/2:T:Tr/2 - T; % По координате Y в пл-ти ДОЭ

[U,V] = meshgrid(u,v);
[theta,r] = cart2pol(u,v);


%% Синтез фокусатора

for i = 1:N
    Phi(i) = -k.*sqrt(f^2 + (r(i) - r0).^2);
end

%% Результат дифракции
% figure;
% mesh(Phi);

Phi2 = exp(1i*pi*Phi);
E = abs(fftshift(fft2(fftshift(Phi2))));

mincgh = min(min(E)); %normalization
E = E - mincgh;
mcgh = max(max(E));
E = E ./mcgh;

figure;
plot(E)