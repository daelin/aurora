from django.contrib import admin
from Stack.models import *
from django import forms

class StackForm(forms.ModelForm):
    class Meta:
        model = Stack
        exclude = []

    def clean(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date > end_date:
            raise forms.ValidationError('Start Date cannot be after End Date')
        return self.cleaned_data

class StackAdmin(admin.ModelAdmin):
    form = StackForm
    fieldsets = [
        (
            None, {
                'fields': [
                    'title',
                    'description',
                    'course',
                    'chapter',
                    'start_date',
                    'end_date',
                ]
            }
        ),
    ]
    list_display = ('id', 'title', 'description', 'course', 'start_date', 'end_date', )

class ChapterAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None, {
                'fields': [
                    'name',
                ]
            }
        ),
    ]
    list_display = ('name',)

admin.site.register(Stack, StackAdmin)
admin.site.register(Chapter, ChapterAdmin)
