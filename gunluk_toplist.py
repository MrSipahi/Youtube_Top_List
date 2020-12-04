import pymysql as MySQLdb
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from PIL import Image
from instabot import Bot
import locale
import os
import time

 


db = MySQLdb.connect("ip","user","password","db_names" )
cursor = db.cursor()

query="Select * from kanal"
df = pd.read_sql(query, con=db)

dun = datetime.today() - timedelta(days=1)
dun = dun.strftime("%Y-%m-%d")

try:
    bot = Bot()
    bot.login(username=" ",password=" ")
except:
    pass



kanalID_list = df["ID"].unique()
kanalad_list = df["ad"].unique()
kanaltag_list = df["tag"].unique()
taglar=[]

for x in kanaltag_list:
    taglar.append(f"{x}")


goruntulenmeler=[]
begenmeler=[]
begenmemeler=[]
yorumlar=[]


for kanalID in kanalID_list:
    query=f"Select * from gunluk where kanal_ID='{kanalID}' AND tarih='{dun}' "
    df = pd.read_sql(query, con=db)
    goruntulenmeler.append(df['goruntulenme'].sum())
    begenmeler.append(df['begenme'].sum())
    begenmemeler.append(df['begenmeme'].sum())
    yorumlar.append(df['yorum'].sum())

liste = [[] for i in range(len(kanalID_list))]
for j in range(0,len(kanalID_list)):
    kanalad= kanalad_list[j]
    #kanalad= kanalad.replace(" ","_")
    liste[j] = [kanalad,goruntulenmeler[j],begenmeler[j],begenmemeler[j],yorumlar[j]]

df2= pd.DataFrame(list(liste),columns =['Ad', 'Goruntulenme', 'Begenme', 'Begenmeme', 'Yorum']) 
x = df2.sort_values('Goruntulenme',ascending=False)

caption2 = []
def goruntulenmetop():
    plt.style.use("dark_background")
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey

    colors = [
        '#0E5863',
        '#127785',
        '#1697A9',
        '#1AB3C8',
        '#2BCCE3',      
    ]
    explode = (0.1, 0.02, 0.02, 0.02, 0.02)#, 0.01, 0.01, 0.01, 0.01, 0.01)
    figure = plt.gcf()  # get current figure
    figure.set_size_inches(16, 9) 

    x = df2.sort_values('Goruntulenme',ascending=False)
    result = x['Ad']
    for adlar in result:
        kanalad = adlar
        break;
    result = x['Goruntulenme']
    for adlar in result:
        goruntu = adlar
        break;

    plt.pie(x['Goruntulenme'].head(5),labels=x['Ad'].head(5),autopct='%1.1f%%',colors=colors,shadow=True,startangle=90,explode=explode,textprops={'fontsize': 23})
    plt.axis('equal')
    plt.title(f"{dun}\nGünün En Çok İzlenen Youtube Kanalları\nTop 5 List",fontsize=25)
    plt.savefig('gunluk_top10.jpg',bbox_inches='tight')
    caption2.append(f"Günün En Çok İzlenen, Beğeni alan, Dislike alan ve Yorum alan Youtube Kanalları Top 5\n\n\nListemizde bulunan 14 Youtube Kanalının arasında en çok izlenen Youtube Kanalı;\n{goruntu} görüntülenme ile {kanalad}") 
    img = '/home/yonetici/verianaliz/arkaplan.jpg'
    watermark_photo(img, 't1.jpg',
                        'gunluk_top10.jpg', position=(225,90))

def begenmetop():
    plt.style.use("dark_background")
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey

    colors = [
        '#0E5863',
        '#127785',
        '#1697A9',
        '#1AB3C8',
        '#2BCCE3',      
    ]
    explode = (0.1, 0.02, 0.02, 0.02, 0.02)#, 0.01, 0.01, 0.01, 0.01, 0.01)
    figure = plt.gcf()  # get current figure
    figure.set_size_inches(16, 9) 

    x = df2.sort_values('Begenme',ascending=False)
    result = x['Ad']
    for adlar in result:
        kanalad = adlar
        break;
    result = x['Begenme']
    for adlar in result:
        begenme = adlar
        break;
    plt.pie(x['Begenme'].head(5),labels=x['Ad'].head(5),autopct='%1.1f%%',colors=colors,shadow=True,startangle=90,explode=explode,textprops={'fontsize': 23})
    plt.axis('equal')
    plt.title(f"{dun}\nGünün En Çok Begenilen Youtube Kanalları\nTop 5 List",fontsize=25)
    plt.savefig('gunluk_top10.jpg',bbox_inches='tight')
    caption2.append(f"\nListemizde bulunan 14 Youtube Kanalının arasında bugün en çok beğenilen Youtube Kanalı;\n{begenme} begenme ile {kanalad}")
    img = '/home/yonetici/verianaliz/arkaplan.jpg'
    watermark_photo(img, 't2.jpg',
                        'gunluk_top10.jpg', position=(225,90))

