import CoolProp.CoolProp as CP 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados_vazao = pd.read_excel(r"C:\Users\guilh\OneDrive\UFMG\IC\caracterização máquina co2\testes\17°C\86 bar\17_86_vazão.xlsx")
dados_temperatura = pd.read_excel(r"C:\Users\guilh\OneDrive\UFMG\IC\caracterização máquina co2\testes\17°C\86 bar\17_86_temperatura.xlsx")

tempo_lista = []
cop_lista = []

cp = CP.PropsSI('C', 'T', 298.15, 'P', 101325.0, 'water')

compressor_pot = 600

for index, row in dados_temperatura.iterrows():
    t21 = row['T21'] + 273.15  
    t22 = row['T22'] + 273.15  
    m_h20 = dados_vazao.at[index, 'V2']/60  

    cop = abs((cp * m_h20 * (t21 - t22)) / compressor_pot)  
   
    cop_lista.append(cop)
    tempo_lista.append(row['tempo, s'])  

cop_media = np.mean(cop_lista)

plt.figure(figsize=(10, 6))
plt.plot(tempo_lista, cop_lista, label='COP')
plt.xlabel('tempo, s')
plt.ylabel('COP')
plt.title('COP em função do tempo')
plt.legend()
plt.grid(True)
plt.show()

df_cop = pd.DataFrame({'tempo, s': tempo_lista, 'COP': cop_lista, 'COP Médio': [cop_media] * len(tempo_lista)})

df_cop.to_excel(r"C:\Users\guilh\OneDrive\UFMG\IC\caracterização máquina co2\testes\17°C\86 bar\COP_17_86.xlsx", index=False)
