from django.contrib import admin
from message_handler.admin import JsonMessageHandlerAdmin, MessageHandlerResource
from message_handler.filters import JSONFieldFilter

from .models import DubtalesSubmission


class FormTypeFilter(JSONFieldFilter):
    model = DubtalesSubmission
    title = 'Form Type'
    parameter_name = 'form_type'


@admin.register(DubtalesSubmission)
class DubtalesSubmissionAdmin(JsonMessageHandlerAdmin):

    def form_type(self, obj):
        return obj.message.get('form_type', '')
    form_type.admin_order_field = 'message__form_type'

    def name(self, obj):
        return obj.message.get('form_name', '')
    name.admin_order_field = 'message__form_name'

    def email(self, obj):
        return obj.message.get('form_email', '')
    email.admin_order_field = 'message__form_email'

    def agree_terms(self, obj):
        return obj.message.get('form_terms', '')
    agree_terms.admin_order_field = 'message__form_terms'

    list_display = (
        'form_type',
        'name',
        'email',
        'agree_terms',
    )
    list_filter = (FormTypeFilter,)
