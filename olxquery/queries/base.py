import random
import re
import urllib.request
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse, urlunsplit
from olxquery.types import Location, Category


class BaseQuery(ABC):
    __UA_FILE = "ua_file.txt"
    __SCHEME = "https"
    __NETLOC = "olx.com.br"

    location: Location | None
    category: Category | None

    @property
    @classmethod
    @abstractmethod
    def QUERY_PARAMS(cls) -> dict[str, str]:
        return NotImplementedError

    def __init__(self, **kwargs):
        if kwargs:
            self.__init_atributes(kwargs)

        self.__urls = []
        self.__urls_generated = False
        self.__user_agent = self.__get_user_agent()

    def __init_atributes(self, kwargs: dict):
        for k, v in kwargs.items():
            if v is not None:
                setattr(self, k, v)

    def __get_user_agent(self):
        try:
            filename = Path(__file__).resolve().parent.parent / self.__UA_FILE
            with open(filename, "r") as f:
                lines = f.readlines()
                user_agent = random.choice(lines)[:-2]
        except Exception as e:
            raise e
        return user_agent

    def __get_state_uf(self):
        # if self.location is not None:
        if hasattr(self, "location"):
            uf = self.location.__module__.split(".")[-1]
            return uf
        return None

    def __get_netloc(self):
        return self.__NETLOC

    def __get_obj_prop(self, cls, prop="url"):
        url = getattr(cls, f"_{cls.__name__}__{prop}")
        return url

    def __get_path(self):
        path = []

        # if self.category is not None:
        if hasattr(self, "category"):
            path.append(self.__get_obj_prop(self.category))

        # if self.location is not None:
        if hasattr(self, "location"):
            uf = self.__get_state_uf()
            path.append(f"estado-{uf}")
            path.append(self.__get_obj_prop(self.location))

        if len(path) == 1:
            return path[0]
        elif len(path) > 1:
            return "/".join(path)

        return ""

    def __get_query(self):
        queries = {
            k: v
            for (k, v) in vars(
                self
            ).items()  # Get queryable properties filtering from __QUERY_PARAMS
            if k in self.QUERY_PARAMS.keys() and v is not None
        }

        if queries is not None:
            query = {}
            for (
                k,
                v,
            ) in (
                queries.items()
            ):  # new dictionary with correct keys from __QUERY_PARAMS
                query[self.QUERY_PARAMS[k]] = v
            return urlencode(query)
        # tuple_version = [(k, v) for k, v in {k: v for (k, v) in vars(self).items()  # Same but with list of tuples
        #                                      if k in self.__QUERY_PARAMS.keys()
        #                                      and v is not None}.items()]

    def __build_url(self):
        netloc = self.__get_netloc()
        path = self.__get_path()
        query = self.__get_query()
        url = urlunsplit((self.__SCHEME, netloc, path, query, None))

        if len(self.__urls) == 0:
            self.__urls.append(url)
        return url

    def __get_html(self, url):
        req = urllib.request.Request(
            url, None, headers={"User-Agent": self.__user_agent}
        )
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        return html

    def __append_page_to_query(self, url, page_number):
        parsed_url = urlparse(url)
        query = dict(parse_qsl(parsed_url.query))
        query.update({"o": page_number})
        parsed_url = parsed_url._replace(query=urlencode(query))
        url = urlunparse(parsed_url)
        return url

    def __generate_urls(self):
        url = self.__build_url()
        html = self.__get_html(url)

        re_pattern = r"data-lurker_position=\"(\d+)"
        matches = re.findall(re_pattern, html)

        if matches:
            last_page = int(matches[-1])
            for n in range(
                2, last_page + 1
            ):  # 2 because we already have the first page + 1 because of how range works
                self.__urls.append(self.__append_page_to_query(url, n))
        else:
            self.__urls.append(url)

        self.__urls_generated = True
        return self.__urls

    @property
    def url(self):
        if len(self.__urls) > 0:
            return self.__urls[0]
        else:
            return self.__build_url()

    @property
    def urls(self):
        if self.__urls_generated:
            return self.__urls
        else:
            return self.__generate_urls()

    def __repr__(self):
        return f"<{self.__class__.__name__} object {id(self)!r}>"

    # TODO: Think about how to implement __str__ without knowing the kwargs
    # def __str__(self):
    #     search = f' search="{self.search}"' if self.search is not None else ""
    #     location = f' location="{self.location.__name__}"' if self.location is not None else ""
    #     category = f' category="{self.category.__name__}"' if self.category is not None else ""
    #     return f"<BaseQuery({{{search}{location}{category}}})>"
