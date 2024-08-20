from rest_framework import exceptions, serializers

from apps.complaints.models import Complaint


class ComplaintCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Complaint
        exclude = (
            'viewed',
        )

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if bool(attrs.get('station')) + bool(attrs.get('review')) != 1:
            raise exceptions.ValidationError('station or review must be 1')
        return attrs