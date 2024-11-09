from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework.response import Response

from . import permissions as pp
from . import models as pm
from . import serializers as ps


class AccountTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = pm.AccountType.objects.all()
    serializer_class = ps.AccountTypeSerializer
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        pass


class CardTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = pm.CardType.objects.all()
    serializer_class = ps.CardTypeSerializer
    permission_classes = [IsAuthenticated]


class TransactionTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = pm.TransactionType.objects.all()
    serializer_class = ps.TransactionTypeSerializer
    permission_classes = [IsAuthenticated]


class ProjectTypeViewSet(viewsets.ModelViewSet):
    queryset = pm.ProjectType.objects.all()
    serializer_class = ps.ProjectTypeSerializer
    permission_classes = [IsAuthenticated, pp.IsOwnerOrAdminReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(Q(owner=self.request.user) | Q(owner__is_superuser=True))

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
    permission_classes = [IsAuthenticated, pp.IsOwnerOrAdminReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(Q(owner=self.request.user) | Q(owner__is_superuser=True))


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = pm.Subcategory.objects.all()
    serializer_class = ps.SubcategorySerializer
    permission_classes = [IsAuthenticated, pp.IsOwnerOrAdminReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(Q(owner=self.request.user) | Q(owner__is_superuser=True))


class EntityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = pm.Entity.objects.all()
    serializer_class = ps.EntitySerializer
    permission_classes = [IsAuthenticated]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = pm.Customer.objects.all()
    serializer_class = ps.CustomerSerializer
    permission_classes = [IsAuthenticated, pp.IsOwnerOrAdminReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(owner=self.request.user)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = pm.Account.objects.all()
    serializer_class = ps.AccountSerializer
    permission_classes = [IsAuthenticated, pp.IsOwnerOrAdminReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(owner=self.request.user)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = pm.Project.objects.all()
    serializer_class = ps.ProjectSerializer
    permission_classes = [IsAuthenticated, pp.IsOwnerOrAdminReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(owner=self.request.user)


class CardViewSet(viewsets.ModelViewSet):
    queryset = pm.Card.objects.all()
    serializer_class = ps.CardSerializer
    permission_classes = [IsAuthenticated, pp.IsOwnerOrAdminReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(owner=self.request.user)


class TransactionViewSet(viewsets.GenericViewSet):
    queryset = pm.Transaction.objects.all()
    serializer_class = ps.TransactionSerializer
    permission_classes = [IsAuthenticated, pp.IsOwnerOrAdminReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(Q(owner=self.request.user) | Q(owner__is_superuser=True))

    def partial_update(self, request, *args, **kwargs):
        obj = self.get_object()

        obj.comment = request.data.get('comment', obj.comment)
        obj.transaction_type = pm.TransactionType.objects.get(id=request.data.get('transaction_type', obj.transaction_type))
        obj.subcategory = pm.Subcategory.objects.get(id=request.data.get('subcategory', obj.subcategory))
        obj.project = pm.Project.objects.get(id=request.data.get('project', obj.project))
        obj.save()

        serializer = self.get_serializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
