from django.shortcuts import render

from common.riot_api import (
    RiotIDNotFoundError,
    RiotAPIKeyError,
    RiotRateLimitError,
    RiotAPIError,
)

from .services.death_analysis import analyze_deaths


ERROR_MESSAGES = {
    RiotIDNotFoundError: "Riot ID를 찾을 수 없습니다.",
    RiotAPIKeyError: "API Key 인증에 실패했습니다.",
    RiotRateLimitError: "API 요청 제한에 걸렸습니다. 잠시 후 다시 시도해주세요.",
}


def parse_riot_id(raw):
    """
    'gameName#tagLine' 형식의 Riot ID를 분리합니다.
    """
    raw = (raw or "").strip()

    if "#" not in raw:
        return None

    game_name, _, tag_line = raw.partition("#")

    game_name = game_name.strip()
    tag_line = tag_line.strip()

    if not game_name or not tag_line:
        return None

    return game_name, tag_line


def index(request):
    context = {
        "selected_count": 20,
    }

    if request.method == "POST":
        riot_id_input = request.POST.get("riot_id", "").strip()
        count = 20
        context["riot_id_input"] = riot_id_input
        parsed = parse_riot_id(riot_id_input)

        if not parsed:
            context["error"] = (
                "Riot ID 형식이 올바르지 않습니다. "
                "예: Hide on bush#KR1"
            )
        else:
            try:
                context["result"] = analyze_deaths(
                    parsed[0],
                    parsed[1],
                    count=count,
                )

            except tuple(ERROR_MESSAGES) as e:
                context["error"] = ERROR_MESSAGES[type(e)]

            except RiotAPIError:
                context["error"] = (
                    "Riot API에서 일시적인 오류가 발생했습니다. "
                    "잠시 후 다시 시도해주세요."
                )

            except Exception:
                context["error"] = (
                    "분석 중 오류가 발생했습니다. "
                    "잠시 후 다시 시도해주세요."
                )

    return render(
        request,
        "where_you_die/index.html",
        context,
    )
