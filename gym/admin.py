from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Contact)
admin.site.register(Enquiry)
admin.site.register(Equipment)
admin.site.register(Member)
admin.site.register(Plan)



class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(Question , QuestionAdmin)
admin.site.register(Answer)



