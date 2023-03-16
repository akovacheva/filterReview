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

    date_order = request.GET.get("date_order")
    #
    # if rating_query:
    #     qs = qs.filter(rating__gte=rating_query)
    #
    # if prioritize_text_query == "Yes":
    #     qs = qs.order_by('-reviewText')
    #
    #
    # if rating_order == "Highest First":
    #     qs = qs.order_by('-rating')
    # elif rating_order == "Lowest First":
    #     qs = qs.order_by('rating')
    #
    # if date_order == "Newest First":
    #     qs = qs.order_by('-reviewCreatedOnDate')
    # elif rating_order == "Oldest First":
    #     qs = qs.order_by('reviewCreatedOnDate')

    if rating_query and prioritize_text_query == "Yes":
        qs = qs.filter(rating__gte=rating_query).order_by('-reviewText', '-rating', '-reviewCreatedOnDate')
    elif rating_query:
        qs = qs.filter(rating__gte=rating_query).order_by('-rating', '-reviewCreatedOnDate', '-reviewText')
    elif prioritize_text_query == "Yes":
        qs = qs.order_by('-reviewText', '-rating', '-reviewCreatedOnDate')
    elif rating_order == "Highest First":
        qs = qs.order_by('-rating', '-reviewCreatedOnDate', '-reviewText')
    elif rating_order == "Lowest First":
        qs = qs.order_by('rating', '-reviewCreatedOnDate', '-reviewText')
    elif date_order == "Newest First":
        qs = qs.order_by('-reviewCreatedOnDate', '-rating', '-reviewText')
    elif date_order == "Oldest First":
        qs = qs.order_by('reviewCreatedOnDate', '-rating', '-reviewText')


    context = {
        'queryset': qs,
        'ratingset': numbers,
        'prioritize_text_query': prioritize_text_query,
        'rating_order': rating_order
    }
    return render(request, "review_form.html", context)
