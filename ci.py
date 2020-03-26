from tkinter import *
from PIL import ImageTk,Image
import requests


import json

window = Tk()
window.title('Client Interface')
window.configure(background="#222")
window.geometry("800x600")


def request_id(api_key,name,region):
    url = "https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name+"?api_key="+api_key
    res = requests.get(url)
    print(res)
    return json.loads(res.text)['id']

def request_game_info(id,api_key,region):
    url = "https://"+region+".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+id+"?api_key="+api_key
    res = requests.get(url)
    print(res.text)
    part_list = json.loads(res.text)['participants']
    names = []
    champions = []

    for i in part_list:
        names.append(i['summonerName'])
        champions.append(i['championId'])


    return names,champions


api_key="RGAPI-44cbb52d-1ee1-4052-8aef-bde3937576ba"
def get_ennemie():
    p1 = summernorname.get()
    region = regions.get()
    print(p1)
    id= request_id(api_key,p1,region)
    print(id)
    names,champions_key =request_game_info(id,api_key,region)

    import random
    if p1 in names[5:]:
        p2 = random.choice(names[:5])
    elif p1 in names[:5]:
        p2=random.choice(names[5:])

    res.config(text=p2)
















lbl = Label(window, text="Welcome to Hunter Of Legends , Enter you Summenor Name and Get your prey",bg='#222',fg="orange",font=("Arial",15))
lbl.place(x=40,y=20)


namelbl = Label(window, text="Enter your Summoner Name: ",bg="#222",
fg="orange",font=("Arial",18))
namelbl.place(x=200,y=200)



summernorname = Entry(window,text="Name",bg="white",width=22,font=('Arial',15))
summernorname.place(x=240,y=250)

regionlbl = Label(window, text="Region: ",bg="#222",fg="orange",font=("Arial",18))
regionlbl.place(x=300,y=300)



regions = Entry(window,text="bruda",bg="white",width=22,font=('Arial',15))
regions.place(x=250,y=350)


res = Label(window, text="",bg="#222",fg="orange",font=("Arial",18))
res.place(x=320,y=460)




submit = Button(window,text="Submit",bg="white",width=10,font=('Arial',15),command=get_ennemie)
submit.place(x=300,y=400)


window.mainloop()
