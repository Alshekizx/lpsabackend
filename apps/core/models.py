from django.db import models


# -----------------------
# SPEAKER
# -----------------------
class Speaker(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


# -----------------------
# EVENT
# -----------------------
class Event(models.Model):
    STATUS = (
        ("upcoming", "Upcoming"),
        ("past", "Past"),
    )

    id_slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS)
    image = models.URLField()
    full_description = models.TextField()
    brochure = models.FileField(upload_to="event_brochures/", blank=True, null=True)
    registration_url = models.URLField(blank=True)
    embed_code = models.TextField(blank=True)

    speakers = models.ManyToManyField(Speaker, blank=True)

    def __str__(self):
        return self.title


class EventSchedule(models.Model):
    event = models.ForeignKey(Event, related_name="schedule", on_delete=models.CASCADE)
    time = models.TimeField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class EventGallery(models.Model):
    event = models.ForeignKey(Event, related_name="gallery", on_delete=models.CASCADE)
    image = models.URLField()


# -----------------------
# NEWS
# -----------------------
class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    category = models.CharField(max_length=100)
    image = models.URLField()
    excerpt = models.TextField()
    content = models.TextField()


# -----------------------
# PRESS RELEASE
# -----------------------
class PressRelease(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    excerpt = models.TextField()


# -----------------------
# PUBLICATION
# -----------------------
class Publication(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    type = models.CharField(max_length=100)
    pages = models.IntegerField()
    download_url = models.URLField()
    image = models.URLField()
    content = models.TextField(blank=True)
    author = models.CharField(max_length=255, blank=True)


# -----------------------
# VIDEO
# -----------------------
class Video(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    duration = models.CharField(max_length=20)
    thumbnail = models.URLField()
    video_url = models.URLField()
    description = models.TextField()


# -----------------------
# AWARDS
# -----------------------
class AwardCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class AwardCriteria(models.Model):
    category = models.ForeignKey(AwardCategory, related_name="criteria", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)


class PastWinner(models.Model):
    year = models.IntegerField()
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.URLField()
    achievement = models.TextField()


# -----------------------
# TRAINING
# -----------------------
class TrainingProgram(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)
    format = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    image = models.URLField()
    description = models.TextField()
    next_intake = models.DateField()


class TrainingModule(models.Model):
    program = models.ForeignKey(TrainingProgram, related_name="modules", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


# -----------------------
# TEAM / PARTNERS
# -----------------------
class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.URLField()


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.URLField()
    bio = models.TextField()



class Stat(models.Model):
    value = models.CharField(max_length=50)
    label = models.CharField(max_length=255)


# -----------------------
# REGISTRATIONS
# -----------------------
class Registration(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    organization = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100, blank=True)
    event = models.ForeignKey(Event, related_name="registrations", on_delete=models.SET_NULL, null=True, blank=True)
    ticket_type = models.CharField(max_length=100, blank=True)
    dietary_requirements = models.TextField(blank=True)
    accessibility = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"