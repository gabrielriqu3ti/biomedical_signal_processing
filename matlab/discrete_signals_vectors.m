% PTC3456 - Processamento de Sinais Biológicos 
% Aula 1

n = -10:10;

degrauE = zeros(size(n));
degrauE(n<=6) = 1;

degrauD = zeros(size(n));
degrauD(n>=7) = 1;

aux_1 = zeros(size(n));
aux_1(n<=-7) = 1;
aux_2 = zeros(size(n));
aux_2(n<=-6) = 1;
x1 = aux_1 - aux_2;

x2 = ones(size(n));
aux_2 = zeros(size(n));
aux_2(n<=-6) = 1;
x2 = x2 - aux_2;

x3 = zeros(size(n));
x3(n<=-6) = 1;
x3 = x3 .* (1/5) .* (-1/3).^(n + 6);

x4 = zeros(size(n));
x4(n<=6) = 1;
x4 = x4 .* (-15) .* (-1/3).^(n - 6);

figure(1)

subplot(211)
stem(n, degrauE, 'filled')
title('degrauE[n]')
xlabel('n')
ylabel('degrauE')
legend('u(-n+6)')

subplot(212)
stem(n, degrauD, 'filled')
title('degrauD[n]')
xlabel('n')
ylabel('degraD')
legend('u(n-7)')

figure(2)

subplot(221)
stem(n, x1, 'filled')
title('x1[n]')
xlabel('n')
ylabel('x1')
legend('u(-n-7)-u(-n-6)')

subplot(222)
stem(n, x2, 'filled')
title('x2[n]')
xlabel('n')
ylabel('x2')
legend('1-u(-n-6)')

subplot(223)
stem(n, x3, 'filled')
title('x3[n]')
xlabel('n')
ylabel('x3')
legend('(1/5)(-1/3)^{n+6}u(-n-6)')

subplot(224)
stem(n, x4, 'filled')
title('x4[n]')
xlabel('n')
ylabel('x4')
legend('(15)(-1/3)^{n-6}u(-n+6)')
