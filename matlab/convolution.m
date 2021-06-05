%% PTC3456 - Processamento de Sinais Biológicos 
% Aula 2

n = -10:10;

x = zeros(size(n));
x(n == 2) = 1;
x(n == 3) = 2;
x(n == 4) = -2;
x(n == 5) = -1;

h = zeros(size(n));
h(n == -1) = 5;
h(n == 1) = 2;
h(n == 2) = 6;

y = conv(x, h, 'same');

figure(1)

subplot(2,2,1)
stem(n, x, 'filled')
title('x[n]')
xlabel('n')
ylabel('x')
legend('\delta[n-2]+2\delta[n-3]-2\delta[n-4]-\delta[n-5]')
grid on

subplot(2,2,2)
stem(n, h, 'filled')
title('h[n]')
xlabel('n')
ylabel('h')
legend('5\delta[n+1]+2\delta[n-1]+6\delta[n-2]')
grid on

subplot(2,2,3)
stem(n, y, 'filled')
title('y[n]')
xlabel('n')
ylabel('y')
legend('(x * h)[n]')
grid on

subplot(2,2,4)
stem(n, x, 'filled')
hold on
stem(n, h, 'filled')
stem(n, y, 'filled')
hold off
title('x[n], h[n] and y[n]')
xlabel('n')
ylabel('signals')
legend('x[n]', 'h[n]', 'y[n]')
grid on
