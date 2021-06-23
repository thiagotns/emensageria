import xmltodict
from rest_framework.serializers import (
    ModelSerializer,
    JSONField,
    IntegerField,
    BooleanField,
    ChoiceField
)

from ..models import (
    Eventos,
)

from ..choices import EVENTO_ORIGEM_API, EVENTO_ORIGEM


class EventosSerializer(ModelSerializer):
    retorno_envio = JSONField(read_only=True)
    retorno_consulta = JSONField(read_only=True)
    ocorrencias = JSONField(read_only=True)

    def create(self, validated_data):
        validated_data['origem'] = EVENTO_ORIGEM_API
        validated_data['is_aberto'] = False
        if validated_data['evento_xml'] and not validated_data['evento_json']:
            import json
            dict = xmltodict.parse(validated_data['evento_xml'])
            validated_data['evento_json'] = json.dumps(dict.get('eSocial'))
        return Eventos.objects.create(**validated_data)

    class Meta:
        model = Eventos
        fields = '__all__'
        read_only_fields = (
            'tpamb',
            'procemi',
            'status',
            'transmissor_evento',
            'validacao_precedencia',
            'validacoes',
            'arquivo',
            'is_aberto',
            'origem',
            'transmissor_evento_error',
            'retorno_envio',
            'retorno_envio_json',
            'retorno_consulta',
            'retorno_consulta_json',
            'ocorrencias',
            'ocorrencias_json',
            'created_by',
        )
