from rest_framework.pagination import PageNumberPagination

from .constants import MAX_PAGE


class PostsPagination(PageNumberPagination):
    page_size = MAX_PAGE
     