from django.contrib import admin
from .models import (AccountType, CardType, TransactionType, ProjectType, Category, Subcategory, Entity, Customer,
                     Account, Project, Card, Transaction)


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(CardType)
class CardTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectType)
class ProjectTypeAdmin(admin.ModelAdmin):
    pass


class SubcategoriesInline(admin.TabularInline):
    model = Subcategory

    fields = ('subcategory_logo', 'subcategory_name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('category_logo', 'category_name')

    inlines = [SubcategoriesInline]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory_name', 'category')

    fields = ('subcategory_logo', ('subcategory_name', 'category'))


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    fields = ('entity_logo', 'entity_name')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone')

    fields = ('photo', ('first_name', 'last_name'), 'phone')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('iban', 'account_alias', 'entity', 'balance', 'display_customers')
    list_filter = ('entity', 'customers')

    fields = ('entity', ('account_alias', 'customers'), ('iban', 'balance', 'currency'), 'account_type')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_type')

    fields = (('project_name', 'project_type'), 'project_description')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('card_alias', 'card_number', 'expiration_date', 'customer')
    list_filter = ('card_type', 'customer')

    fields = ('card_type', ('card_alias', 'customer', 'account'), ('card_number', 'expiration_date'))


@admin.register(Transaction)
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
            'fields': ('transaction_comment',)
        }),
    )
