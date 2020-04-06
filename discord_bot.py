import discord
from discord.ext import commands

import requests
import pprint
import json
import time
import pandas as pd
global p2


api_key= API_KEY
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















bot = commands.Bot(command_prefix='#')



@bot.event
async def on_ready():
    bot.remove_command('help')
    await bot.change_presence(activity=discord.Game(name="#commands to display commands :D"))



'''
@bot.command()
async def play(ctx):
    await ctx.send("**Welcome To Hunter Of Legends**, If you are in a game Use #Name <SummonerName>\n")
    await ctx.send("Please type your nickname")


'''
@bot.command()
async def Name(ctx,message):
    print(message)
    try:
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

    except KeyError:
        await ctx.send("*Oops...*,You either are not in a match or you typed your summoner's name with spaces ")






@bot.command()
async def Score(ctx,p1,Prey):
    try:

        p1_scores,p2_scores=get_match_kills(p1,Prey,api_key,region)
        await ctx.send(f"Your Score is **{p1_scores}** Good job!!")
    except KeyError:
        await ctx.send("*Oops...*,You either are not in a match or you typed your summoner's name with spaces ")

@bot.command()
async def commands(ctx):

    halp = discord.Embed(title="**Welcome to hunter of legends**\nhere are the commands that you can use ",
        colour =0xff0000)
    halp.add_field(name="Name",
        value="Enter your league of legends username to get your prey\n\
        To do that simply use #Name <summonername> ",inline=False)
    halp.add_field(name="Score",
        value=" Enter your league of legends username and the prey's name\n\
        to get your score to do that simply use #Score <summonername> <prey>",inline=False)
    await ctx.send('',embed=halp)
bot.run(TOKEN)
