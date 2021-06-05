% PTC3456 - Processamento de Sinais Biológicos 
% Aula 7
% Tarefa sobre projeto de ADC
%
% x(t) = s(t) + r(t)
% x(t)     : ECG analógico na faixa [-5.0, 5.0] V
% s(t)     : ECG analógico sem rúido na faixa [0.01, 100] Hz
% r(t)     : ruído branco aditivo com desvio-padrão de 2 mV (RMS)
% 
% ADC de 12 bits na faixa [-5, 5] V
% e(t) = x(t) - x_ADC(t)
% x_ADC(t) : ECG digital saindo do ADC
% u        :
% e(t)     : erro de quantização do ADC - distribuição uniforme de [-u/2, u/2]
% 

%% Valores pré-definidos
% Sinal de ECG
V_min = -5; % (V) - voltagem mínima do sinal de ECG analógico
V_max = 5; % (V) - voltagem máxima do sinal de ECG analógico
f_ECG_min = 0.01; % (Hz) - frequência mínima do sinal de ECG analógico sem ruído
f_ECG_max = 100; % (Hz) - frequência máxima do sinal de ECG analógico sem ruído
white_noise_RMS = 0.002; % (V) - desvio-padrão da voltagem do ruído branco
% ADC
N_bits = 12; % número de bits do ADC

% Cálculo da resolução da quantificação do ADC
u = (V_max - V_min) / (2^N_bits - 1); % (V) - resolução

% Cálculo da desvio-padrão do erro de quantização do ADC
eq_RMS = sqrt(u^2 / 12); % (V^2) - desvio-padrão (ou RMS) do erro de quantização do ADC

% Filtro Butterworth (analógico)
%                 1
% G(f) = --------------------
%        sqrt(1 + (f/f_c)^2n)
order_butter = 8; % ordem do filtro Butterworth
f_c = f_ECG_max; % frequência de corte do filtro Butterworth
f_s = 2 * f_c * ((white_noise_RMS / eq_RMS)^2 - 1)^(1/(2*order_butter)); % frequência de amostragem do ADC

[num_butter, den_butter] = butter(order_butter, 2*pi*f_c, 'low', 's');
H_butter = tf(num_butter, den_butter);

w = logspace(-2, 4, 200);
[mag, phase, w_out] = bode(H_butter, w);

mag_min = -200;
mag_max = 20;
phase_min = -730;
phase_max = 10;

%% Diagrama de Bode do filtro analógico
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

f_s_1_1 = 10000; % Hz - frequênciaa de amostragem
G_n_1_1 = 0.001; % ganho do filtro analógico na frequência de Nyquist
filter_order_1_1 = 4; % ordem do filtro analógico

% Cálculo da frequência de corte
f_c_1_1 = f_s/(2 * (1/G_n_1_1^2 - 1)^(1/(2*filter_order_1_1)));
