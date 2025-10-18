from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from datetime import datetime, timezone
import requests


# Create your views here.
@method_decorator(never_cache, name='dispatch')
class profileView(APIView):
    def get(self, request):
        utc_time = datetime.now(timezone.utc).isoformat()


        try:
            response = requests.get("https://catfact.ninja/fact")
            catfact = response.json().get('fact', 'Facts not found')
        except Exception:
            catfact = 'Could not fetch any cat fact right this moment'
        return Response({
            "status": "success",
            "user": {
                "email": "judeani60@gmail.com",
                "name": "Ani Jude Ikechukwu",
                "stack": ["HTML5", "CSS", "JAVASCRIPT", "PYTHON", "DJANGO"]
            },
            "timestamp": utc_time,
            "fact": catfact
        }, status=HTTP_200_OK)
