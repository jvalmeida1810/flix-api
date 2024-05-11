from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie

    
class MovieModelSeriealizer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        
        if rate:
            return round(rate, 1)

        return None
        
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('Filmes com data inferior a 1915 não podem ser cadastrados.')
        return value
    
    def validate_description(self, value):
        if len(value) > 600:
            raise serializers.ValidationError('O campo de descrição não pode ser maior do que 200 caracteres')
        return value