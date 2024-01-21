from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as pv


router = DefaultRouter()
router.register(prefix=r'account-types', viewset=pv.AccountTypeViewSet, basename='account_type')
router.register(prefix=r'card-types', viewset=pv.CardTypeViewSet, basename='card_type')
router.register(prefix=r'transaction-types', viewset=pv.TransactionTypeViewSet, basename='transaction_type')
router.register(prefix=r'project-types', viewset=pv.ProjectTypeViewSet, basename='project_type')
router.register(prefix=r'categories', viewset=pv.CategoryViewSet, basename='category')
router.register(prefix=r'subcategories', viewset=pv.SubcategoryViewSet, basename='subcategory')
router.register(prefix=r'entities', viewset=pv.EntityViewSet, basename='entity')
router.register(prefix=r'customers', viewset=pv.CustomerViewSet, basename='customer')
router.register(prefix=r'accounts', viewset=pv.AccountViewSet, basename='account')
router.register(prefix=r'projects', viewset=pv.ProjectViewSet, basename='project')
router.register(prefix=r'cards', viewset=pv.CardViewSet, basename='card')
router.register(prefix=r'transactions', viewset=pv.TransactionViewSet, basename='transaction')


urlpatterns = [
    path(route='', view=include(router.urls))
]
