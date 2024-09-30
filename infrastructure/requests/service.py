from django.http import HttpRequest


class RequestService:
    def __init__(self, request: HttpRequest):
        self.request = request

    def get_all_headers_to_string(self) -> str:
        str_headers = ""
        for key, value in self.request.META.items():
            if "HTTP" in key:
                str_headers += f"""{key}: {value}\n"""

        return str_headers

    def get_client_ip(self) -> str:
        x_forwarded_for = self.request.META.get("HTTP_X_REAL_IP")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = self.request.META.get("REMOTE_ADDR")
        return ip


def get_request_service(request):
    return RequestService(request)
