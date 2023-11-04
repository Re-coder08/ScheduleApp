from django.utils import timezone
from django.contrib.auth import logout

from . import settings

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')

            if last_activity is not None:
                # Calculate the elapsed time since the last activity
                elapsed_time = timezone.now() - last_activity

                # Check if the elapsed time exceeds the session timeout
                if elapsed_time.total_seconds() >= settings.SESSION_COOKIE_AGE:
                    # Log the user out
                    logout(request)

            # Update the last activity timestamp in the session
            request.session['last_activity'] = timezone.now()

        response = self.get_response(request)
        # print("Type :: {}".format(type(response)))
        return response
