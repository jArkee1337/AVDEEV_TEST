from django import forms
from django.contrib import admin
from .models import Answer, Question, SetOfQuestions


class AnswerInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        counter = 0
        try:
            for form in self.forms:
                if form.cleaned_data['right_or_wrong']:
                    counter += 1
            if counter < 1:
                raise forms.ValidationError('There must be one correct answer!')
            if counter == len(self.forms):
                raise forms.ValidationError("All answers cannot be correct!")
        except KeyError:
            pass


class AnswerInline(admin.TabularInline):
    formset = AnswerInlineFormset
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('collection', 'question_text',)
    list_display_links = ('collection',)
    list_editable = ('question_text',)
    search_fields = ['collection__name_of_set']
    inlines = [AnswerInline]


class SetOfQuestionsAdmin(admin.ModelAdmin):
    readonly_fields = ('right_answers',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(SetOfQuestions, SetOfQuestionsAdmin)
