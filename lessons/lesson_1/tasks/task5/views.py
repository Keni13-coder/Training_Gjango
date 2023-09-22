from django.shortcuts import render
from django.http import HttpResponse
import random
import logging

logger = logging.getLogger(__name__)

def heads_or_tails(request):
    responce = random.choice(['орёл', "решка"])
    logger.info(f'responce:{responce}')
    return HttpResponse(responce)



def the_dice(request):
    responce = str(random.randint(1,6))
    logger.info(f'responce:{responce}')
    return HttpResponse(responce)
    
    
def random_numbers(request):
    responce = str(random.randrange(0,100))
    logger.info(f'responce:{responce}')
    return HttpResponse(responce)

