from sklearn.decomposition import TruncatedSVD
import pandas as pd
import requests
from common.api_key import api_key
from common.championData import champion

def account_v1__gamename_tagline(gamename,tagline=None):
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gamename}/{tagline}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

def summoner_v4__encryptedpuuid(puuid):
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_summonerInfo(summonerName): # summonerName -> summonerId
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

# print(get_summonerInfo('troll bat').get('id'))


# 바뀐듯 아래껄로
# def leadue_v4__encryptedsummonerid(summonerId):
#     url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summonerId}"
#     headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
#     "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
#     "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Origin": "https://developer.riotgames.com",
#     "X-Riot-Token": api_key
# }
#     response = requests.get(url, headers=headers)
#     return response.json()
def leadue_v4__encryptedsummonerid(summonerId):
    url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summonerId}"
    headers = {
    
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}
    response = requests.get(url, headers=headers)
    return response.json()

def get_mastery_bypuuid(puuid):
    url = f"https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    df = pd.DataFrame(response.json())
    print(df.head())
    # df = df[['puuid','championId','championLevel','championPoints']] #puuid가 사라짐;;
    df = df[['puuid','championId','championLevel','championPoints']]
    print(df.head())

    to_add_puuid = df.loc[0]['puuid']
    try:
        exdf = pd.read_csv('common/mastery.csv')
    except FileNotFoundError:
        exdf = pd.read_csv('myportfolio/common/mastery.csv')
    exdf = exdf[exdf['puuid'] != to_add_puuid] #새로 추가하는 data가 이미 있는 유저의 데이터라면 그 유저에 대한 기존 데이터 다 삭제
    final_df = pd.concat([exdf, df])
    
    final_df.to_csv('mastery.csv', index=False)

    return final_df


def get_mastery(summonerId):#소환사 아이디로 마스터리 검색하고 검색해서 나온 숙련도 정보를 puuid 와 함께 csv 파일로 덮어써서 저장
    url = f"https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summonerId}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    df = pd.DataFrame(response.json())
    print(df.head())
    df = df[['puuid','championId','championLevel','championPoints']]
    print(df.head())

    to_add_puuid = df.loc[0]['puuid']
    exdf = pd.read_csv('common/mastery.csv')
    exdf = exdf[exdf['puuid'] != to_add_puuid] #새로 추가하는 data가 이미 있는 유저의 데이터라면 그 유저에 대한 기존 데이터 다 삭제
    final_df = pd.concat([exdf, df])
    final_df.to_csv('common/mastery.csv', index=False)
    return final_df
# df = get_mastery('5ypezW81tzdXWE5NwmHLoDBlZJXddWOnp9d2nN3BWc-dIns')
# print(df)

def point_ML(df, puuid): # 위에서 나온 dataframe으로 머신러닝 돌리는데 마지막에 추가된 puuid(소환사를 검색해주는 거임)
    df = df[['puuid', 'championId', 'championPoints']]
    duplicates = df.duplicated(subset=['puuid', 'championId'], keep=False)
    pivot_df = df.pivot(index='puuid', columns='championId', values='championPoints')
    fill_na_df = pivot_df.fillna(0) # fill na 를 한 dataframe 하나 만들어주기
    svd = TruncatedSVD(n_components=25) # 컴포넌트는 차원축소(164차원이었던 dataframe 을 25 차원으로 줄여줌)
    df_point_transformed = svd.fit_transform(fill_na_df) # fillnadf을 svd를 적용해서 차원 축소시켜줌 그걸 변수에저장
    df_point_transformed = pd.DataFrame(df_point_transformed, index=fill_na_df.index) # 학습시킨걸로 크기 줄여서 예측
    df_point_predicted = svd.inverse_transform(df_point_transformed) # 인버스 통해서 크기 차원축소 했던걸 원래대로 돌려줌
    df_point_predicted = pd.DataFrame(df_point_predicted, columns=fill_na_df.columns, index=fill_na_df.index) # 복원된 데이터를 dataframe으로변경시켜줌
    user = puuid
    for champion in pivot_df.columns: # 비어있는 곳만 예측한 값으로 채워줌
        if pd.isnull(pivot_df.loc[user, champion]):
            fill_na_df.loc[user, champion] = df_point_predicted.loc[user, champion]
        #데이터 손해로 임시 주석처리 정말 필요 없어도 주석으로 놔둘 예정
        for user in pivot_df.index:
            if pd.isnull(pivot_df.loc[user, champion]):
                fill_na_df.loc[user, champion] = df_point_predicted.loc[user, champion]
    recommendations = {} # 추천 시스템
    for user in fill_na_df.index:
        original_scores = pivot_df.loc[user]
        predicted_scores = fill_na_df.loc[user]
        
        # 원래 점수가 낮은 챔피언들 중에서 예측 점수가 높은 챔피언을 찾습니다.(3명만)
        # 처음 중앙값보다 낮은 챔피언 중에 높은거 추천
        low_original_high_predicted = predicted_scores[original_scores < original_scores.median()].nlargest(3)    
        # 해당 사용자에 대한 추천을 저장합니다.
        recommendations[user] = low_original_high_predicted.index.tolist()

    # 추천 결과를 출력합니다.
    print(recommendations.get(puuid)) # 
    return(recommendations.get(puuid))
    
    
# point_ML(df)

# input_nickname = '나쁜유저는없다'
# point_ML(get_mastery(get_summonerInfo(nickname).get('id')))


def masterty_SVD(nickname):
    info = get_summonerInfo(nickname)
    id = info.get('id')
    puuid = info.get('puuid')

    print(puuid)
    df = get_mastery(id)
    point_ML(df, puuid)

# masterty_SVD(input_nickname)


# 아이콘 이미지 링크 f'https://ddragon.leagueoflegends.com/cdn/13.17.1/img/profileicon/{}.png'
# iconid = info.get('name')
# iconid = info.get('profileIconId')
# level = info.get('summonerLevel')

# info = get_summonerInfo('trollbat')
# print(info.get('puuid'))

def get_matchId(puuid):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=100"
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    return response

def get_matchInfo(matchId):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
    } 
    response = requests.get(url, headers=headers)
    return response

def get_tagLine(puuid):
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

# print(get_tagLine("soerso-LMacN5eiMW2dqWEHA7br3adVNQgoDnotBXcOTFLBFBytjDTRO6JZAzhebWO8zlCebUGda-w"))

# 231220수요일에 riot developer 사이트 그대로 반영한 api로 수정중
# 방법은 왼쪽 탭에 있는 것을 큰 이름으로 하여 _추가해서 1,2,3,4 로 적어놓기
# 내용은 주석처리하여 확인할 수 있도록 함 그리고 돌려볼 수 있는 방법도 구성해놓기

def account_v1_1(puuid): #
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    print(response)
    return response.json()

