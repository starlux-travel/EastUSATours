from .models import SiteTheme

def site_theme(request):
    try:
        theme = SiteTheme.objects.first()
    except Exception:
        theme = None
    return {'site_theme': theme}
