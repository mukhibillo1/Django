from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size_query_param = "size"
    page_size = 10

    def get_paginated_response(self, data):
        return Response(
            {
                "page_size": self.get_page_size(self.request),
                "current_page": self.page.number,
                "total_pages": self.page.paginator.num_pages,
                "page_items": len(self.page),
                "total": self.page.paginator.count,
                "results": data,
            }
        )


class ByOne(CustomPagination):
    page_size = 1


class ByOne(CustomPagination):
    page_size = 1


class ByOne(CustomPagination):
    page_size = 1


class ByThree(CustomPagination):
    page_size = 3


class ByFour(CustomPagination):
    page_size = 4


class ByFive(CustomPagination):
    page_size = 5


class BySix(CustomPagination):
    page_size = 6


class BySeven(CustomPagination):
    page_size = 7


class ByEight(CustomPagination):
    page_size = 8


class ByNine(CustomPagination):
    page_size = 9


class PageTen(CustomPagination):
    page_size = 10


class PageEleven(CustomPagination):
    page_size = 11


class PageTwelve(CustomPagination):
    page_size = 12


class PageThirteen(CustomPagination):
    page_size = 13


class PageFourteen(CustomPagination):
    page_size = 14


class PageFifteen(CustomPagination):
    page_size = 15


class PageSixteen(CustomPagination):
    page_size = 16


class PageSeventeen(CustomPagination):
    page_size = 17


class PageEighteen(CustomPagination):
    page_size = 18


class PageNineteen(CustomPagination):
    page_size = 19


class PageTwenty(CustomPagination):
    page_size = 20
