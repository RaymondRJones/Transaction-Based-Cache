from django.urls import path
from cache_app.views import cache_get, cache_set, cache_delete, cache_begin, cache_commit, cache_rollback

urlpatterns = [
    path("cache/get/", cache_get, name="cache_get"),
    path("cache/set/", cache_set, name="cache_set"),
    path("cache/delete/", cache_delete, name="cache_delete"),
    path("cache/begin/", cache_begin, name="cache_begin"),
    path("cache/commit/", cache_commit, name="cache_commit"),
    path("cache/rollback/", cache_rollback, name="cache_rollback"),
]

