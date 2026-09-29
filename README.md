# Análise Bivariada

Exercício de análise bivariada entre a quantidade de poluente despejada e o dano ecológico observado.

A ideia é medir se existe relação entre as duas variáveis, o quão forte ela é, e usar isso para prever o dano a partir de uma quantidade de poluente qualquer.

## Dados

| Qtd_Poluente (ug/L) | Dano_Eco |
|---|---|
| 1 | 3 |
| 2 | 6 |
| 3 | 7 |
| 4 | 10 |
| 5 | 10 |
| 6 | 12 |

## O que o script faz

1. Gráfico de dispersão das duas variáveis
2. Covariância e correlação de Pearson
3. Mapa de correlação (heatmap)
4. Regressão linear simples (OLS), com a reta plotada sobre os pontos e intervalo de confiança de 95%
5. Previsão do dano ecológico para uma nova observação

## Resultados

Covariância: 6.0
Correlação de Pearson: 0.976

Como a covariância deu positiva, as variáveis crescem juntas. A correlação perto de 1 mostra que essa relação é forte.

Modelo ajustado:

    Dano_Eco = 2.0000 + 1.7143 * Qtd_Poluente

| Métrica | Valor |
|---|---|
| R² | 0.952 |
| R² ajustado | 0.940 |
| p-value (F) | 0.000864 |

O R² de 0.952 indica que o modelo explica cerca de 95% da variação do dano ecológico. O p-value bem abaixo de 0.05 confirma que a relação é estatisticamente significativa.

Previsão para 9 ug/L de poluente: dano ecológico de aproximadamente 17.43.

## Como rodar

Precisa de Python 3 e das bibliotecas abaixo:

    pip install numpy pandas matplotlib seaborn statsmodels

Depois:

    python analise_bivariada.py

Os três gráficos abrem em janelas separadas, um de cada vez. Feche cada janela para o script continuar. Os resultados numéricos e o resumo da regressão saem no terminal.

## Observação

A amostra tem só 6 observações, então o statsmodels avisa que o teste de normalidade dos resíduos (Omnibus) não é confiável abaixo de 8 amostras. Para o objetivo do exercício isso não atrapalha, mas vale saber.
