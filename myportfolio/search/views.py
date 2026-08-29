from django.shortcuts import render
from TRBT_main.models import Match_Info,Summoner_Info,League_Entries,Champion_Image,Item_Image,Main_Perk_Image,Sub_Perk_Image
from django.urls import reverse
from common.riot_api import get_summonerInfo, leadue_v4__encryptedsummonerid, masterty_SVD, get_mastery, point_ML, get_tagLine, account_v1__gamename_tagline, summoner_v4__encryptedpuuid, get_mastery_bypuuid
from common.championData import champion

# #KR1 노출되게끔 수정함

# Create your views here.
def index(request):
    # match_info=Match_Info.objects.all()
    # # summoner_info = Summoner_Info.objects.get(summonerName='아이디가문제')
    # # summoner_rank = League_Entries.objects.get(summonerName='아이디가문제')
    # champion_image = Champion_Image.objects.all()
    # item_image = Item_Image.objects.all()
    # main_Perk_image = Main_Perk_Image.objects.all()
    # sub_Perk_image = Sub_Perk_Image.objects.all()
    return render(request, 'search/searchpage.html',
                   {
                #  'summoner_info':summoner_info, 
                #    'summoner_rank': summoner_rank, 
                    # 'level':level,
                #    'champion_image': champion_image, 
                #    'item_image':item_image, 
                #    'main_Perk_image':main_Perk_image,
                #    'sub_Perk_image':sub_Perk_image,
                #    'match_info':match_info
                   })

def search(request,nickname=""):
    if request.method == 'POST':
        nickname = request.POST.get('searched')
    else:
        pass

    # info = get_summonerInfo(nickname) #id뽑기 위한건데 gamename 이랑 tag가 달라져서
    # #을 기준으로 gamename과 tagline 나누기
    parts = nickname.split('#')
    gamename = parts[0].strip()
    tagline = parts[1].replace(' ','') if len(parts) > 1 else ''
    try:
        account_v1__gamename_tagline(gamename, tagline)['puuid']
    except KeyError:
        return render(request, 'search/searchpage.html', {'error': '일치하는 정보가 없습니다.'})
    puuid = account_v1__gamename_tagline(gamename, tagline)['puuid']
    info = summoner_v4__encryptedpuuid(puuid)
    leagueInfo = leadue_v4__encryptedsummonerid(info['id'])
    solo = leagueInfo[0]
    try:
        free = leagueInfo[1]
    except IndexError:
        free = None
    winrate = (solo.get('wins')/(solo.get('wins')+solo.get('losses')))*100
    winrate_rated = round(winrate, 1)
    puuid = info['puuid']
    df = get_mastery_bypuuid(puuid)
    recommend_champ = point_ML(df, puuid)
    champion_names = [champion[champ_id] for champ_id in recommend_champ]
    
    tagLine = get_tagLine(puuid)
    # 아이콘 이미지 링크 f'https://ddragon.leagueoflegends.com/cdn/13.17.1/img/profileicon/{}.png'
    # name = info.get('name')
    # iconid = info.get('profileIconId')
    # level = info.get('summonerLevel')

    # summoner_info = Summoner_Info.objects.get(summonerName=nickname)

    return render(request, 'search/search.html',{'info':info, 'solo':solo, 'free':free, 'winrate':winrate_rated, 'tagLine':tagLine, 'recommend_champ1':champion_names[0], 'recommend_champ2':champion_names[1], 'recommend_champ3':champion_names[2]})

def ai(request, summonerName):
    pass
    # search/models.py -> database 구축(columns, 자료형(type)) 지정하는 Class 만들어주기
    # search/views.py -> database csv 넣어주는 식 하나 만들어주기(AWS hosting 되면 딱 한 번만 실행할 것)
    # api요청에 요청을 통해 받은 최종적인 dataframe을 database추가해주는데 중복(database에 있는 id를 검색한거라면 = if puuid 같을 때)되면 최신걸로 업데이트

