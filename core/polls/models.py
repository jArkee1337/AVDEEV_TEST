from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=250)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.DO_NOTHING, related_name='answers')
    answer_text = models.CharField(max_length=250)
    right_or_wrong = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class SetOfQuestions(models.Model):
    name_of_set = models.CharField(max_length=250)
    question = models.ManyToManyField('Question', related_name='collection')

    def __str__(self):
        return self.name_of_set
