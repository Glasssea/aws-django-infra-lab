from common.riot_api import (
    account_v1__gamename_tagline,
    get_matchId,
    _riot_request,
)


def get_timeline(match_id):
    """
    Match-V5 Timeline API를 통해 한 경기의 타임라인 데이터를 가져옵니다.
    """
    url = (
        f"https://asia.api.riotgames.com/lol/match/v5/"
        f"matches/{match_id}/timeline"
    )

    # common.riot_api의 기존 요청/예외처리를 그대로 사용하기 위해
    # 기존 Riot API key를 가져옵니다.
    from common.api_key import api_key

    headers = {
        "X-Riot-Token": api_key
    }

    return _riot_request(url, headers)


def get_participant_id(timeline, puuid):
    """
    Timeline 데이터에서 해당 PUUID의 participantId를 찾습니다.
    """
    participants = timeline.get("metadata", {}).get("participants", [])

    try:
        return participants.index(puuid) + 1
    except ValueError:
        return None


def extract_deaths(timeline, participant_id, match_id):
    """
    CHAMPION_KILL 이벤트 중 현재 사용자가 victim인 이벤트만 추출합니다.
    """
    deaths = []

    frames = timeline.get("info", {}).get("frames", [])

    for frame in frames:
        for event in frame.get("events", []):

            if event.get("type") != "CHAMPION_KILL":
                continue

            if event.get("victimId") != participant_id:
                continue

            position = event.get("position")

            if not position:
                continue

            timestamp_ms = event.get("timestamp", 0)
            timestamp_minutes = round(timestamp_ms / 60000, 2)

            deaths.append({
                "match_id": match_id,
                "x": position.get("x"),
                "y": position.get("y"),
                "timestamp_ms": timestamp_ms,
                "minutes": timestamp_minutes,
            })

    return deaths


def analyze_deaths(game_name, tag_line, count=20):
    """
    Riot ID
        ↓
    PUUID
        ↓
    최근 경기 ID
        ↓
    각 경기 Timeline
        ↓
    사용자의 사망 이벤트 추출
    """

    # 안전장치
    count = int(count)

    if count not in (20, 50, 100):
        count = 20

    account = account_v1__gamename_tagline(game_name, tag_line)

    puuid = account["puuid"]

    match_ids = get_matchId(puuid, count=count)

    all_deaths = []
    analyzed_matches = 0

    for match_id in match_ids:

        timeline = get_timeline(match_id)

        participant_id = get_participant_id(timeline, puuid)

        if participant_id is None:
            continue

        deaths = extract_deaths(
            timeline,
            participant_id,
            match_id,
        )

        all_deaths.extend(deaths)

        analyzed_matches += 1

    average_deaths = (
        round(len(all_deaths) / analyzed_matches, 2)
        if analyzed_matches
        else 0
    )

    return {
        "account": account,
        "puuid": puuid,
        "requested_matches": count,
        "analyzed_matches": analyzed_matches,
        "total_deaths": len(all_deaths),
        "average_deaths": average_deaths,
        "deaths": all_deaths,
    }
