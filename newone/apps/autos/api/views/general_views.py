from apps.autos.api.serializers.general_serializers import CategorySerializer,ImportationSerializer

from apps.base.api  import GeneralListAPIView

class CategoryListAPIVIew(GeneralListAPIView):
    serializer_class = CategorySerializer

class ImportationLisAPIVIew(GeneralListAPIView):
    serializer_class = ImportationSerializer
    

