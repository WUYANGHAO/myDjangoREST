from rest_framework import pagination

class StandardPageNumberPagination(pagination.PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'