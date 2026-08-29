from django.db import models

# Create your models here.



#Unnamed: 0,puuid,championId,championLevel,championPoints

class User_info(models.Model):
    puuid = models.CharField(primary_key=True, max_length=78)
    summonerId = models.CharField(max_length=80)
    summonerName = models.CharField(max_length=16)
    summonerLevel = models.IntegerField()
    profileIcon = models.IntegerField()
    revisionDate = models.BigIntegerField()
    accountId = models.CharField(max_length=80)
    

class Mastery(models.Model):
    id = models.AutoField(primary_key=True)
    puuid = models.CharField(max_length=78)
    championId = models.IntegerField()
    championLevel = models.IntegerField()
    championPoints = models.IntegerField()
    class Meta:
        unique_together = (('puuid', 'championId'),)

class ApiTimeline(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50) # 검색한 닉네임
    puuid = models.CharField(max_length=78)
    timestamp = models.DateTimeField(auto_now_add=True)
    request_kind = models.CharField(max_length=100) # 검색 종류

class Record(models.Model):
    id = models.AutoField(primary_key=True)
    puuid = models.CharField(max_length=78)
    recent_match_id = models.CharField(max_length=20)
    
    