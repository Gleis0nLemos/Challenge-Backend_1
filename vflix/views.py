from rest_framework import viewsets
from vflix.models import Video
from vflix.serializer import VideoSerializer

class VideoViewSet(viewsets.ModelViewSet):
    """Viewsets for Video"""

    queryset = Video.objects.all()
    serializer_class = VideoSerializer

