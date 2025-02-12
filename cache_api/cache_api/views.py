from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import json
from cache_app.cache_manager import TransactionalCache

cache = TransactionalCache()

@csrf_exempt
def cache_get(request):
    if request.method == "GET":
        key = request.GET.get("key")
        value = cache.get(key)
        return JsonResponse({"key": key, "value": value}, status=200)

@csrf_exempt
def cache_set(request):
    if request.method == "POST":
        data = json.loads(request.body)
        key, value = data.get("key"), data.get("value")
        cache.set(key, value)
        return JsonResponse({"message": "Value staged for commit"}, status=200)

@csrf_exempt
def cache_delete(request):
    if request.method == "POST":
        data = json.loads(request.body)
        key = data.get("key")
        cache.delete(key)
        return JsonResponse({"message": "Key staged for deletion"}, status=200)

@csrf_exempt
def cache_begin(request):
    if request.method == "POST":
        try:
            cache.begin()
            return JsonResponse({"message": "Transaction started"}, status=200)
        except RuntimeError as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def cache_commit(request):
    if request.method == "POST":
        try:
            cache.commit()
            return JsonResponse({"message": "Transaction committed"}, status=200)
        except RuntimeError as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def cache_rollback(request):
    if request.method == "POST":
        try:
            cache.rollback()
            return JsonResponse({"message": "Transaction rolled back"}, status=200)
        except RuntimeError as e:
            return JsonResponse({"error": str(e)}, status=400)

