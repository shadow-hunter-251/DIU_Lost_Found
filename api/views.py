from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from items.models import Item

from .serializers import ItemSerializer


def require_authentication(request):

    if not request.user.is_authenticated:

        return Response(
            {
                'detail': 'Authentication required.'
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    return None


class ItemListAPIView(APIView):

    def get_permissions(self):

        if self.request.method == 'POST':

            return [IsAuthenticated()]

        return [AllowAny()]

    def get(self, request):

        items = Item.objects.filter(
            status='ACTIVE'
        ).select_related(
            'category',
            'user'
        )

        item_type = request.GET.get('type')

        if item_type in ['LOST', 'FOUND']:

            items = items.filter(
                item_type=item_type
            )

        serializer = ItemSerializer(
            items,
            many=True,
            context={
                'request': request
            }
        )

        return Response(
            serializer.data
        )

    def post(self, request):

        serializer = ItemSerializer(
            data=request.data,
            context={
                'request': request
            }
        )

        if serializer.is_valid():

            item = serializer.save(
                user=request.user
            )

            return Response(
                ItemSerializer(
                    item,
                    context={
                        'request': request
                    }
                ).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ItemDetailAPIView(APIView):

    def get_permissions(self):

        if self.request.method in [
            'PUT',
            'PATCH',
            'DELETE'
        ]:

            return [IsAuthenticated()]

        return [AllowAny()]

    def get_object(self, item_id):

        try:

            return Item.objects.get(
                id=item_id
            )

        except Item.DoesNotExist:

            return None

    def get(self, request, item_id):

        item = self.get_object(item_id)

        if item is None:

            return Response(
                {
                    'detail': 'Item not found.'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ItemSerializer(
            item,
            context={
                'request': request
            }
        )

        return Response(
            serializer.data
        )

    def put(self, request, item_id):

        authentication_error = require_authentication(
            request
        )

        if authentication_error:

            return authentication_error

        item = self.get_object(item_id)

        if item is None:

            return Response(
                {
                    'detail': 'Item not found.'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if item.user != request.user:

            return Response(
                {
                    'detail': 'You can only edit your own items.'
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = ItemSerializer(
            item,
            data=request.data,
            context={
                'request': request
            }
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, item_id):

        authentication_error = require_authentication(
            request
        )

        if authentication_error:

            return authentication_error

        item = self.get_object(item_id)

        if item is None:

            return Response(
                {
                    'detail': 'Item not found.'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if item.user != request.user:

            return Response(
                {
                    'detail': 'You can only edit your own items.'
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = ItemSerializer(
            item,
            data=request.data,
            partial=True,
            context={
                'request': request
            }
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, item_id):

        authentication_error = require_authentication(
            request
        )

        if authentication_error:

            return authentication_error

        item = self.get_object(item_id)

        if item is None:

            return Response(
                {
                    'detail': 'Item not found.'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if item.user != request.user:

            return Response(
                {
                    'detail': 'You can only delete your own items.'
                },
                status=status.HTTP_403_FORBIDDEN
            )

        item.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )