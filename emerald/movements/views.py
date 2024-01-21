from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from . import permissions as pp
from . import models as pm
from . import serializers as ps


class AccountTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = pm.AccountType.objects.all()
    serializer_class = ps.AccountTypeSerializer
    permission_classes = [IsAuthenticated]


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


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = pm.Transaction.objects.all()
    serializer_class = ps.TransactionSerializer
    permission_classes = [IsAuthenticated, pp.IsOwnerOrAdminReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(Q(owner=self.request.user) | Q(owner__is_superuser=True))
