from EduaddaApp.models import *
from django.db.models import Q


# =========== FILTER DATA CLASS HERE ===============
class CbtFliterData:

    def _init_(self, query_data):
        self.query_data = query_data
        print(self.query_data)

    