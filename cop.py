import CoolProp.CoolProp as CP 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#importa os dados. ESPECIFICAR O TESTE
dados_vazao = pd.read_excel(r"C:\Users\guilh\OneDrive\UFMG\IC\caracterização máquina co2\testes\17°C\86 bar\17_86_vazão.xlsx")
dados_temperatura = pd.read_excel(r"C:\Users\guilh\OneDrive\UFMG\IC\caracterização máquina co2\testes\17°C\86 bar\17_86_temperatura.xlsx")
dados_delta_h = pd.read_excel(r"C:\Users\guilh\OneDrive\UFMG\IC\caracterização máquina co2\testes\delta_h.xlsx")

tempo_lista = []
pot_frig_lista = []
cop_lista = []
m_co2_lista = []

#algumas constantes. ESPECIFICAR O TESTE
cp = CP.PropsSI('C', 'T', 298.15, 'P', 101325.0, 'water')
delta_h = (dados_delta_h['17_86'].iloc[0])*1E3
compressor_pot = 600

#calculos
for index, row in dados_temperatura.iterrows():
    t21 = row['T21'] + 273.15  
    t22 = row['T22'] + 273.15  
    m_h2o = dados_vazao.at[index, 'V2']/60  
    pot_frig = abs(cp* m_h2o * (t21-t22))
    cop = pot_frig / compressor_pot
    m_co2 = abs(m_h2o*cp*(t21-t22))/delta_h

    m_co2_lista.append(m_co2)
    pot_frig_lista.append(pot_frig)
    cop_lista.append(cop)
    tempo_lista.append(row['tempo, s'])  

#faz a média de alguns dados
cop_media = np.mean(cop_lista)
pot_frig_media = np.mean(pot_frig_lista)
m_co2_media = np.mean(m_co2_lista)

plt.figure(figsize=(10, 6))
plt.plot(tempo_lista, cop_lista, label='COP')
plt.xlabel('tempo, s')
plt.ylabel('COP')
plt.title('COP em função do tempo')
plt.legend()
plt.grid(True)
plt.show()

df_cop = pd.DataFrame({'tempo, s': tempo_lista, 'Vazão mássica de CO2, kg/s': m_co2_media, 'Potência frigorífica, W': pot_frig_media, 'COP': cop_lista, 'COP Médio': [cop_media] * len(tempo_lista)})

#salva os dados. ESPECIFICAR O TESTE
df_cop.to_excel(r"C:\Users\guilh\OneDrive\UFMG\IC\caracterização máquina co2\testes\17°C\86 bar\teste_17_86.xlsx", index=False)
