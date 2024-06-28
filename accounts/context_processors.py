from .models import Account, TrainerAccount

def user_type(request):
    user_type = None
    if request.user.is_authenticated:
        if isinstance(request.user, Account):
            user_type = 'account'
        elif isinstance(request.user, TrainerAccount):
            user_type = 'trainer'
    return {'user_type': user_type}
