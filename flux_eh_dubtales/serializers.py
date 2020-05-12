import logging

from django.conf import settings

from instiller import InstillerApi

from message_handler.serializers import BaseMessageHandlerSerializer
from .models import DubtalesSubmission
from . import metadata

logger = logging.getLogger(__name__)


class DubtalesSubmissionSerializer(BaseMessageHandlerSerializer):

    class Meta:
        model = DubtalesSubmission
        fields = (
            'message',
        )
        extra_kwargs = {
            'message': {'write_only': True},
        }

    def post_create(self, obj):
        if obj.message.get('form_type') == metadata.FORM_TYPE_NEWSLETTER:
            api_keys = settings.INSTILLER_API_KEYS.get('Dubtales_Mstr')
            if api_keys:
                instiller = InstillerApi(
                    settings.INSTILLER_API_URL,
                    api_keys.get('api_id'),
                    api_keys.get('api_key')
                )
                try:
                    email_address = obj.message.get('form_email')
                    if email_address:
                        obj.post_create_output = instiller.automation_trigger_workflow(
                            'dubtales_dbl_oi',
                            email_address,
                        )
                except Exception as e:
                    logger.error(f"Instiller lists_subscribe_user error {e}")
        return obj
