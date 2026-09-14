"""Middleware that converts unexpected errors into JSON responses."""

from django.http import JsonResponse


class SafeMiddleware:  # pylint: disable=too-few-public-methods
    """Handle requests while returning a JSON response for exceptions."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except Exception as e:  # pylint: disable=broad-exception-caught
            return JsonResponse({"error": str(e)}, status=500)
