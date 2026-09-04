from django.shortcuts import render
from TRBT_main.models import Match_Info,Summoner_Info,League_Entries,Champion_Image,Item_Image,Main_Perk_Image,Sub_Perk_Image
from django.urls import reverse
from common.riot_api import (
    get_summonerInfo, leadue_v4__encryptedsummonerid, leadue_v4__bypuuid, masterty_SVD,
    get_mastery, point_ML, get_tagLine, account_v1__gamename_tagline, summoner_v4__encryptedpuuid,
    get_mastery_bypuuid, get_recent_matches, RiotIDNotFoundError, RiotAPIKeyError,
    RiotRateLimitError, RiotAPIError, InsufficientRecommendationDataError,
)
from common.championData import champion, DDRAGON_VERSION

ERROR_MESSAGES = {
    RiotIDNotFoundError: 'Riot ID를 찾을 수 없습니다.',
    RiotAPIKeyError: 'API Key 인증에 실패했습니다.',
    RiotRateLimitError: 'API 요청 제한에 걸렸습니다. 잠시 후 다시 시도해주세요.',
    InsufficientRecommendationDataError: '추천에 필요한 데이터가 부족합니다.',
}


def parse_riot_id(raw):
    """'gameName#tagLine' -> (gameName, tagLine), or None if malformed."""
    raw = (raw or '').strip()
    if '#' not in raw:
        return None
    gamename, _, tagline = raw.partition('#')
    gamename = gamename.strip()
    tagline = tagline.strip()
    if not gamename or not tagline:
        return None
    return gamename, tagline


def _find_queue_entry(league_entries, queue_type):
    entry = next((e for e in league_entries if e.get('queueType') == queue_type), None)
    if not entry:
        return None
    entry = dict(entry)
    wins, losses = entry.get('wins', 0), entry.get('losses', 0)
    entry['winRate'] = round((wins / (wins + losses)) * 100, 1) if (wins + losses) > 0 else None
    return entry


def run_svd_lookup(gamename, tagline):
    """Riot ID -> account/summoner/league/mastery lookups -> SVD recommendation.

    Raises RiotIDNotFoundError / RiotAPIKeyError / RiotRateLimitError /
    InsufficientRecommendationDataError (or RiotAPIError) on failure; callers
    render a friendly message for each instead of a 500.
    """
    account = account_v1__gamename_tagline(gamename, tagline)
    puuid = account['puuid']
    # summoner-v4 no longer returns "name"/"id" (encrypted summonerId), so
    # display name/tag comes from the account-v1 lookup above, and league
    # entries are looked up by puuid instead of the old encrypted id.
    summoner = summoner_v4__encryptedpuuid(puuid)
    league_entries = leadue_v4__bypuuid(puuid)
    solo = _find_queue_entry(league_entries, 'RANKED_SOLO_5x5')
    flex = _find_queue_entry(league_entries, 'RANKED_FLEX_SR')

    mastery_df = get_mastery_bypuuid(puuid)
    recommend_ids = point_ML(mastery_df, puuid)
    recommendations = [
        {'champion_id': champ_id, 'slug': champion.get(champ_id, str(champ_id))}
        for champ_id in recommend_ids
    ]

    # Recent matches are a lower priority than the SVD recommendation (see
    # task priorities) -- any failure here must never break the result above.
    try:
        recent_matches = get_recent_matches(puuid, count=5)
    except Exception:
        recent_matches = []

    return {
        'account': account,
        'summoner': summoner,
        'solo': solo,
        'flex': flex,
        'recommendations': recommendations,
        'recent_matches': recent_matches,
        'ddragon_version': DDRAGON_VERSION,
    }


# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        riot_id_input = request.POST.get('riot_id', '')
        context['riot_id_input'] = riot_id_input
        parsed = parse_riot_id(riot_id_input)
        if not parsed:
            context['error'] = "Riot ID 형식이 올바르지 않습니다. 예: Hide on bush#KR1"
        else:
            try:
                context.update(run_svd_lookup(*parsed))
            except tuple(ERROR_MESSAGES) as e:
                context['error'] = ERROR_MESSAGES[type(e)]
            except RiotAPIError:
                context['error'] = '외부 API에서 일시적인 오류가 발생했습니다. 잠시 후 다시 시도해주세요.'
    return render(request, 'search/searchpage.html', context)

def search(request,nickname=""):
    if request.method == 'POST':
        nickname = request.POST.get('searched')

    parsed = parse_riot_id(nickname)
    if not parsed:
        return render(request, 'search/searchpage.html', {'error': "Riot ID 형식이 올바르지 않습니다. 예: Hide on bush#KR1"})

    try:
        result = run_svd_lookup(*parsed)
    except tuple(ERROR_MESSAGES) as e:
        return render(request, 'search/searchpage.html', {'error': ERROR_MESSAGES[type(e)]})
    except RiotAPIError:
        return render(request, 'search/searchpage.html', {'error': '외부 API에서 일시적인 오류가 발생했습니다. 잠시 후 다시 시도해주세요.'})

    recommendations = result['recommendations']
    solo = result['solo']
    return render(request, 'search/search.html', {
        'info': result['summoner'],
        'gameName': result['account']['gameName'],
        'solo': solo,
        'free': result['flex'],
        'winrate': solo['winRate'] if solo else None,
        'tagLine': result['account']['tagLine'],
        'recommend_champ1': recommendations[0]['slug'],
        'recommend_champ2': recommendations[1]['slug'],
        'recommend_champ3': recommendations[2]['slug'],
    })

def ai(request, summonerName):
    pass
    # search/models.py -> database 구축(columns, 자료형(type)) 지정하는 Class 만들어주기
    # search/views.py -> database csv 넣어주는 식 하나 만들어주기(AWS hosting 되면 딱 한 번만 실행할 것)
    # api요청에 요청을 통해 받은 최종적인 dataframe을 database추가해주는데 중복(database에 있는 id를 검색한거라면 = if puuid 같을 때)되면 최신걸로 업데이트
