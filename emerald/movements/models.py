from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


class AccountType(models.Model):
    # Fields
    account_type_name = models.CharField(max_length=20,
                                         unique=True,
                                         help_text="Enter the type of account (savings, investing, etc.)")
    owner = models.ForeignKey('auth.User', related_name='account_types', on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['account_type_name']

    # Methods
    def get_absolute_url(self):
        """ Returns the URL to access a particular instance. """
        return reverse(viewname='account-type-detail', args=[str(self.id)])

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.account_type_name


class CardType(models.Model):
    # Fields
    card_type_name = models.CharField(max_length=10,
                                      unique=True,
                                      help_text="Enter the type of card (debit, credit, etc.)")

    # Metadata
    class Meta:
        ordering = ['card_type_name']

    # Methods
    def get_absolute_url(self):
        """ Returns the URL to access a particular instance. """
        return reverse(viewname='card-type-detail', args=[str(self.id)])

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.card_type_name


class TransactionType(models.Model):
    # Fields
    transaction_type_name = models.CharField(max_length=50,
                                             unique=True,
                                             help_text="Enter the type of transaction (income, expense, etc.)")

    # Metadata
    class Meta:
        ordering = ['transaction_type_name']

    # Methods
    def get_absolute_url(self):
        """ Returns the URL to access a particular instance. """
        return reverse(viewname='transaction-type-detail', args=[str(self.id)])

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.transaction_type_name


class ProjectType(models.Model):
    # Fields
    project_type_name = models.CharField(max_length=20,
                                         unique=True,
                                         help_text="Enter the type of project (trip, vacation, etc.)")

    # Metadata
    class Meta:
        ordering = ['project_type_name']

    # Methods
    def get_absolute_url(self):
        """ Returns the URL to access a particular instance. """
        return reverse(viewname='project-type-detail', args=[str(self.id)])

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.project_type_name


class Category(models.Model):
    # Fields
    category_name = models.CharField(max_length=50,
                                     unique=True,
                                     help_text="Enter a category (restaurant, transport, etc.)")
    category_logo = models.ImageField(help_text="Upload category logo",
                                      unique=False, null=True, blank=True, verbose_name='Logo')

    # Metadata
    class Meta:
        ordering = ['category_name']
        verbose_name_plural = "categories"

    # Methods
    def get_absolute_url(self):
        """ Returns the URL to access a particular instance. """
        return reverse(viewname='category-detail', args=[str(self.id)])

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.category_name


class Subcategory(models.Model):
    # Fields
    subcategory_name = models.CharField(max_length=50,
                                        unique=True,
                                        help_text="Enter a subcategory")
    subcategory_logo = models.ImageField(help_text="Upload subcategory logo",
                                         unique=False, null=True, blank=True, verbose_name='Logo')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=False)

    # Metadata
    class Meta:
        # ordering = ['subcategory_name']
        verbose_name_plural = "subcategories"
        order_with_respect_to = "category"

    # Methods
    def get_absolute_url(self):
        """ Returns the URL to access a particular instance. """
        return reverse(viewname='subcategory-detail', args=[str(self.id)])

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.subcategory_name


class Entity(models.Model):
    # Fields
    entity_name = models.CharField(max_length=50,
                                   unique=True,
                                   help_text="Enter entity name")
    entity_logo = models.ImageField(help_text="Upload entity logo",
                                    unique=False, null=True, blank=True, verbose_name='Logo')

    # Metadata
    class Meta:
        ordering = ['entity_name']
        verbose_name_plural = "entities"

    # Methods
    def get_absolute_url(self):
        """ Returns the URL to access a particular instance. """
        return reverse(viewname='entity-detail', args=[str(self.id)])

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.entity_name


class Customer(models.Model):
    # Fields
    first_name = models.CharField(max_length=50,
                                  unique=False,
                                  help_text="Enter your name")
    last_name = models.CharField(max_length=50,
                                 unique=False,
                                 help_text="Enter your last name")
    phone = models.CharField(max_length=20,
                             unique=True,
                             help_text="Enter your phone number")
    photo = models.ImageField(help_text="Enter your photo", null=True, blank=True)

    # Metadata
    class Meta:
        ordering = ['first_name', 'last_name']

    # Methods
    def get_absolute_url(self):
        """ Returns the URL to access a particular instance. """
        return reverse(viewname='customer-detail', args=[str(self.id)])

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return f"{self.first_name} {self.last_name}"


