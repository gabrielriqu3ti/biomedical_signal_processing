% PTC3456 - Processamento de Sinais Biol�gicos 
% Aula 7
% Tarefa sobre projeto de ADC
%
% x(t) = s(t) + r(t)
% x(t)     : ECG anal�gico na faixa [-5.0, 5.0] V
% s(t)     : ECG anal�gico sem r�ido na faixa [0.01, 100] Hz
% r(t)     : ru�do branco aditivo com desvio-padr�o de 2 mV (RMS)
% 
% ADC de 12 bits na faixa [-5, 5] V
% e(t) = x(t) - x_ADC(t)
% x_ADC(t) : ECG digital saindo do ADC
% u        :
% e(t)     : erro de quantiza��o do ADC - distribui��o uniforme de [-u/2, u/2]
% 

%% Valores pr�-definidos
% Sinal de ECG
V_min = -5; % (V) - voltagem m�nima do sinal de ECG anal�gico
V_max = 5; % (V) - voltagem m�xima do sinal de ECG anal�gico
f_ECG_min = 0.01; % (Hz) - frequ�ncia m�nima do sinal de ECG anal�gico sem ru�do
f_ECG_max = 100; % (Hz) - frequ�ncia m�xima do sinal de ECG anal�gico sem ru�do
white_noise_RMS = 0.002; % (V) - desvio-padr�o da voltagem do ru�do branco
% ADC
N_bits = 12; % n�mero de bits do ADC

% C�lculo da resolu��o da quantifica��o do ADC
u = (V_max - V_min) / (2^N_bits - 1); % (V) - resolu��o

% C�lculo da desvio-padr�o do erro de quantiza��o do ADC
eq_RMS = sqrt(u^2 / 12); % (V^2) - desvio-padr�o (ou RMS) do erro de quantiza��o do ADC

% Filtro Butterworth (anal�gico)
%                 1
% G(f) = --------------------
%        sqrt(1 + (f/f_c)^2n)
order_butter = 8; % ordem do filtro Butterworth
f_c = f_ECG_max; % frequ�ncia de corte do filtro Butterworth
f_s = 2 * f_c * ((white_noise_RMS / eq_RMS)^2 - 1)^(1/(2*order_butter)); % frequ�ncia de amostragem do ADC

[num_butter, den_butter] = butter(order_butter, 2*pi*f_c, 'low', 's');
H_butter = tf(num_butter, den_butter);

w = logspace(-2, 4, 200);
[mag, phase, w_out] = bode(H_butter, w);

mag_min = -200;
mag_max = 20;
phase_min = -730;
phase_max = 10;

%% Diagrama de Bode do filtro anal�gico
figure(1)
subplot(2,1,1)
plot(w_out, 20*log10(mag(:,:)), 'DisplayName', 'magnitude')
hold on
plot([2*pi*f_c, 2*pi*f_c], [mag_min, mag_max], 'k--', 'DisplayName', 'cut-off frequency')
plot([2*pi*f_s, 2*pi*f_s], [mag_min, mag_max], 'r--', 'DisplayName', 'sampling frequency')
plot([pi*f_s, pi*f_s], [mag_min, mag_max], 'm--', 'DisplayName', 'Nyquist frequency')
fill([2*pi*f_ECG_min, 2*pi*f_ECG_max, 2*pi*f_ECG_max, 2*pi*f_ECG_min], [mag_min, mag_min, mag_max, mag_max], ...
    'g', 'FaceAlpha', 0.1, 'EdgeColor', 'none', 'DisplayName', 'ECG band')
hold off
title(['Bode Diagram of ', num2str(order_butter), 'th-order lowpass Butterworth Filter'])
ylabel('Magnitude (dB)')
xlabel('Frequency (rad/s)')
ylim([mag_min, mag_max])
legend('Location', 'southwest')
set(gca, 'XScale', 'log')

subplot(2,1,2)
plot(w_out, phase(:,:), 'DisplayName', 'phase')
hold on
plot([2*pi*f_c, 2*pi*f_c], [phase_min, phase_max], 'k--', 'DisplayName', 'cut-off frequency')
plot([2*pi*f_s, 2*pi*f_s], [phase_min, phase_max], 'r--', 'DisplayName', 'sampling frequency')
plot([pi*f_s, pi*f_s], [phase_min, phase_max], 'm--', 'DisplayName', 'Nyquist frequency')
fill([2*pi*f_ECG_min, 2*pi*f_ECG_max, 2*pi*f_ECG_max, 2*pi*f_ECG_min], [phase_min, phase_min, phase_max, phase_max], ...
    'g', 'FaceAlpha', 0.1, 'EdgeColor', 'none', 'DisplayName', 'ECG band')
hold off
ylabel('Phase (deg)')
xlabel('Frequency (rad/s)')
ylim([phase_min, phase_max])
legend('Location', 'southwest')
set(gca, 'XScale', 'log')

%% Execicio opicional 1.1

f_s_1_1 = 10000; % Hz - frequ�nciaa de amostragem
G_n_1_1 = 0.001; % ganho do filtro anal�gico na frequ�ncia de Nyquist
filter_order_1_1 = 4; % ordem do filtro anal�gico

% C�lculo da frequ�ncia de corte
f_c_1_1 = f_s/(2 * (1/G_n_1_1^2 - 1)^(1/(2*filter_order_1_1)));
