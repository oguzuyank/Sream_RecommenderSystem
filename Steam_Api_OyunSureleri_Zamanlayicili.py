"""
Burda fonksiyonu tanımlıyoruz.
Fonsyon mutlaka bir tablı olarak yazılmalı yoksa hata verir

Parameters
----------
x : TYPE
    DESCRIPTION.
a : TYPE
    DESCRIPTION.

Returns
-------
None.

"""
import pandas as pd
import time
from datetime import datetime
astart = datetime.now().strftime('%d-%b-%Y-%H:%M:%S') 
print(astart)
say=0

#df = pd.read_excel (r'C:\Users\oguzu\Desktop\Userİd.xlsx')
#userlist = pd.DataFrame(df.Users.unique()).to_numpy()

df = pd.read_json (r'C:\Users\oguzu\Desktop\UserFriendsİd.json')
userlist = pd.DataFrame(df.steamid.unique()).to_numpy()

erorrID = [] 

for UserId in userlist: 
    say = say + 1
    
    UserId = int( UserId ) 
    UserId = str( UserId ) 
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=E7068F836A557CEE3BEC1753C236D01F&steamid="+ UserId +"&format=json"
    #df["response"] #Jsonun ismi
    try:
            #time.sleep(3)
            df1 = pd.read_json(url)
            df1 = pd.json_normalize(df1["response"].games)
            df1["user"] = UserId
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
        print("********************User Unique Len=  ",len(df2.user.unique()))
        print( datetime.now().strftime('%d-%b-%Y-%H:%M:%S') )
        time.sleep(180)
        
    if(say % 1000 == 0):
        df2.to_json(r"C:\Users\oguzu\Desktop\Userİd.json", index = bool )
        df2.to_json(r"C:\Users\oguzu\Desktop\UserİdYedek.json", index = bool )

astop = datetime.now().strftime('%d-%b-%Y-%H:%M:%S') 


 

