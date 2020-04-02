from django.http import JsonResponse
from api.models import Category
from api.models import Product

def category_list(request):
    categories = Category.objects.all()
    json_categories = [c.to_json() for c in categories]
    return JsonResponse(json_categories, safe=False)


def category_detail(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.to_json())


def category_product(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.product_set.all()
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)

def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    data = {
        'products': products_json,
    }
    return JsonResponse(data)

def product_detail(request, pk):
    try:
        product = Product.objects.get(id=pk).to_json()
    except Product.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        })
    return JsonResponse(product)