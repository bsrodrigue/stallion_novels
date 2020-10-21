from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Novel

import logging

logger = logging.getLogger(__name__)

def home(request):
    latest_novels = Novel.objects.order_by('-created_at')
    logger.info('Small little creature wants to access Homepage')
    return render(
        request,
        "novels/home.html",
        {
            "page_title": "Stallion Novels",
            "latest_novels": latest_novels,
            "page_hero_title": "Bienvenue sur Stallion Novels",
            "page_hero_description": "Lisez, écrivez et partagez des Webnovels Africains",
        },
    )
