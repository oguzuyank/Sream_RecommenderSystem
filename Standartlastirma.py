import pandas as pd

df = pd.read_json('..\SteamData\SteamGameTime_GameClear.json')

# (['appid', 'playtime_forever', 'user'], dtype='object')


df_minmax = pd.DataFrame()

for i in df.appid.unique():
    
    tut = df[df.appid == i]
    
    Q1 = tut.playtime_forever.quantile(0.25) # 1. kartil
    Q3 = tut.playtime_forever.quantile(0.75) # 2. kartil
    IQR = Q3-Q1 # Çeyrek açıklık
    upper = Q3 + 3*IQR #Üst sınır değeri
    
    tut.playtime_forever[tut.playtime_forever > upper] = upper
    
    tut["playtime_forever"] = tut["playtime_forever"]  / tut["playtime_forever"].abs().max()

    df_minmax = pd.concat([df_minmax,tut], axis=0,ignore_index=bool)

    
df_minmax.to_json(r'..\SteamData\df_minmax.json', index = bool )






