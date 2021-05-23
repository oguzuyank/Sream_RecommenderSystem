import pandas as pd

df = pd.read_json (r'C:\Users\oguzu\Desktop\SteamTez\SteamData\Data\SteamGameTime_raw.json')

df_yedek = df.copy()

df.drop_duplicates (keep = "first", inplace = True)

df.to_json(r"C:\Users\oguzu\Desktop\df_temiz.json", index = bool )
