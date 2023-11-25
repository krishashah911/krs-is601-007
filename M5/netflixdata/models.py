from datetime import datetime
from decimal import Decimal
from common.utils import JsonSerializable

class Netflixdata(JsonSerializable):
    def __init__(self, title: str, title_type: str, netflix_id: str, synopsis: str,
                 rating: Decimal, year: int, imdb_id: str, title_date: datetime,
                 created: datetime = None, modified: datetime = None):
        self.title = title
        self.title_type = title_type
        self.netflix_id = netflix_id
        self.synopsis = synopsis
        self.rating = rating
        self.year = year
        self.imdb_id = imdb_id
        self.title_date = title_date
        self.created = created
        self.modified = modified