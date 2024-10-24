class BasicType:
    url = ""
    is_root = False

    @classmethod
    def get_url(cls):
        if hasattr(cls, "_parent") and not cls._parent.is_root:
            parent_url = cls._parent.get_url()
            if parent_url and not parent_url.endswith("/"):
                parent_url += "/"
            return f"{parent_url}{cls.url}"
        return cls.url

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        for _, obj in cls.__dict__.items():
            if isinstance(obj, type) and issubclass(obj, BasicType):
                obj._parent = cls


class Category(BasicType):
    pass


class Location(BasicType):
    pass
