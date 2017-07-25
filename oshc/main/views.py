from django.shortcuts import render

import re;



def home(request):
    return render(request, 'index.html')

def request_session(request):
    return render(request, 'session.html')




def RANDOM_VIEW(request):
    str = "This is a test string. The length of this string is more than 80 chars. Hound CI should report this line as it violated the PEP8 convention. Some more random words to increase the string length".

    
    
    
    // Whitespce
