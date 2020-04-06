import discord
from discord.ext import commands

import requests
import pprint
import json
import time
import pandas as pd
global p2


api_key= "RGAPI-4ac148f7-07f6-4104-96e4-08a1aad4eed6"
region= "euw1"


def request_actid(api_key,name,region):
    url = "https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name+"?api_key="+api_key
    res = requests.get(url)
    return json.loads(res.text)['accountId']

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




def get_match(name,api_key,region):
    id =request_actid(api_key,name,region)


    url = "https://"+region+".api.riotgames.com/lol/match/v4/matchlists/by-account/"+id+"?api_key="+api_key
    res = requests.get(url)
    game_id = json.loads(res.text)['matches'][0]['gameId']
    url2 =  "https://"+region+".api.riotgames.com/lol/match/v4/matches/"+str(game_id)+"?api_key="+api_key
    data = requests.get(url2)

    res2 = json.loads(data.text)['participantIdentities']
    df = pd.DataFrame(columns=['Name','ParticipantID'])
    names = []
    pi = []
    for i in res2:
        print(i['player']['summonerName'])
        print(i['participantId'])
        names.append(i['player']['summonerName'].replace(' ',''))
        pi.append(i['participantId'])

    df['Name'] = names
    df['ParticipantID'] = pi
    return df,game_id









def get_match_kills(p1,p2,api_key,region):
    df,game_id = get_match(p1,api_key,region)
    url = "https://"+region+".api.riotgames.com/lol/match/v4/timelines/by-match/"+str(game_id)+"?api_key="+api_key
    data = requests.get(url)
    print(df)

    print(list(df.loc[df['Name']==p1,'ParticipantID'])[0])


    p1_scores = 0
    p2_scores = 0
    for frame in json.loads(data.text)['frames']:
        for event in frame['events']:

            if event['type'] == "CHAMPION_KILL":
                print(event['killerId'] == list(df.loc[df['Name']==p1,'ParticipantID'])[0] and event['victimId'] == list(df.loc[df['Name']==p2,'ParticipantID'])[0])
                if event['killerId'] == list(df.loc[df['Name']==p1,'ParticipantID'])[0] and event['victimId'] == list(df.loc[df['Name']==p2,'ParticipantID'])[0]:
                    p1_scores += 2
                #elif event['killerId'] == list(df.loc[df['Name']==p2,'ParticipantID'])[0] and event['victimId'] == list(df.loc[df['Name']==p1,'ParticipantID'])[0]:
                #    p2_scores += 2

                elif len(event['assistingParticipantIds']) == 1 and list(df.loc[df['Name']==p1,'ParticipantID'])[0] in event['assistingParticipantIds']:
                    p1_scores += 1
                elif len(event['assistingParticipantIds']) != 1 and list(df.loc[df['Name']==p1,'ParticipantID'])[0] in event['assistingParticipantIds']:
                    p1_scores += 0.5



    return p1_scores















bot = commands.Bot(command_prefix='>')



@bot.event
async def on_read():
    await bot.change_presence(activity=discord.Game(name=">help to display commands :D"))




@bot.command()
async def play(ctx):
    await ctx.send("**Welcome To Hunter Of Legends**, If you are in a game Use #Name <SummonerName>")
    await ctx.send("Please type your nickname")



@bot.command()
async def Name(ctx,message):
    print(message)
    id= request_id(api_key,message.replace(' ',''),region)
    print(id)
    names,champions_key =request_game_info(id,api_key,region)
    p2 =""

    new_names = [x.replace(' ','') for x in names]


    import random
    if message in new_names[5:]:
        await ctx.send(f"**Your Prey is:  **{random.choice(names[:5])}")
    elif message in new_names[:5]:
        await ctx.send(f"**Your Prey is:  **{random.choice(names[5:])}")

    await ctx.send("Use #Score <YourSummnorname> <Prey'sName> to get Your Score after The Match Finishes")




@bot.command()
async def Score(ctx,p1,Prey):
    p1_scores,p2_scores=get_match_kills(p1,Prey,api_key,region)
    await ctx.send(f"Your Score is **{p1_scores}** Good job!!")


bot.run("NDcwMjE2OTM1NDE4NzU3MTMx.XnvuFw.I98iUYAk6J-MTAPbaUB4nIe4d5c")