class Account(models.Model):
    # Fields
    iban = models.CharField(max_length=24,
                            unique=True,
                            null=False,
                            help_text="Enter account IBAN",
                            verbose_name="IBAN")
    account_alias = models.CharField(max_length=20,
                                     unique=False,
                                     null=True, blank=True,
                                     help_text="Enter account alias")
    balance = models.FloatField()
    currency = models.CharField(max_length=3,
                                unique=False,
                                null=False,
                                help_text="Enter account currency")
    account_type = models.ForeignKey("AccountType", on_delete=models.RESTRICT, null=False)
    entity = models.ForeignKey("Entity", on_delete=models.RESTRICT, null=False)
    customers = models.ManyToManyField("Customer")

    # Metadata
    class Meta:
        ordering = []

    # Methods
    def get_absolute_url(self):
        """ Returns the URL to access a particular instance. """
        return reverse(viewname='account-detail', args=[str(self.id)])

    def display_customers(self):
        """ This is required to display customers in Admin """
        return ', '.join(str(customer) for customer in self.customers.all()[:3])
    display_customers.short_description = 'Customers'

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return f"{self.iban} - {self.account_alias}" if self.account_alias else self.iban


class Project(models.Model):
    # Fields
    project_name = models.CharField(max_length=50,
                                    unique=False,
                                    help_text="Enter project name")
    project_description = models.TextField(help_text="Enter project description", null=True, blank=True)
    project_type = models.ForeignKey("ProjectType", on_delete=models.SET_NULL, null=True, blank=True)

    # Metadata
    class Meta:
        ordering = ['project_name']

    # Methods
    def get_absolute_url(self):
        """ Returns the URL to access a particular instance. """
        return reverse(viewname='project-detail', args=[str(self.id)])

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.project_name


class Card(models.Model):
    # Fields
    card_alias = models.CharField(max_length=30,
                                  unique=False,
                                  help_text="Enter card name",
                                  null=True, blank=True)
    card_number = models.CharField(max_length=16,
                                   unique=True,
                                   help_text="Enter card number",
                                   validators=[MinLengthValidator])
    expiration_date = models.DateField(help_text="Enter expiration date")
    card_type = models.ForeignKey("CardType", on_delete=models.RESTRICT, null=False)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, null=False)
    account = models.ForeignKey("Account", on_delete=models.CASCADE, null=False)

    # Metadata
    class Meta:
        ordering = []

    # Methods
    def get_absolute_url(self):
        """ Returns the URL to access a particular instance. """
        return reverse(viewname='card-detail', args=[str(self.id)])

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return f"{self.card_number} - {self.card_alias}" if self.card_alias else self.card_number


class Transaction(models.Model):
    # Fields
    concept = models.CharField(max_length=200,
                               unique=False,
                               null=False,
                               help_text="Transaction concept")
    operation_date = models.DateField(unique=False,
                                      null=False)
    value_date = models.DateField(unique=False,
                                  null=False)
    amount = models.FloatField(unique=False,
                               null=False,
                               help_text="Transaction amount")
    currency = models.CharField(max_length=3,
                                unique=False,
                                null=False,
                                help_text="Enter transaction currency")
    transaction_comment = models.CharField(max_length=200,
                                           unique=False,
                                           help_text="Enter any comments here",
                                           null=True, blank=True)
    transaction_type = models.ForeignKey("TransactionType", on_delete=models.RESTRICT, null=False)
    card = models.ForeignKey("Card", on_delete=models.SET_NULL, null=True, blank=True)
    account = models.ForeignKey("Account", on_delete=models.RESTRICT, null=False)
    subcategory = models.ForeignKey("Subcategory", on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True, blank=True)
    referenced_transaction = models.ForeignKey("Transaction", on_delete=models.SET_NULL, null=True, blank=True)

    # Metadata
    class Meta:
        ordering = []

    # Methods
    def get_absolute_url(self):
        """ Returns the URL to access a particular instance. """
        return reverse(viewname='transaction-detail', args=[str(self.id)])

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.concept
