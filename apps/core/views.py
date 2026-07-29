from rest_framework import viewsets
from .models import *
from .serializers import *


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("-date")
    serializer_class = EventSerializer


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = "__all__"


class NewsViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all().order_by("-date")
    serializer_class = NewsSerializer

class PressReleaseViewSet(viewsets.ModelViewSet):
    queryset = PressRelease.objects.all().order_by("-date")
    serializer_class = PressReleaseSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all().order_by("-date")
    serializer_class = PublicationSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by("-date")
    serializer_class = VideoSerializer


class AwardCategoryViewSet(viewsets.ModelViewSet):
    queryset = AwardCategory.objects.all()
    serializer_class = AwardCategorySerializer


class PastWinnerViewSet(viewsets.ModelViewSet):
    queryset = PastWinner.objects.all().order_by("-year")
    serializer_class = PastWinnerSerializer


class TrainingProgramViewSet(viewsets.ModelViewSet):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all().order_by("-created_at")
    serializer_class = RegistrationSerializer