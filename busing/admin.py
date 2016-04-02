from django.contrib import admin
from busing.models import Stop
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site


class stopsAdmin(admin.ModelAdmin):
	fields = ('id', 'shuttle', 'location', 'time_1', 'time_2', 'type_of_request', 'kind_of_stop', 'coord_x', 'coord_y', 'location_notes')
	list_display = ('id', 'shuttle', 'location', 'time_1', 'time_2', 'type_of_request', 'kind_of_stop', 'coord_x', 'coord_y', 'location_notes')
	list_filter = ['shuttle']
	ordering = ['id']


admin.site.register(Stop, stopsAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
