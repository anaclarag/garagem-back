from rest_framework.serializers import ModelSerializer

from core.models import Acessorio

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"