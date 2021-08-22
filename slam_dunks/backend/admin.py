from django.contrib import admin
from .models import User, Match, City, Team, Venue, School

# Register your models here.
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(City)
admin.site.register(School)
admin.site.register(Venue)
