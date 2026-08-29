from django.db import models

# Create your models here.

class Collections(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    artist = models.CharField(max_length=255, null=True, blank=True)
    art = models.ImageField(upload_to='arts/')  # 파일 저장 경로 설정
    created_at = models.DateTimeField(auto_now_add=True)
    onerscore = models.IntegerField(null=True, blank=True)
    aiscore = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name