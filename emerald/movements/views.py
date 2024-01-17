from rest_framework import generics, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from . import permissions as pp
from . import models as pm
from . import serializers as ps


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = ps.UserSerializer


class AccountTypeViewSet(viewsets.ModelViewSet):
    queryset = pm.AccountType.objects.all().order_by('account_type_name')
    serializer_class = ps.AccountTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class GetAccountTypeView(APIView):
#     serializer_class = ps.AccountTypeSerializer
#     lookup_url_kwarg = 'id'
#
#     def get(self, request, format=None):
#         account_type_id = request.GET.get(self.lookup_url_kwarg)
#         if account_type_id:
#             account_type = pm.AccountType.objects.filter(id=account_type_id)
#             if len(account_type) > 0:
#                 data = ps.AccountTypeSerializer(account_type[0]).data
#                 return Response(data=data, status=status.HTTP_200_OK)
#             return Response(data={'Account Type not found': 'Invalid Account Type'}, status=status.HTTP_404_NOT_FOUND)
#
#         return Response(data={'Bad Request': 'Id not found'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CreateAccountTypeView(APIView):
#     serializer_class = ps.CreateAccountTypeSerializer
#
#     def post(self, request, format=None):
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()
#
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             account_type_name = serializer.data.get('account_type_name')
#
#             account_type = pm.AccountType(account_type_name=account_type_name)
#             account_type.save()
#
#             return Response(ps.AccountTypeSerializer(account_type).data, status=status.HTTP_201_CREATED)


class CardTypeView(generics.ListCreateAPIView):
    queryset = pm.CardType.objects.all()
    serializer_class = ps.CardTypeSerializer


class TransactionTypeView(generics.ListCreateAPIView):
    queryset = pm.TransactionType.objects.all()
    serializer_class = ps.TransactionTypeSerializer


class ProjectTypeView(generics.ListCreateAPIView):
    queryset = pm.ProjectType.objects.all()
    serializer_class = ps.ProjectTypeSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = pm.Category.objects.all()
    serializer_class = ps.CategorySerializer


class SubcategoryView(generics.ListCreateAPIView):
    queryset = pm.Subcategory.objects.all()
    serializer_class = ps.SubcategorySerializer


class EntityView(generics.ListCreateAPIView):
    queryset = pm.Entity.objects.all()
    serializer_class = ps.EntitySerializer


class CustomerView(generics.ListCreateAPIView):
    queryset = pm.Customer.objects.all()
    serializer_class = ps.CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AccountView(generics.ListCreateAPIView):
    queryset = pm.Account.objects.all()
    serializer_class = ps.AccountSerializer


class ProjectView(generics.ListCreateAPIView):
    queryset = pm.Project.objects.all()
    serializer_class = ps.ProjectSerializer


class CardView(generics.ListCreateAPIView):
    queryset = pm.Card.objects.all()
    serializer_class = ps.CardSerializer


class TransactionView(generics.ListCreateAPIView):
    queryset = pm.Transaction.objects.all()
    serializer_class = ps.TransactionSerializer
