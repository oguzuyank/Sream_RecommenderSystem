import pandas as pd
import time
from datetime import datetime
astart = datetime.now().strftime('%d-%b-%Y-%H:%M:%S') 
print(astart)
say=0

df = pd.read_excel (r'C:\Users\oguzu\Desktop\Userİd.xlsx')
userlist = pd.DataFrame(df.Users.unique()).to_numpy()
erorrID = [] 

for UserId in userlist: 
    say = say + 1
    
    UserId = int( UserId ) 
    UserId = str( UserId ) 
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=1FC012E5AD51D79EAC1B77D851CE3389&steamid="+ UserId +"&format=json"
    df1 = pd.read_json(url)
    #df["response"] #Jsonun ismi
    try:
        df1 = pd.json_normalize(df1["response"].games)
        df1["user"] = UserId
        if (UserId == "76561198026324627"):
            df2 = df1
        else:
                df2 = pd.concat([df2,df1], axis=0,ignore_index=bool)
    except:
        
        int(UserId)
        erorrID.append(UserId)
        print(UserId)
        
    pass

    if(say % 100 == 0):
        print(say)
        df2.to_csv(r'C:\Users\oguzu\Desktop\Userİd.csv', index = bool )
df2.to_csv(r'C:\Users\oguzu\Desktop\Userİd.csv', index = bool )

astop = datetime.now().strftime('%d-%b-%Y-%H:%M:%S') 
 