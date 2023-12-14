from django.shortcuts import render, redirect
from receipts.models import Receipt

def receipt_list(request):
    receipts = Receipt.objects.all()
    context = {
        'receipts': receipts,
    }
    return render(request, 'receipts/receipt_list.html', context)
