from models import Team, Player
from rest_framework import viewsets, mixins
from serializers import TeamSerializer, PlayerSerializer

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
    queryset =  Team.objects.all()
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
        return Player.objects.filter(team_id=self.kwargs['team_id'])