from models import Team, Player, Change
from rest_framework import viewsets, mixins
from serializers import TeamSerializer, PlayerSerializer, ChangeSerializer, TeamChangeSerializer


# Create your views here.
class TeamViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        user = self.request.user
        return Team.objects.filter(user_id=user.id)


class PlayerViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.filter(team_id=self.kwargs['team_id'], team__user_id=self.request.user.id)


class ChangeViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Change.objects.all()
    serializer_class = ChangeSerializer

    def get_queryset(self):
        return Change.objects.filter(
            player_id=self.kwargs['player_id'],
            player__team__user_id=self.request.user.id
        ).order_by('-change_date')


class TeamChangeViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = Change.objects.all()
    serializer_class = TeamChangeSerializer

    def get_queryset(self):
        return Change.objects.filter(
            player__team_id=self.kwargs['team_id'],
            player__team__user_id=self.request.user.id
        ).order_by('-change_date')
