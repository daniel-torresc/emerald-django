from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as pv


router = DefaultRouter()
# router.register(prefix=r'users', viewset=pv.UserViewSet, basename='user')
router.register(prefix=r'account-types', viewset=pv.AccountTypeViewSet, basename='account_type')


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
