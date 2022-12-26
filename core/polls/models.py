from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=250)
    collection = models.ForeignKey('SetOfQuestions', on_delete=models.CASCADE, related_name='questions')

    def check_amount_of_right_answers(self):
        self.right_answers = 0
        for answer in self.answers.all():
            if answer.right_or_wrong:
                self.right_answers += 1
        return self.right_answers

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=250)
    right_or_wrong = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class SetOfQuestions(models.Model):
    name_of_set = models.CharField(max_length=250)
    right_answers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name_of_set
