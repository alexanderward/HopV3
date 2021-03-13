from rest_framework.response import Response


class CustomResponse:

    @staticmethod
    def success(data, status_code=200):
        return Response({"status": "success", "data": data}, status=status_code)

    @staticmethod
    def error(message, status_code=400):
        return Response({"status": "error", "message": message}, status=status_code)
