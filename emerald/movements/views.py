from rest_framework import permissions, viewsets
from . import permissions as pp
from . import models as pm
from . import serializers as ps


class AccountTypeViewSet(viewsets.ModelViewSet):
    queryset = pm.AccountType.objects.all().order_by('name')
    serializer_class = ps.AccountTypeSerializer


class CardTypeViewSet(viewsets.ModelViewSet):
    queryset = pm.CardType.objects.all()
    serializer_class = ps.CardTypeSerializer


class TransactionTypeViewSet(viewsets.ModelViewSet):
    queryset = pm.TransactionType.objects.all()
    serializer_class = ps.TransactionTypeSerializer


class ProjectTypeViewSet(viewsets.ModelViewSet):
    queryset = pm.ProjectType.objects.all()
    serializer_class = ps.ProjectTypeSerializer
    permission_classes = [permissions.IsAdminUser, pp.IsOwner]

    # def get_queryset(self):
    #     if self.request.user.is_superuser:
    #         return self.queryset
    #
    #     owner = self.request.user
    #     return self.queryset.filter(owner=owner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def list(self, request):
    #     if not request.user.is_authenticated:
    #         return Response(data={}, status=status.HTTP_403_FORBIDDEN)
    #
    #     owner_id = request.user
    #
    #     if owner_id:
    #         self.queryset = self.queryset.filter(owner=owner_id)
    #
    #     serializer = ps.ProjectTypeSerializer(self.queryset, many=True)
    #     return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = pm.Category.objects.all()
    serializer_class = ps.CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = pm.Subcategory.objects.all()
    serializer_class = ps.SubcategorySerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = pm.Entity.objects.all()
    serializer_class = ps.EntitySerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = pm.Customer.objects.all()
    serializer_class = ps.CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AccountViewSet(viewsets.ModelViewSet):
    queryset = pm.Account.objects.all()
    serializer_class = ps.AccountSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = pm.Project.objects.all()
    serializer_class = ps.ProjectSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = pm.Card.objects.all()
    serializer_class = ps.CardSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = pm.Transaction.objects.all()
    serializer_class = ps.TransactionSerializer
