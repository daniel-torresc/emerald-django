from django.contrib import admin
from . import models as pm


@admin.register(pm.AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(pm.CardType)
class CardTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(pm.TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(pm.ProjectType)
class ProjectTypeAdmin(admin.ModelAdmin):
    model = pm.ProjectType

    fields = ('name', )


class SubcategoriesInline(admin.TabularInline):
    model = pm.Subcategory

    fields = ('logo', 'name')


@admin.register(pm.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('logo', 'name')

    inlines = [SubcategoriesInline]


@admin.register(pm.Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

    fields = ('logo', ('name', 'category'))


@admin.register(pm.Entity)
class EntityAdmin(admin.ModelAdmin):
    fields = ('logo', 'name')


@admin.register(pm.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone')

    fields = ('photo', ('first_name', 'last_name'), 'phone')


@admin.register(pm.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('iban', 'alias', 'entity', 'balance', 'display_customers')
    list_filter = ('entity', 'customers')

    fields = ('entity', ('alias', 'customers'), ('iban', 'balance', 'currency'), 'account_type')


@admin.register(pm.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_type')

    fields = (('name', 'project_type'), 'description')


@admin.register(pm.Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('alias', 'number', 'expiration_date', 'customer')
    list_filter = ('card_type', 'customer')

    fields = ('card_type', ('alias', 'customer', 'account'), ('number', 'expiration_date'))


@admin.register(pm.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('concept', 'amount', 'card', 'account', 'referenced_transaction')
    list_filter = ('operation_date', 'card', 'account', 'project')

    fieldsets = (
        (None, {
            'fields': ('referenced_transaction',)
        }),
        ('Main Info', {
            'fields': (('amount', 'concept'), ('operation_date', 'value_date'))
        }),
        ('Reference Info', {
            'fields': (('account', 'card'), )
        }),
        ('Tags', {
            'fields': (('transaction_type', 'subcategory', 'project'), )
        }),
        ('Additional Comments', {
            'fields': ('comment',)
        }),
    )
