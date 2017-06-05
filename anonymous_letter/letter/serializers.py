from rest_framework import serializers

from letter.models import Letter


class LetterCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Letter
        fields = ('id', 'text', 'codeword')
        extra_kwargs = {
            'codeword': {'write_only': True},
        }

    def create(self, validated_data):
        letter = Letter.objects.create_letter(**validated_data)
        return letter


class LetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Letter
        fields = ('id', 'text', 'response')
        read_only_fields = ('text', )
