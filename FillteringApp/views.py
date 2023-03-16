from django.db.models import Q
from django.shortcuts import render
from FillteringApp.models import Review

def ReviewFilterView(request):
    qs = Review.objects.all()

    rs = Review.objects.values_list('rating').distinct()
    numbers = [r[0] for r in rs]

    rating_query = request.GET.get("rating")
    prioritize_text_query = request.GET.get("Prioritizebytext")

    rating_order = request.GET.get("rating_order")


    if rating_query != '' and rating_query is not None:
        qs = qs.filter(rating=rating_query)

    if prioritize_text_query == "Yes":
        qs = qs.filter(Q(reviewText__isnull=False) & ~Q(reviewText='')).order_by('-reviewText', '-rating')

    if rating_order == "Highest First":
        qs = qs.order_by('-rating')
    elif rating_order == "Lowest First":
        qs = qs.order_by('rating')

    context = {
        'queryset': qs,
        'ratingset': numbers,
        'prioritize_text_query': prioritize_text_query,
        'rating_order': rating_order
    }
    return render(request, "review_form.html", context)
