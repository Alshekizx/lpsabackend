from rest_framework.routers import DefaultRouter
from .views import (
    EventViewSet,
    NewsViewSet,
    PressReleaseViewSet,
    PublicationViewSet,
    VideoViewSet,
    AwardCategoryViewSet,
    PastWinnerViewSet,
    TrainingProgramViewSet,
    SpeakerViewSet,
    PartnerViewSet,
    TeamMemberViewSet,
    StatViewSet,
    RegistrationViewSet,
)

router = DefaultRouter()

router.register(r"events", EventViewSet)
router.register(r"news", NewsViewSet)
router.register(r"press-releases", PressReleaseViewSet)
router.register(r"publications", PublicationViewSet)
router.register(r"videos", VideoViewSet)
router.register(r"awards", AwardCategoryViewSet)
router.register(r"past-winners", PastWinnerViewSet)
router.register(r"training-programs", TrainingProgramViewSet)
router.register(r"speakers", SpeakerViewSet)
router.register(r"partners", PartnerViewSet)
router.register(r"team-members", TeamMemberViewSet)
router.register(r"stats", StatViewSet)
router.register(r"registrations", RegistrationViewSet)

urlpatterns = router.urls
