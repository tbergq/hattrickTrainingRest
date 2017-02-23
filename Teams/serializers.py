from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Team
from Account.serializers import UserSerializer


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
