from django.contrib import admin
from .models import *

admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(EventSchedule)
admin.site.register(EventGallery)

admin.site.register(NewsArticle)
admin.site.register(PressRelease)

admin.site.register(Publication)
admin.site.register(Video)

admin.site.register(AwardCategory)
admin.site.register(AwardCriteria)
admin.site.register(PastWinner)

admin.site.register(TrainingProgram)
admin.site.register(TrainingModule)

admin.site.register(Partner)
admin.site.register(TeamMember)