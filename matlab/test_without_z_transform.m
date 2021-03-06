% PTC3456 - Processamento de Sinais Biológicos 
% Aula 3

n = -10:10;

%% Exercicio 1
% h[n] = delta[n-2] - 2 delta[n-3] + delta[n-4] - delta[n-6]
% x[n] = delta[n+1] + 2 delta[n-1] - delta[n-2]

x = zeros(size(n));
x(n == -1) = 1;
x(n == 1) = 2;
x(n == 2) = -1;

h = zeros(size(n));
h(n == 2) = 1;
h(n == 3) = -2;
h(n == 4) = 1;
h(n == 6) = -1;

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

%% Exercicio 2
% H(z) =   4 z^(-5
%        ------------
%        1 + z^(-1)/5
% x[n] = -2 (-1/5)^n u[-n-1]

n = -100:100;

x = zeros(size(n));
x(n <= -1) = 1;
x = - 2 .* (-1/5).^n .* x;

h = zeros(size(n));
h(n <= 4) = 1;
h = - 4 .* (-1/5).^(n-5) .* h;

y = conv(x, h, 'same');
y_calc = zeros(size(n));
y_calc(n <= 4) = 1;
y_calc = - 8 .* (n-4) .* (-1/5).^(n-5) .* y_calc;

figure(2)

subplot(2,2,1)
stem(n, x, 'filled')
title('x[n]')
xlabel('n')
ylabel('x')
legend('x = -2 (-1/5)^n u[-n-1]')
xlim([-10, 10])
grid on

subplot(2,2,2)
stem(n, h, 'filled')
title('h[n]')
xlabel('n')
ylabel('h')
legend('-4 (-1/5)^(n-5) u[-n+4]')
xlim([-10, 10])
grid on

subplot(2,2,3)
stem(n, y, 'filled')
hold on
stem(n, y_calc, 'filled')
stem(n, abs(y - y_calc), 'filled')
hold off
title('y[n]')
xlabel('n')
ylabel('y')
legend('(x * h)[n]', '-8(n-4)(-1/5)^{n-5}u[-n+4]', '|(x * h)[n] + 8(n-4)(-1/5)^{n-5}u[-n+4]|')
xlim([-10, 10])
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
xlim([-10, 10])
grid on

