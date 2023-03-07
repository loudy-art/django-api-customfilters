from rest_framework import serializers
from api.models import Family, Crest, Image


class ImageSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Image
        fields = ('img_id', 'image_url')


class CrestSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Crest
        fields = ("crest_id", "name_id")


class BaseFamilySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    crests = CrestSerializer(many=True, read_only=True)

    class Meta:
        model = Family
        fields = (
            'name_id', 'name', 'clan', 'country', 'info',
            'last_update', 'has_content', 'condition', 'images', 'crests'
        )


class FamilySerializerHistory(BaseFamilySerializer):
    class Meta(BaseFamilySerializer.Meta):
        fields = BaseFamilySerializer.Meta.fields


class FamilySerializerProductsCrest(BaseFamilySerializer):
    class Meta(BaseFamilySerializer.Meta):
        fields = (
            'name_id', 'name', 'clan', 'country',
            'last_update', 'has_content', 'condition', 'images', 'crests'
        )


class FamilySerializerCrest(serializers.ModelSerializer):
    crests = CrestSerializer(many=True, read_only=True)

    class Meta:
        model = Family
        fields = (
            'name_id', 'name', 'clan', 'country',
            'last_update', 'has_content', 'condition', 'crests'
        )


class FamilySerializerProducts(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Family
        fields = (
            'name_id', 'name', 'clan', 'country',
            'last_update', 'has_content', 'condition', 'images'
        )


class FamilySerializerHistoryCrest(BaseFamilySerializer):
    class Meta(BaseFamilySerializer.Meta):
        fields = (
            'name_id', 'name', 'clan', 'country',
            'last_update', 'has_content', 'condition', 'info', 'crests'
        )


class FamilySerializerGeneral(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = (
            'name_id', 'name', 'clan', 'country',
            'last_update', '




########################################## ESTE ES EL QUE VA EL DE ACA ABAJO ES GOD


class FamilySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    crests = CrestSerializer(many=True, read_only=True)

    class Meta:
        model=Family
        fields=('name_id','name','clan','country',
                'last_update','has_content','condicion', 'images', 'crests')

    def __init__(self, *args, **kwargs):
        # access context variables passed from the view
        history = kwargs['context'].get('history', False)

        super().__init__(*args, **kwargs)

        # modify serializer fields based on the context variable
        if history:
            self.fields.pop('images')
            self.fields.pop('crests')



##########3

class FamilySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    crests = CrestSerializer(many=True, read_only=True)
    show_info = serializers.BooleanField(default=True, write_only=True)

    class Meta:
        model = Family
        fields = ('name_id', 'name', 'clan', 'country', 'last_update', 'has_content', 'condicion', 'images', 'crests', 'show_info')

    def __init__(self, instance=None, data=None, context={}):
        if 'history' in context and context['history']:
            self.fields.pop('images')
            self.fields.pop('crests')
            if 'show_info' in data:
                self.fields.pop('show_info')
        super().__init__(instance=instance, data=data, context=context)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'history' in self.context and self.context['history']:
            representation.pop('images', None)
            representation.pop('crests', None)
            if 'show_info' in self.validated_data:
                representation.pop('info', None)
        return representation

        

###################################
# 
# class FamilySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    crests = CrestSerializer(many=True, read_only=True)

    class Meta:
        model=Family
        fields=('name_id','name','clan','country',
                'last_update','has_content','condicion', 'images', 'crests')

    def __init__(self, *args, **kwargs):
        # access context variables passed from the view
        history = kwargs['context'].get('history', False)

        super().__init__(*args, **kwargs)

        # modify serializer fields based on the context variable
        if history:
            self.fields = {field_name: field for field_name, field in self.fields.items()
                           if field_name in ('name_id', 'name', 'clan', 'country', 'last_update',
                                             'has_content', 'condicion')}
        else:
            self.fields['images'] = ImageSerializer(many=True, read_only=True)
            self.fields['crests'] = CrestSerializer(many=True, read_only=True)
            
        return self.fields        