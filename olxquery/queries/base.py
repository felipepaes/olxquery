from pathlib import Path
import random
import re
import urllib.request
from urllib.parse import urlunsplit, urlencode, urlparse, parse_qsl, urlunparse
import xml.etree.ElementTree as ET


class BaseQuery:

    __UA_FILE = "ua_file.txt"
    __SCHEME = "https"
    __NETLOC = "olx.com.br"
    __QUERY_PARAMS = {
        "search": "q",
        "price_min": "ps",
        "price_max": "pe",
        "page": "o",
    }

    def __init__(self,
                 search=None,
                 location=None,
                 category=None,
                 price_min=None,
                 price_max=None,
                 *args,
                 **kwargs):

        self.search = search
        self.location = location
        self.category = category

        self.price_min = price_min
        self.price_max = price_max

        self.__urls = []
        self.__urls_generated = False
        self.__user_agent = self.__get_user_agent()

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
        if self.location is not None:
            uf = self.location.__module__.split(".")[-1]
            return uf
        return None

    def __get_netloc(self):
        if self.__get_state_uf():
            uf = self.__get_state_uf()
            netloc = f"{uf}.{self.__NETLOC}"
            return netloc
        return self.__NETLOC

    def __get_obj_prop(self, cls, prop="url"):
        url = getattr(cls, f"_{cls.__name__}__{prop}")
        return url

    def __get_path(self):
        path = []

        if self.location is not None:
            path.append(self.__get_obj_prop(self.location))

        if self.category is not None:
            path.append(self.__get_obj_prop(self.category))

        if len(path) == 1:
            return path[0]
        elif len(path) > 1:
            return "/".join(path)
        
        return ""

    def __get_query(self):
        queries = {k: v for (k, v) in vars(self).items()  # Get queryable properties filtering from __QUERY_PARAMS
                   if k in self.__QUERY_PARAMS.keys()
                   and v is not None}

        if queries is not None:
            query = {}
            for k, v in queries.items():  # new dictionary with correct keys from __QUERY_PARAMS
                query[self.__QUERY_PARAMS[k]] = v
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
            url,
            None,
            headers={"User-Agent": self.__user_agent}
        )
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        return html

    def __append_to_query(self, url, query_param, value):
        parsed_url = urlparse(url)
        query = dict(parse_qsl(parsed_url.query))
        query.update({
            self.__QUERY_PARAMS[query_param]: value
        })
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
            for n in range(2, last_page+1):
                self.__urls.append(self.__append_to_query(url, "page", n))
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

    def __str__(self):
        search = f' search="{self.search}"' if self.search is not None else ""
        location = f' location="{self.location.__name__}"' if self.location is not None else ""
        category = f' category="{self.category.__name__}"' if self.category is not None else ""
        return f"<BaseQuery({{{search}{location}{category}}})>"
