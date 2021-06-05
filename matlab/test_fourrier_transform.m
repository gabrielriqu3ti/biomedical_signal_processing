% PTC3456 - Processamento de Sinais Biológicos 
% Aula 5

w = -pi:pi/100:3*pi;

n = -3:3;

h = zeros(1, length(n));
h((n >= -3) & (n <= 3)) = (1/7) * [1, 1, 1, 1, 1, 1, 1];

H = freqz(h, 1, w);

i = sqrt(-1);

G = H .* exp(i * 3 * w);

subplot(2,1,1)
plot(w, G)
xlabel('w')
ylabel('G(w)')

subplot(2,1,2)
plot(n, h)
xlabel('n')
ylabel('h[n]')
