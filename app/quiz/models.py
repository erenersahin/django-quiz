from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['id']


class Quiz(models.Model):
    category = models.name = models.ForeignKey(
        'Category', related_name='quiz', on_delete=models.DO_NOTHING, default=1)
    title = models.CharField(max_length=255,
                             default=_("New Quiz"), verbose_name=_("Quiz Title"))
    created_time = models.DateTimeField(_("Created Time"), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']


class Updated(models.Model):
    updated_time = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):
    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (3, _('Expert'))
    )

    TYPE = (
        (0, _('Multiple Choice')),
    )

    quiz = models.name = models.ForeignKey(
        'Quiz', related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(
        choices=TYPE, default=0, verbose_name=_("Type of Question"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty = models.IntegerField(
        choices=SCALE, default=0, verbose_name=_("Difficulty"))
    created_time = models.DateTimeField(_("Created Time"), auto_now_add=True)
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    def __str__(self):
        return self.title


class Answer(Updated):
    question = models.name = models.ForeignKey(
        'Question', related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(
        max_length=255, verbose_name=_("Answer Text"))
    is_correct = models.BooleanField(
        default=False, verbose_name=_("Correct Status"))

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']
