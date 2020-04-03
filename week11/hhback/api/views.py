from django.http import JsonResponse
from api.models import Company,Vacancy

def company_list(request):
    companies = Company.objects.all()
    json_comp=[c.to_json() for c in companies]
    return JsonResponse(json_comp,safe=False)
def company_detail(request,pk):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse(company.to_json())

def company_vacancy(request,pk):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    vacancy = company.vacancy_set.all()
    json_vacancy = [v.to_json() for v in vacancy]
    return JsonResponse(json_vacancy,safe=False)

def vacancy_list(request):
    vacancy = Vacancy.objects.all()
    vacancy_json = [v.to_json() for v in vacancy]
    data = {
        'vacancies': vacancy_json,
    }
    return JsonResponse(data)
def vacancy_detail(request,pk):
    try:
        vacancy = Vacancy.objects.get(id=pk).to_json()
    except Vacancy.DoesNotExist as e:
        return JsonResponse({
            'error':str(e)
        })
    return JsonResponse(vacancy)
def top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10:1]
    vacancy_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancy_json, safe=False)
