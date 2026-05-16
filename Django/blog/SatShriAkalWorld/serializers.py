from rest_framework import serializers
from SatShriAkalWorld.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id',
                  'title',
                  'content',
                  'created_on',
                  'updated_on',
                  'created_by',]


    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Post.objects.create(**validated_data)
