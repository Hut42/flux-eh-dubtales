from .models import DubtalesSubmission
from .serializers import DubtalesSubmissionSerializer

serializer_class = DubtalesSubmissionSerializer
queryset = DubtalesSubmission.objects.all()
