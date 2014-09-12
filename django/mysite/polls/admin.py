from django.contrib import admin
from polls.models import Poll
# Register your models here.

#admin.site.register(Poll)
class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)
