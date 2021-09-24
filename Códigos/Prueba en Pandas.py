#from windrose import WindroseAxes
import pandas as pd

x = pd.read_csv('C:\\Users\\gm_ll\\OneDrive - UNIVERSIDAD AUTONOMA DEL CARIBE\\Gmecatronics\\Sistemas informáticos\\Python\\Códigos\\Test.csv')
df = pd.DataFrame(x)
print(df)
a = list(df.iloc[0:,0]) #Las dos columnas esán siendo leíadas como una sola. ¿Por qué?
#b = list(df.iloc[0:,1])
print(a)
#print(b)