# Preparando o ambiente
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import statsmodels.api as sm

# Construindo o dataset
dados = pd.DataFrame({
    'Qtd_Poluente': [1, 2, 3, 4, 5, 6],
    'Dano_Eco': [3, 6, 7, 10, 10, 12]
})

# A)
# Gráfico de dispersão
sb.scatterplot(x='Qtd_Poluente', y='Dano_Eco', data=dados)
plt.title('Dispersão: Quantidade de Poluente x Dano Ecológico')
plt.xlabel('Quantidade de Poluentes (ug/L)')
plt.ylabel('Dano Ecológico')
plt.show()

# Covariância
# Quando positiva, significa que as variáveis têm relação proporcional. Se for negativa, não temos isso.
print("Covariância:", np.cov(dados['Qtd_Poluente'], dados['Dano_Eco'])[0, 1])

# Correlação linear de Pearson
# Taxa de confiabilidade na correlação das informações.
print("Correlação:", np.corrcoef(dados['Qtd_Poluente'], dados['Dano_Eco'])[0, 1])

# Gráfico de correlação
sb.heatmap(dados.corr(), annot=True, cmap='coolwarm')
plt.title("Mapa de Correlação")
plt.show()

# B)
X = sm.add_constant(dados['Qtd_Poluente'])
modelo = sm.OLS(dados['Dano_Eco'], X).fit()

sb.regplot(x='Qtd_Poluente',
           y='Dano_Eco',
           data=dados,
           ci=95,  # Taxa de confiança
           line_kws={"color": "red"})
plt.title('Gráfico de Dispersão com Reta de Regressão')
plt.xlabel('Quantidade de Poluentes (ug/L)')
plt.ylabel('Dano Ecológico')
plt.show()

# C)
# Aqui já conseguimos prever os próximos danos ecológicos com base na conta pronta.
print(modelo.summary())
# Y = a + bX + E
# Dano Ecológico = 2.0000 + 1.7143 * Quantidade de Poluente + E (flutuações aleatórias)

# D)
# R2          = R-squared:          0.952
# R2 ajustado = Adj. R-squared:     0.940
# p-value (F) = Prob (F-statistic): 0.000864

# E)
nova_obs = 9
intercepto, coeficiente = modelo.params
print(intercepto + coeficiente * nova_obs)
