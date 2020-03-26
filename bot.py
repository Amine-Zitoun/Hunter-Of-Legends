import requests
import pprint
import json
import time
import pandas as pd
global p2
def request_id(api_key,name,region):
    url = "https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name+"?api_key="+api_key
    res = requests.get(url)
    print(res)
    return json.loads(res.text)['id']

def request_actid(api_key,name,region):
    url = "https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name+"?api_key="+api_key
    res = requests.get(url)
    return json.loads(res.text)['accountId']
def summoner_data (api_key,name,region):
    url = "https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name+"?api_key="+api_key

    res = requests.get(url)
    data = dict(json.loads(res.text))
    return data


def check_if_same(p1,p2,p):
    print(p)
    t1 = p[:5]
    t2 = p[5:]
    print("Checking : {} and {}".format(p1,p2))
    if (p1 in t1 and p2 in t1 )or (p2 in t2 and p1 in t2):
        return True
    else:
        return False



def get_match_history(name,api_key,region,nmatches):
    id =request_actid(api_key,name,region)


    url = "https://"+region+".api.riotgames.com/lol/match/v4/matchlists/by-account/"+id+"?api_key="+api_key
    res = requests.get(url)
    matches = json.loads(res.text)['matches'][:nmatches]
    count = 1
    for i in matches:
        print("GAME NUMBER {}".format(count))
        print("-----------------------------------")
        print("\n\n")
        print("GAME ID: {}\nLANE: {}\nROLE: {}\nChampionID: {} ".format(i['gameId'],
        i['lane'],i['role'],i['champion']))
        print("-----------------------------------")
        print("\n\n")
        count+=1

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
        names.append(i['player']['summonerName'])
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


def get_champs_data():
    with open("champions.json", 'rb') as f:
        data =json.load(f)
    return data


from random import shuffle

def main():
    global p2
    champ_data = get_champs_data()

    names= [c['id'] for c in champ_data]
    keys = [c['key'] for c in champ_data]
    dict_data = dict(zip(keys, names))
    api_key= "RGAPI-92ec2123-7def-4140-a706-ab7a81cba5d0"
    print('[*] Wa hbibi register your region and name then you will be able to use the commands '+
    'below FOR\n\n[*] summoner_data user -D \n\n[*] spectate user -S\n\n[*] MatchHistory -H\n\n[*] Match By ID -M\n\n[*] Score -L\n\n[*] Play -P')



    region = input("Enter Region: ")


    name = input("Enter Summoner Name: ")


    command = input("Your Command: ")
    if command:
        print("Got ya!")
        if command.lower() == "-d":
            data = summoner_data(api_key,name,region)
            for key,value in zip(dict(data).keys(),dict(data).values()):
                print("{}: {}".format(key,value))
        elif command.lower() == "-s":
            id= request_id(api_key,name,region)
            print(id)
            count = 1
            names,champions_key =request_game_info(id,api_key,region)



            for i,champ in zip(names,champions_key):

                print("Player {} : {} // Champion : {}".format(count,i,champ))
                count += 1

        elif command.lower() == "check":
            p1 = input("Player 1: ")
            p2 = input("Player 2: ")
            id= request_id(api_key,name,region)
            names,champions_key =request_game_info(id,api_key,region)


            res = check_if_same(p1,p2,names)
            print(res)

        elif command.lower() == "-h":
            nmatches = int(input("Number of Matches to be Displayed: "))
            get_match_history(name,api_key,region,nmatches)
        elif command.lower() == "-m":

            data = get_match(name,api_key,region)

        elif command.lower() == "-l":
            p1 = input("Player 1: ")
            p2 = input("Player 2: ")
            p1_scores,p2_scores=get_match_kills(p1,p2,api_key,region)
            print("PLAYER 1 SCORE: {}\nPLAYER 2 SCORE: {}".format(p1_scores,p2_scores
            ))

        elif command.lower() == "-p":
            p1 = input("Enter Summoner Name: ")
            id= request_id(api_key,p1,region)
            print(id)
            names,champions_key =request_game_info(id,api_key,region)

            import random
            if p1 in names[5:]:
                p2 = random.choice(names[:5])
            elif p1 in names[:5]:
                p2=random.choice(names[5:])


            print(f"YOUR ENNEMIE IS {p2}")
            print("WAITING FOR MATCH TO CALCULATE YOUR SCORE , EXECUTE COMMAND -L WHEN YOU FNISH TO GET YOUR SCORES")






main()
