from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as pv


router = DefaultRouter()
# router.register(prefix=r'users', viewset=pv.UserViewSet, basename='user')
router.register(prefix=r'account-types', viewset=pv.AccountTypeViewSet, basename='account_type')
router.register(prefix=r'card-types', viewset=pv.CardTypeViewSet, basename='card_type')
router.register(prefix=r'transaction-types', viewset=pv.TransactionTypeViewSet, basename='transaction_type')
router.register(prefix=r'project-types', viewset=pv.ProjectTypeViewSet, basename='project_type')
router.register(prefix=r'categories', viewset=pv.CategoryViewSet, basename='category')
router.register(prefix=r'subcategories', viewset=pv.SubcategoryViewSet, basename='subcategory')
router.register(prefix=r'entities', viewset=pv.EntityViewSet, basename='entity')
router.register(prefix=r'customers', viewset=pv.CustomerViewSet, basename='customer')
router.register(prefix=r'accounts', viewset=pv.AccountViewSet, basename='account')
router.register(prefix=r'cards', viewset=pv.CardViewSet, basename='card')
router.register(prefix=r'transactions', viewset=pv.TransactionViewSet, basename='transaction')


urlpatterns = [
    path(route='', view=include(router.urls))
    # path(route="account-types/", view=pv.AccountTypeListView.as_view(),     name='account_type'),
    # path(route="card-types/",            view=pv.CardTypeView.as_view(),              name='card_type'),
    # path(route="transaction-types/",     view=pv.TransactionTypeView.as_view(),       name='transaction_type'),
    # path(route="project-types/",         view=pv.ProjectTypeView.as_view(),           name='project_type'),
    # path(route="categories/",            view=pv.CategoryView.as_view(),              name='category'),
    # path(route="subcategories/",         view=pv.SubcategoryView.as_view(),           name='subcategory'),
    # path(route="entities/",              view=pv.EntityView.as_view(),                name='entity'),
    # path(route="customers/",             view=pv.CustomerView.as_view(),              name='customer'),
    # path(route="accounts/",              view=pv.AccountView.as_view(),               name='account'),
    # path(route="projects/",              view=pv.ProjectView.as_view(),               name='project'),
    # path(route="cards/",                 view=pv.CardView.as_view(),                  name='card'),
    # path(route="transactions/",          view=pv.TransactionView.as_view(),           name='transaction'),
]
