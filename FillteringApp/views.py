from django.shortcuts import render

# Create your views here.
from FillteringApp.models import Review


def ReviewFilterView(request):
    qs = Review.objects.all()
    rs = Review.objects.values_list('rating').distinct()
    numbers = [r[0] for r in rs]

    rating_query =  request.GET.get("rating")
    reviewText_query = request.GET.get("reviewText")

    if rating_query != '' and rating_query is not None:
        qs = qs.filter(rating=rating_query)
    if reviewText_query != '' and reviewText_query is not None:
        qs = qs.filter(reviewText=reviewText_query)
    context = {
        'queryset': qs,
        'ratingset': numbers
    }
    return render(request, "review_form.html", context)

