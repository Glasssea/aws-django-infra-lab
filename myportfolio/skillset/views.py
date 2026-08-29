from django.shortcuts import render,redirect
import base64
from django.core.files.base import ContentFile
from .models import Collections
from django.urls import reverse



# Create your views here.

def index(request):
    # 가장 최근에 추가된 3개의 그림을 가져옵니다.
    if Collections.objects.all():
        collections = Collections.objects.all()
        recent_collections = Collections.objects.all().order_by('-id')[:3]
    else:
        print('data empty')
        collections = ['none','none']
        recent_collections = []
        collection = 'none'
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        artist = data.get('artist')
        canvas_data = request.POST.get('myCanvasData', None)    
        # print(canvas_data)  # = 파일 정보
        if canvas_data is not None:
            format, imgstr = canvas_data.split(';base64,')
            ext = format.split('/')[-1]
            art = ContentFile(base64.b64decode(imgstr), name=f"temp.{ext}")

        

        # art 필드에 저장
        collection = Collections.objects.create(title=title, artist=artist, art=art)
        collection.save()
        return redirect(reverse('skillset:index',))
    
    return render(request, 'skillset/index.html', {'collections': collections, 'recent_collections': recent_collections})




