from django.shortcuts import render

# Create your views here.
from FillteringApp.models import Review


def ReviewFilterView(request):
    qs = Review.objects.distinct().all()
    rating_query =  request.GET.get("rating")

    if rating_query != '' and rating_query is not None:
        qs = qs.filter(rating=rating_query)
    context = {
        'queryset': qs

    }
    return render(request, "review_form.html", context)

