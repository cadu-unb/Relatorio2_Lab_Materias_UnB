import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Constante da Natureza
# Carga elementar do elétron (e) em Coulombs (C)
CARGA_ELEMENTAR_E = 1.60e-19 

# Dados fornecidos: Frequência (nu) em Hz e Tensão de Corte (V0) em Volts (V)
dados = {
    # 'Azul 1': [10.3657869e14, 0.83],
    # 'Azul 2': [8.65752182e14, 0.72],
    # 'Azul 3': [6.95466595e14, 0.67],
    # 'Verde': [5.52879628e14, 0.41],
    # 'Laranja': [5.26284792e14, 0.2],
'Azul 1': [865153248922717.2, 0.65],
 'Azul 2': [743527055929066.8, 0.52],
 'Azul 3': [652580178281142.4, 0.51],
 'Verde': [525920704701664.5, 0.32],
 'Laranja': [501929581114123.75, 0.2]
}

# 1. Preparação dos Dados
# A regressão linear espera que X e Y sejam arrays.
frequencias_nu = np.array([v[0] for v in dados.values()])
tensoes_v0 = np.array([v[1] for v in dados.values()])

# 2. Execução da Regressão Linear
# Usaremos scipy.stats.linregress, que é ideal para regressão linear simples.
# Retorna: slope (a), intercept (b), r_value, p_value, std_err
slope_a, intercept_b, r_value, p_value, std_err = linregress(frequencias_nu, tensoes_v0)

# 3. Cálculo das Constantes Físicas
# Declive (a) = h/e  => h = a * e
h_experimental = slope_a * CARGA_ELEMENTAR_E

# Interceção (b) = -Phi/e  => Phi = -b * e
Phi_experimental_J = -intercept_b * CARGA_ELEMENTAR_E

# Converter Função Trabalho para Eletron-Volts (eV) para facilitar a comparação
# 1 eV = e J
Phi_experimental_eV = Phi_experimental_J / CARGA_ELEMENTAR_E

# 4. Cálculo da Linha de Regressão (Valores Previstos)
V0_previsto = slope_a * frequencias_nu + intercept_b

# 5. Saída no Terminal (Requisito 1)
print("--- Resultados da Regressão Linear para o Efeito Fotoelétrico ---")
print(f"Equação da Reta (V₀ vs \u03BD): V\u2080 = {slope_a:.4e} * \u03BD + {intercept_b:.4f}")
print("-" * 50)
print("\n[Parâmetros da Regressão]")
print(f"Declive (a): {slope_a:.8e} V\u00B7s")
print(f"Interceção (b): {intercept_b:.8f} V")
print(f"Coeficiente de Correlação (R): {r_value:.8f}")

print("\n[Valores Físicos Experimentais Encontrados]")
# h
h_teorico = 6.626e-34 # J·s
diferenca_percentual_h = abs(h_experimental - h_teorico) / h_teorico * 100
print(f"1. Constante de Planck (h): {h_experimental:.8e} J\u00B7s")
print(f"   (Teórico: {h_teorico:.8e} J\u00B7s | Diferença: {diferenca_percentual_h:.2f}%)")

# Phi
Phi_teorico_eV_Na = 2.3  # Exemplo comum para um metal (Sódio), se não for especificado
print(f"2. Função Trabalho (\u03A6): {Phi_experimental_J:.8e} J")
print(f"   Função Trabalho (\u03A6): {Phi_experimental_eV:.8f} eV")
print(f"   (Valor em eV é mais 'geral' e mais fácil de comparar.)")

print("\n--- FIM DOS CÁLCULOS ---")


# 6. Geração do Gráfico (Requisito 2)
plt.figure(figsize=(10, 6))

# Pontos de dados experimentais
plt.scatter(frequencias_nu, tensoes_v0, color='blue', label='Dados Experimentais (\u03BD, V\u2080)', marker='o')

# Reta da regressão linear (dados previstos)
plt.plot(frequencias_nu, V0_previsto, color='red', label=f'Reta de Regressão (R={r_value:.4f})')

# Personalização do Gráfico
plt.title('Regressão Linear: Efeito Fotoelétrico (V\u2080 vs Frequência)\n', fontsize=18)
plt.xlabel('\nFrequência $\\nu$ (Hz)', fontsize=14)
plt.ylabel('Tensão de Corte $V_0$ (V)\n', fontsize=14)
plt. grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=14)
# plt.show()
plt.savefig('efeito_fotoeletrico_regressao.pdf')