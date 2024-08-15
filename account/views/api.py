from django.http import JsonResponse
from django.views.generic import View

from common.pagination import Pagination
from user.exceptions import InvalidReferalLevel, InvalidSortedByField
from user.user_service.user_service import get_user_service
from user.user_service.user_service_interface import UserServiceInterface


class GetReferals(View):
    user_service: UserServiceInterface = get_user_service()

    def get(self, request):
        level = self.request.GET.get("level")
        sorted_by = self.request.GET.get("sorted_by")

        try:
            referrals = self.user_service.get_referrals(level=level, user=self.request.user, sorted_by=sorted_by)
        except InvalidSortedByField as e:
            return JsonResponse({"error": str(e)}, status=400)
        except InvalidReferalLevel as e:
            return JsonResponse({"error": str(e)}, status=400)

        pagination = Pagination(request)

        referrals = pagination.paginate(referrals, "referrals")

        return JsonResponse(referrals)