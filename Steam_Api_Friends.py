import pandas as pd
import time
from datetime import datetime

say=0

df = pd.read_json (r'C:\Users\oguzu\Desktop\SteamTez\SteamData\Data\SteamGameTime_raw.json')
userlist = pd.DataFrame(df.user.unique()).to_numpy()
df.drop(df.index, axis=0, inplace=True)
erorrID = [] 

for UserId in userlist: 
    say = say + 1
    
    try:
        UserId = int( UserId ) 
        UserId = str( UserId ) 
        url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=E7068F836A557CEE3BEC1753C236D01F&steamid="+ UserId +"&relationship=friend&format=json"
        df1 = pd.read_json(url)
        df1 = pd.json_normalize(df1["friendslist"].friends)
        if (say==1):
            df2 = df1
        else:
            df2 = pd.concat([df2,df1], axis=0,ignore_index=bool)
    except:
        int(UserId)
        erorrID.append(UserId)
        print(UserId+ "=" + str(say))
    pass
    
    if(say % 100 == 0):
        print("********************Sayı=  ",say)
        print("********************Error=  ",len(erorrID))
        print("********************İndex Len=  ",len(df2.index))
        print("********************User Unique Len=  ",len(df2.steamid.unique()))
        print( datetime.now().strftime('%d-%b-%Y-%H:%M:%S') )
        time.sleep(180)
        
    if(say % 500 == 0):
        df2.to_json(r"C:\Users\oguzu\Desktop\UserFriendsİd.json", index = bool )
        df2.to_json(r"C:\Users\oguzu\Desktop\UserFriendsİdYedek.json", index = bool )







