from rest_framework import serializers
from .models import User, Todo, Post, Album, Comment, Photo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):

        ret = super().to_representation(instance)
        ret['address'] = {
            'street': ret['street'],
            'suite': ret['suite'],
            'city': ret['city'],
            'zipcode': ret['zipcode'],
            'geo': {
                'lat': ret['lat'],
                'lng': ret['lng']
            }
        }
        ret['company'] = {
            'name': ret['company_name'],
            'catchPhrase': ret['company_catch_phrase'],
            'bs': ret['bs']
        }
        ret.pop('street')
        ret.pop('suite')
        ret.pop('city')
        ret.pop('lat')
        ret.pop('lng')
        ret.pop('company_name')
        ret.pop('company_catch_phrase')
        ret.pop('bs')

        return ret

    class Meta:
        model = User
        fields = '__all__'
