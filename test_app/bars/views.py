from .models import Bar
from .serializers import BarSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response


class BarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Bar.objects.all()
    serializer_class = BarSerializer

    def list(self, request):
        rating_gte = request.GET.get('rating_gte')
        if rating_gte:
            queryset = Bar.objects.filter(rating__gte=rating_gte)
        else:
            queryset = Bar.objects.order_by('updated_at')
        serializer = BarSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, 200)
