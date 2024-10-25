from abc import ABC
from urllib.parse import urlencode, urlunsplit

from olxquery.types import Category, Location


class BaseQuery(ABC):
    __SCHEME = "https"
    __NETLOC = "olx.com.br"

    location: Location | None
    category: Category | None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "QUERY_PARAMS") or not isinstance(cls.QUERY_PARAMS, dict):
            raise TypeError(
                f"Class {cls.__name__} must define a class-level dictionary 'QUERY_PARAMS'."
            )

    def __init__(self, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if v is not None:
                    setattr(self, k, v)

    def __get_netloc(self):
        return self.__NETLOC

    def __get_path(self):
        path = []

        # if self.category is not None:
        if hasattr(self, "category"):
            path.append(self.category.get_url())

        # if self.location is not None:
        if hasattr(self, "location"):
            path.append(self.location.get_url())

        if len(path) == 1:
            return path[0]
        elif len(path) > 1:
            return "/".join(path)

        return ""

    def __get_query(self):
        # Get queryable properties
        # by checking QUERY_PARAMS
        queries = {
            k: v for (k, v) in vars(self).items() if k in self.QUERY_PARAMS.keys() and v is not None
        }

        if queries is not None:
            query = {}
            # new dictionary with correct keys from QUERY_PARAMS
            for k, v in queries.items():
                query[self.QUERY_PARAMS[k]] = v
            return urlencode(query)

    def __build_url(self):
        netloc = self.__get_netloc()
        path = self.__get_path()
        query = self.__get_query()
        url = urlunsplit((self.__SCHEME, netloc, path, query, None))
        return url

    @property
    def url(self):
        return self.__build_url()

    def __repr__(self):
        return f"<{self.__class__.__name__} object {id(self)!r}>"

    # TODO: Think about how to implement __str__ without knowing the kwargs
    # def __str__(self):
    #     search = f' search="{self.search}"' if self.search is not None else ""
    #     location = f' location="{self.location.__name__}"' if self.location is not None else ""
    #     category = f' category="{self.category.__name__}"' if self.category is not None else ""
    #     return f"<BaseQuery({{{search}{location}{category}}})>"
