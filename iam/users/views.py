from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def user_info(request):
    user_data = {
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }
    return JsonResponse(user_data)
