from rest_framework import serializers
from models import Team, Player, Change


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('url', 'team_name', 'hattrick_team_id', 'id')

    def create(self, validated_data):
        print "create"
        user = self.context['request'].user
        team = Team.objects.create(user_id=user.id, **validated_data)
        print validated_data
        return team


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class ChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Change
        fields = '__all__'

class TeamChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Change
        fields = '__all__'
        depth = 1