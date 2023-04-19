import json
import re

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect


# @require_http_methods(['PUT'])
# @login_required