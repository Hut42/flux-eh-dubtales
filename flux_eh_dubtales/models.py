from django_mysql.models import JSONField, Model

from django.db import models

from message_handler.models import BaseMessageModel


class DubtalesSubmission(Model, BaseMessageModel):

    message = JSONField()
    submitted = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Dubtales Submission"
        verbose_name_plural = "Dubtales Submissions"
