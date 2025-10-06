import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Constantes da Natureza
CARGA_ELEMENTAR_E = 1.602176634e-19  # Carga elementar em Coulombs (C)
H_TEORICO = 6.62607015e-34         # Constante de Planck teórica em J·s

# Dados fornecidos: Frequência (nu) em Hz e Tensão de Corte (V0) em Volts (V)
dados = {
    'Azul 1': [10.3657869 * 10**14, 0.83],
    'Azul 2': [8.65752182 * 10**14, 0.72],
    'Azul 3': [6.95466595 * 10**14, 0.67],
    'Verde': [5.52879628 * 10**14, 0.41],
    'Laranja': [5.26284792 * 10**14, 0.2],
}

# 1. Preparação dos Dados
frequencias_nu = np.array([v[0] for v in dados.values()])
tensoes_v0 = np.array([v[1] for v in dados.values()])

# 2. Execução da Regressão Linear (experimental)
slope_a_exp, intercept_b_exp, r_value, _, _ = linregress(frequencias_nu, tensoes_v0)

# 3. Cálculo da Curva Experimental (para plotagem)
V0_previsto_exp = slope_a_exp * frequencias_nu + intercept_b_exp

# 4. Cálculo da Curva Teórica
# A curva teórica usa h_teórico/e como declive e o intercepto (Função Trabalho) experimental.

# Declive Teórico (a_teo = h_teo / e)
slope_a_teo = H_TEORICO / CARGA_ELEMENTAR_E

# Interceção Teórica (b_teo = -Phi_exp / e). Usamos o intercepto experimental para
# garantir que a reta teórica comece no mesmo ponto de corte (mesmo metal).
intercept_b_teo = intercept_b_exp

# Tensão de Corte Teórica (V_0,teo)
V0_previsto_teo = slope_a_teo * frequencias_nu + intercept_b_teo

# 5. Saída no Terminal (Mantendo os resultados principais)
print("--- Resultados da Regressão Linear ---")
print(f"Declive Experimental (h/e): {slope_a_exp:.4e} V\u00B7s")
print(f"Declive Teórico (h\u2081\u2091\u2092/e): {slope_a_teo:.4e} V\u00B7s")

h_experimental = slope_a_exp * CARGA_ELEMENTAR_E
diferenca_percentual_h = abs(h_experimental - H_TEORICO) / H_TEORICO * 100

print("-" * 35)
print(f"Constante de Planck Experimental (h): {h_experimental:.4e} J\u00B7s")
print(f"Diferença percentual em relação a h\u2081\u2091\u2092: {diferenca_percentual_h:.2f}%")
print("-" * 35)


# 6. Geração do Gráfico com Curva Teórica
plt.figure(figsize=(10, 6))

# Pontos de dados experimentais
plt.scatter(frequencias_nu, tensoes_v0, color='blue', zorder=5, 
            label='Dados Experimentais (\u03BD, V\u2080)', marker='o')

# Reta de Regressão Experimental (dados previstos)
plt.plot(frequencias_nu, V0_previsto_exp, color='red', linestyle='-', zorder=4,
         label=f'Reta Experimental ($h_{{exp}}/e$, $R={r_value:.4f}$)')

# Reta Teórica (pontos calculados teóricos)
plt.plot(frequencias_nu, V0_previsto_teo, color='green', linestyle='--', zorder=3,
         label=f'Reta Teórica ($h_{{teo}}/e$)')

# Personalização do Gráfico
plt.title('Efeito Fotoelétrico: Comparação entre Experimental e Teórico')
plt.xlabel('Frequência $\\nu$ (Hz) ($\times 10^{14}$)')
plt.ylabel('Tensão de Corte $V_0$ (V)')

# Formatação do eixo x para melhor leitura de expoentes
plt.ticklabel_format(axis='x', style='sci', scilimits=(14, 14))

plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.show()