import threading

_thread_locals = threading.local()

def get_current_user():
    """Retourne l'utilisateur actuel stocké dans le thread local."""
    return getattr(_thread_locals, 'user', None)

def set_current_user(user):
    """Stocke l'utilisateur actuel dans le thread local."""
    _thread_locals.user = user

def unset_current_user():
    """Nettoie le thread local."""
    if hasattr(_thread_locals, 'user'):
        del _thread_locals.user

class SetCurrentUserMiddleware:
    """
    Middleware qui stocke l'utilisateur de la requête dans la mémoire thread-local.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            set_current_user(request.user)
        else:
            set_current_user(None) # S'assurer que l'utilisateur est bien None si non connecté

        response = self.get_response(request)
        
        # Nettoyage est essentiel pour éviter les fuites de threads (important)
        unset_current_user() 
        return response