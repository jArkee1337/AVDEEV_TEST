from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=250, verbose_name='Текст вопроса')
    collection = models.ForeignKey('SetOfQuestions',
                                   on_delete=models.CASCADE,
                                   related_name='questions',
                                   verbose_name='Набор'
                                   )

    def check_amount_of_right_answers(self):
        self.right_answers = 0
        for answer in self.answers.all():
            if answer.right_or_wrong:
                self.right_answers += 1
        return self.right_answers

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers', verbose_name='Вопрос')
    answer_text = models.CharField(max_length=250, verbose_name='Текст ответа')
    right_or_wrong = models.BooleanField(default=False, verbose_name='Верно')

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class SetOfQuestions(models.Model):
    name_of_set = models.CharField(max_length=250, verbose_name='Название набора')
    right_answers = models.PositiveIntegerField(default=0, verbose_name='Количество правильных ответов')

    def __str__(self):
        return self.name_of_set

    class Meta:
        verbose_name = 'Набор тестов'
        verbose_name_plural = 'Наборы тестов'
