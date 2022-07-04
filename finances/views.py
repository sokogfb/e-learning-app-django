from django.shortcuts import render

# Create your views here.
from rave_python import Rave

from _elms_core import settings

# rave = Rave(settings.RAVE_PUBLIC_KEY)
rave = Rave(settings.RAVE_PUBLIC_KEY, settings.RAVE_SECRET_KEY, usingEnv=False)  ## In Development Environment
# rave = Rave("YOUR_PUBLIC_KEY", production=True) ## In Production Environmen
rave.__new__()
