from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = "accountsTemplates/login.html"


class CustomLogoutView(LogoutView):
    pass
