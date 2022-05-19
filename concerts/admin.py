from django.contrib import admin

# Register your models here.
from concerts.models import Concert,  Song


class ConcertAdmin(admin.ModelAdmin):
    pass
class SongAdmin(admin.ModelAdmin):
    pass

admin.site.register(Concert, ConcertAdmin)
admin.site.register(Song, SongAdmin)

