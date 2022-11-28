from django.template.context_processors import request
from django.views import generic
from .models import Article
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


class IndexView(generic.ListView):
    template_name = 'shop/home.html'
    context_object_name = 'latest_articles_list'
    def get_queryset(self):
        return Article.objects.all()


def product_detail(request, slug):
    product = get_object_or_404(Article, slug=slug)
    return render(request, 'shop/detail.html', context={"product": product})


def add_to_cart(request, article_id):
    # check if user is auth

    # alternative au try et except dans la function def
    article = get_object_or_404(Article, pk=article_id)

    try:
        selected_choice = article.choice_set.get(pk=request.POST['choice'])

    # KeyError = rien n'est passé en POST
    except (KeyError, Article.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': article,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # quand l'utilisateur a vôté, il est redirigé sur la /polls/<id>/results
        return HttpResponseRedirect(reverse('polls:results', args=article_id))
