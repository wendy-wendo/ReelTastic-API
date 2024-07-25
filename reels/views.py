from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ReelSerializer
from .models import Reel

# Create your views here.
@api_view(['GET'])
def index(request):
    apiUrls = {
        'ReelsList': '/list/',
        'Create Reel': '/create/',
        'Update Reel': '/update/' 
    }

    return Response(apiUrls)


@api_view(['GET'])
def reelsList(request):
    reels = Reel.objects.all()
    serializer = ReelSerializer(reels, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def reelCreate(request):
    serializer = ReelSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()


    return Response(serializer.data)


@api_view(['POST'])
def reelUpdate(request, pk):
    reel = Reel.objects.get(id=pk)
    serializer = ReelSerializer(instance=reel, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)