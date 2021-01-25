from allauth.socialaccount.models import SocialToken
from django.shortcuts import render


# Create your views here.


def _get_access_token(request):
    return SocialToken.objects.get(
                        account__user=request.user,
                        account__provider='google'
                    ).token


def index(request):
    context = {}

    if request.user.is_authenticated:
        context['msg'] = "Welcome, " + request.user.username
        print(_get_access_token(request))
    else:
        context['msg'] = "Please login.."

    return render(request, "loginlogoutapp/index.html", context)
