from rest_framework import serializers
from .models import *


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = "__all__"


class EventScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSchedule
        fields = "__all__"


class EventGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventGallery
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    speakers = SpeakerSerializer(many=True, read_only=True)
    schedule = EventScheduleSerializer(many=True, read_only=True)
    gallery = EventGallerySerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = "__all__"


class PressReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressRelease
        fields = "__all__"


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class AwardCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardCriteria
        fields = "__all__"


class AwardCategorySerializer(serializers.ModelSerializer):
    criteria = AwardCriteriaSerializer(many=True, read_only=True)

    class Meta:
        model = AwardCategory
        fields = "__all__"


class PastWinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastWinner
        fields = "__all__"


class TrainingModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingModule
        fields = "__all__"


class TrainingProgramSerializer(serializers.ModelSerializer):
    modules = TrainingModuleSerializer(many=True, read_only=True)

    class Meta:
        model = TrainingProgram
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = "__all__"


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    event = serializers.SlugRelatedField(slug_field="id_slug", queryset=Event.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Registration
        fields = "__all__"