def begenmemetop():
    plt.style.use("dark_background")
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey

    colors = [
        '#0E5863',
        '#127785',
        '#1697A9',
        '#1AB3C8',
        '#2BCCE3',      
    ]
    explode = (0.1, 0.02, 0.02, 0.02, 0.02)#, 0.01, 0.01, 0.01, 0.01, 0.01)
    figure = plt.gcf()  # get current figure
    figure.set_size_inches(16, 9) 

    x = df2.sort_values('Begenmeme',ascending=False)
    result = x['Ad']
    for adlar in result:
        kanalad = adlar
        break;
    result = x['Begenmeme']
    for adlar in result:
        begenmeme = adlar
        break;
    plt.pie(x['Begenmeme'].head(5),labels=x['Ad'].head(5),autopct='%1.1f%%',colors=colors,shadow=True,startangle=90,explode=explode,textprops={'fontsize': 23})
    plt.axis('equal')
    plt.title(f"{dun}\nGünün En Çok Dislike alan Youtube Kanalları\nTop 5 List",fontsize=25)
    plt.savefig('gunluk_top10.jpg',bbox_inches='tight')
    caption2.append(f"\nListemizde bulunan 14 Youtube Kanalının arasında bugün en çok Dislike alan Youtube Kanalı;\n{begenmeme} dislike ile {kanalad}") 
    img = '/home/yonetici/verianaliz/arkaplan.jpg'
    watermark_photo(img, 't3.jpg',
                        'gunluk_top10.jpg', position=(225,90))

def yorumtop():
    plt.style.use("dark_background")
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey

    colors = [
        '#0E5863',
        '#127785',
        '#1697A9',
        '#1AB3C8',
        '#2BCCE3',      
    ]
    explode = (0.1, 0.02, 0.02, 0.02, 0.02)#, 0.01, 0.01, 0.01, 0.01, 0.01)
    figure = plt.gcf()  # get current figure
    figure.set_size_inches(16, 9) 

    x = df2.sort_values('Yorum',ascending=False)
    result = x['Ad']
    for adlar in result:
        kanalad = adlar
        break;
    result = x['Yorum']
    for adlar in result:
        yorum = adlar
        break;
    plt.pie(x['Yorum'].head(5),labels=x['Ad'].head(5),autopct='%1.1f%%',colors=colors,shadow=True,startangle=90,explode=explode,textprops={'fontsize': 23})
    plt.axis('equal')
    plt.title(f"{dun}\nGünün En Çok Yorum alan Youtube Kanalları\nTop 5 List",fontsize=25)
    plt.savefig('gunluk_top10.jpg',bbox_inches='tight')
    caption2.append(f"\nListemizde bulunan 14 Youtube Kanalının arasında bugün en çok Yorum alan Youtube Kanalı;\n{yorum} yorum ile {kanalad} \n\n\n{taglar}\n\n\n#youtube #youtubetürkiye #enesbatur #basakkarahan #delimine #reynmen #orkunışıtmak #twitchturkiye #wtcnn #hazretiyasuo #hzyasuo #evonmoss #twitch #kafalar #alibicim #mesutcantomay #babala #oguzhanugur #magazin #youtubemagazin") 
    img = '/home/yonetici/verianaliz/arkaplan.jpg'
    watermark_photo(img, 't4.jpg',
                        'gunluk_top10.jpg', position=(225,90))


def watermark_photo(input_image_path,
                output_image_path,
                watermark_image_path,
                position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    base_image.paste(watermark, position)
    base_image.save(output_image_path)


goruntulenmetop()
plt.close()
begenmetop()
plt.close()
begenmemetop()
plt.close()
yorumtop()

fotolar=["t1.jpg","t2.jpg","t3.jpg","t4.jpg"]
try:
    bot.upload_album(fotolar,caption=f"{caption2[0]}\n\n{caption2[1]}\n\n{caption2[2]}\n\n{caption2[3]}")
    os.remove("t1.jpg.REMOVE_ME")
    os.remove("t2.jpg.REMOVE_ME")
    os.remove("t3.jpg.REMOVE_ME")
    os.remove("t4.jpg.REMOVE_ME")
except Exception as e:
    print(e)


