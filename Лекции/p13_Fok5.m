%% ��������� � ������
clc
close
clear

% ������� ������
lambda = 0.6328e-3; % ����� �����, [��]
k = (2*pi)/lambda;

N = 512;
f = 750; % [��]
a = 25.6/2; % ������ ����������, [��]
r0 = 0.2; % ������ ������ �����������, [��]

% ��������� �������������
T = a/N; % �� - ��� 

Tr = a; %������ ��������� ������������

num = 1/(2*T); % ���������� �������
dnu = 1/Tr; % ��� ������������� �� �������

% ����� �������������

u = -Tr/2:T:Tr/2 - T; % �� ���������� � � ��-�� ���
v = -Tr/2:T:Tr/2 - T; % �� ���������� Y � ��-�� ���

[U,V] = meshgrid(u,v);
[theta,r] = cart2pol(u,v);


%% ������ ����������

for i = 1:N
    Phi(i) = -k.*sqrt(f^2 + (r(i) - r0).^2);
end

%% ��������� ���������
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