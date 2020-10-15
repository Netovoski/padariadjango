from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('appprincipal:index')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:    
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("VOCE NÂO È AUTORIZADO PARA ESSA SEÇÃO")
        return wrapper_func
    return decorator

#adcionar grupos
def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'customer':
			return redirect('appprincipal:index')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function