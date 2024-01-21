from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

from .utils import determine_transaction_type


def category_logo_upload_path(instance, filename):
    return f"category/{instance.id}/category_logo/{filename}"


def subcategory_logo_upload_path(instance, filename):
    return f"subcategory/{instance.id}/subcategory_logo/{filename}"


def entity_logo_upload_path(instance, filename):
    return f"entity/{instance.id}/entity_logo/{filename}"


def customer_photo_upload_path(instance, filename):
    return f"customer/{instance.id}/customer_photo/{filename}"


class AccountType(models.Model):
    # Fields
    name = models.CharField(
        max_length=20,
        unique=True,
        help_text="Enter the type of account (savings, investing, etc.)"
    )

    # Metadata
    class Meta:
        ordering = ['name']

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.name


class CardType(models.Model):
    # Fields
    name = models.CharField(
        max_length=10,
        unique=True,
        help_text="Enter the type of card (debit, credit, etc.)"
    )

    # Metadata
    class Meta:
        ordering = ['name']

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.name


class TransactionType(models.Model):
    # Fields
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter the type of transaction (income, expense, etc.)"
    )

    # Metadata
    class Meta:
        ordering = ['name']

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.name


class ProjectType(models.Model):
    # Fields
    name = models.CharField(
        max_length=20,
        unique=False,
        help_text="Enter the type of project (trip, vacation, etc.)"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Metadata
    class Meta:
        ordering = ['name']
        unique_together = ['name', 'owner']

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.name


class Category(models.Model):
    # Fields
    name = models.CharField(
        max_length=50,
        unique=False,
        help_text="Enter a category (restaurant, transport, etc.)"
    )
    logo = models.ImageField(
        help_text="Upload category logo",
        unique=False,
        null=True,
        blank=True,
        upload_to=category_logo_upload_path
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Metadata
    class Meta:
        ordering = ['name']
        verbose_name_plural = "categories"
        unique_together = ['name', 'owner']

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.name


class Subcategory(models.Model):
    # Fields
    name = models.CharField(
        max_length=50,
        unique=False,
        help_text="Enter a subcategory"
    )
    logo = models.ImageField(
        help_text="Upload subcategory logo",
        unique=False,
        null=True,
        blank=True,
        upload_to=subcategory_logo_upload_path
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        null=False,
        related_name='subcategories'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Metadata
    class Meta:
        verbose_name_plural = "subcategories"
        unique_together = ['name', 'owner']

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.name


class Entity(models.Model):
    # Fields
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter entity name"
    )
    logo = models.ImageField(
        help_text="Upload entity logo",
        unique=False,
        null=True,
        blank=True,
        upload_to=entity_logo_upload_path
    )

    # Metadata
    class Meta:
        ordering = ['name']
        verbose_name_plural = "entities"

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.name


class Customer(models.Model):
    # Fields
    first_name = models.CharField(
        max_length=50,
        unique=False,
        help_text="Enter your name"
    )
    last_name = models.CharField(
        max_length=50,
        unique=False,
        help_text="Enter your last name"
    )
    phone = models.CharField(
        max_length=20,
        unique=True,
        help_text="Enter your phone number"
    )
    photo = models.ImageField(
        help_text="Enter your photo",
        null=True,
        blank=True,
        upload_to=customer_photo_upload_path
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Metadata
    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return f"{self.first_name} {self.last_name}"


class Account(models.Model):
    # Fields
    iban = models.CharField(
        max_length=24,
        unique=False,
        null=False,
        help_text="Enter account IBAN",
        verbose_name="IBAN"
    )
    alias = models.CharField(
        max_length=30,
        unique=False,
        null=True,
        blank=True,
        help_text="Enter account alias"
    )
    balance = models.DecimalField(
        max_digits=14,
        decimal_places=2
    )
    currency = models.CharField(
        max_length=3,
        unique=False,
        null=False,
        help_text="Enter account currency"
    )
    account_type = models.ForeignKey(
        "AccountType",
        on_delete=models.RESTRICT,
        null=False
    )
    entity = models.ForeignKey(
        "Entity",
        on_delete=models.RESTRICT,
        null=False
    )
    customers = models.ManyToManyField(
        "Customer"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Metadata
    class Meta:
        unique_together = ['iban', 'owner']

    def display_customers(self):
        """ This is required to display customers in Admin """
        return ', '.join(str(customer) for customer in self.customers.all()[:3])
    display_customers.short_description = 'Customers'

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.iban


class Project(models.Model):
    # Fields
    name = models.CharField(
        max_length=50,
        unique=False,
        help_text="Enter project name"
    )
    description = models.CharField(
        max_length=200,
        help_text="Enter project description",
        null=True,
        blank=True
    )
    project_type = models.ForeignKey(
        "ProjectType",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projects'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Metadata
    class Meta:
        ordering = ['name']
        unique_together = ['name', 'owner']

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.name


class Card(models.Model):
    # Fields
    alias = models.CharField(
        max_length=30,
        unique=False,
        help_text="Enter card name",
        null=True,
        blank=True
    )
    number = models.CharField(
        max_length=16,
        unique=True,
        help_text="Enter card number",
        validators=[MinLengthValidator]
    )
    expiration_date = models.DateField(
        help_text="Enter expiration date"
    )
    card_type = models.ForeignKey(
        "CardType",
        on_delete=models.RESTRICT,
        null=False
    )
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE,
        null=False
    )
    account = models.ForeignKey(
        "Account",
        on_delete=models.CASCADE,
        null=False
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Metadata
    class Meta:
        unique_together = ['number', 'owner']

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.number


class Transaction(models.Model):
    # Fields
    concept = models.CharField(
        max_length=200,
        unique=False,
        null=False,
        help_text="Transaction concept"
    )
    operation_date = models.DateField(
        unique=False,
        null=False
    )
    value_date = models.DateField(
        unique=False,
        null=False
    )
    amount = models.DecimalField(
        max_digits=14,
        decimal_places=2
    )
    currency = models.CharField(
        max_length=3,
        unique=False,
        null=False,
        help_text="Enter transaction currency"
    )
    comment = models.CharField(
        max_length=200,
        unique=False,
        help_text="Enter any comments here",
        null=True,
        blank=True
    )
    transaction_type = models.ForeignKey(
        "TransactionType",
        on_delete=models.RESTRICT,
        null=False
    )
    card = models.ForeignKey(
        "Card",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    account = models.ForeignKey(
        "Account",
        on_delete=models.CASCADE,
        null=False
    )
    subcategory = models.ForeignKey(
        "Subcategory",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    project = models.ForeignKey(
        "Project",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    referenced_transaction = models.ForeignKey(
        "Transaction",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Metadata
    class Meta:
        ordering = []

    def __str__(self):
        """ String for representing the MyModelName object (in Admin site etc.). """
        return self.concept

    def save(self, *args, **kwargs):
        # Determine the transaction type based on the amount
        self.transaction_type = determine_transaction_type(self.amount)

        super(Transaction, self).save(*args, **kwargs)
