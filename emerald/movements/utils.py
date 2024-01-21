from . import models as pm


def determine_transaction_type(amount):
    if amount > 0:
        return pm.TransactionType.objects.get(name='Income')
    elif amount < 0:
        return pm.TransactionType.objects.get(name='Expense')
    else:
        return pm.TransactionType.objects.get(name='Non Computable')
