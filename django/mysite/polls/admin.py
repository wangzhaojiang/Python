from django.contrib import admin
from polls.models import Poll
from polls.models import Choice
# Register your models here.

#admin.site.register(Poll)
#class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question']
#
#admin.site.register(Poll, PollAdmin)

#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 2


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Question',      {'fields' : ['question']}),
            ('Date information',    {'fields' : ['pub_date'], 'classes' : ['collapse']}),
            ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']


admin.site.register(Poll, PollAdmin)

admin.site.register(Choice)
