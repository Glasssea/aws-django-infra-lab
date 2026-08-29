from django.db import models
import importlib
from django.core import validators

class Summoner_Info(models.Model):
    summonerId = models.CharField(primary_key=True, max_length=255)
    accountId = models.CharField(max_length=255)
    puuid = models.CharField(max_length=255)
    summonerName = models.CharField(max_length=255)
    profileIconId = models.IntegerField()
    revisionDate = models.BigIntegerField()
    summonerLevel = models.IntegerField()

class League_Info(models.Model):
    league_info_id = models.AutoField(primary_key=True)
    leagueId = models.CharField(max_length=255)
    queueType = models.CharField(max_length=255)
    tier = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    summonerName = models.CharField(max_length=255)
    leaguePoints = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    totalGames = models.IntegerField()
    winRate = models.FloatField()
    veteran = models.BooleanField()
    inactive = models.BooleanField()
    freshBlood = models.BooleanField()
    hotStreak = models.BooleanField()
    summonerId = models.ForeignKey(Summoner_Info, on_delete=models.SET_NULL, null=True, db_column='summonerId')

class Time_Info(models.Model):
    time_info_id = models.AutoField(primary_key=True)
    split_startTime = models.DateTimeField()
    currentTime = models.DateTimeField()
    split_startTime_unix = models.IntegerField()
    currentTime_unix = models.IntegerField()

class MatchId(models.Model):
    matchId = models.CharField(primary_key=True, max_length=255)

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    metadata = models.JSONField()
    info = models.JSONField()
    matchId = models.ForeignKey(MatchId, on_delete=models.SET_NULL, null=True, db_column='matchId')

class Match_Metadata(models.Model):
    match_metadata_id = models.AutoField(primary_key=True)
    dataVersion = models.CharField(max_length=50)
    participants = models.JSONField()
    matchId = models.ForeignKey(MatchId, on_delete=models.SET_NULL, null=True, db_column='matchId')
    match_id = models.ForeignKey(Match, on_delete=models.SET_NULL, null=True, db_column='match_id')

class Match_Info(models.Model):
    gameCreation = models.BigIntegerField()
    gameDuration = models.IntegerField()
    gameEndTimestamp = models.BigIntegerField()
    gameId = models.BigIntegerField(primary_key=True)
    gameMode = models.CharField(max_length=50)
    gameName = models.CharField(max_length=50)
    gameStartTimestamp = models.BigIntegerField()
    gameType = models.CharField(max_length=50)
    gameVersion = models.CharField(max_length=50)
    mapId = models.IntegerField()
    participants = models.JSONField()
    platformId = models.CharField(max_length=50)
    queueId = models.IntegerField()
    teams = models.JSONField()
    tournamentCode = models.CharField(max_length=50)
    matchId = models.ForeignKey(MatchId, on_delete=models.SET_NULL, null=True, db_column='matchId')
    match_id = models.ForeignKey(Match, on_delete=models.SET_NULL, null=True, db_column='match_id')

class SummonerId_MatchId(models.Model):
    summonerId_matchId_id = models.AutoField(primary_key=True)
    summonerId = models.ForeignKey(Summoner_Info, on_delete=models.SET_NULL, null=True, db_column='summonerId')
    matchId = models.ForeignKey(MatchId, on_delete=models.SET_NULL, null=True, db_column='matchId')
    gameCreation = models.BigIntegerField()

class League_Entries(models.Model):
    league_entries_id = models.AutoField(primary_key=True)
    leagueId = models.CharField(max_length=255)
    queueType = models.CharField(max_length=255)
    tier = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    summonerName = models.CharField(max_length=255)
    leaguePoints = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    totalGames = models.IntegerField()
    winRate = models.FloatField()
    veteran = models.BooleanField()
    inactive = models.BooleanField()
    freshBlood = models.BooleanField()
    hotStreak = models.BooleanField()
    miniSeries = models.JSONField(null=True)
    summonerId = models.CharField(max_length=255)

class Champion_Image(models.Model):
    champion_eng_name = models.CharField(primary_key=True, max_length=50)
    champion_kor_name = models.CharField(max_length=50)
    champion_icon_image = models.ImageField(upload_to='images/champion_icon/')

class Item_Image(models.Model):
    item_code = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_image = models.ImageField(upload_to='images/item/')

class Main_Perk_Image(models.Model):
    main_perk_id = models.IntegerField(primary_key=True)
    main_perk_name = models.CharField(max_length=255)
    main_perk_image = models.ImageField(upload_to='images/main_perk/')

class Sub_Perk_Image(models.Model):
    sub_perk_id = models.IntegerField(primary_key=True)
    sub_perk_name = models.CharField(max_length=255)
    sub_perk_image = models.ImageField(upload_to='images/sub_perk/')
    main_perk_id = models.ForeignKey(Main_Perk_Image, on_delete=models.SET_NULL, null=True, db_column='main_perk_id')

class Spell_Image(models.Model):
    spell_id = models.CharField(primary_key=True, max_length=50)
    spell_name = models.CharField(max_length=50)
    spell_key = models.CharField(max_length=3)
    spell_image = models.ImageField(upload_to='images/spell/')