import json
from pprint import pprint


class _Chat(object):
    first_name = None
    id = None
    last_name = None
    private = None
    username = None

    def __init__(self, chat_body):
        self.first_name = chat_body.get("first_name")
        self.id = chat_body.get("id")
        self.last_name = chat_body.get("last_name")
        self.private = True if chat_body.get("type") == "private" else False
        self.username = chat_body.get("username")

        if not self.username:
            self.username = "{} {}".format(self.first_name, self.last_name)


class _From(object):
    first_name = None
    id = None
    last_name = None
    is_bot = False
    username = None

    def __init__(self, from_body):
        self.first_name = from_body.get("first_name")
        self.id = from_body.get("id")
        self.last_name = from_body.get("last_name")
        self.is_bot = from_body.get("is_bot")
        self.username = from_body.get("username", None)

        if not self.username:
            self.username = "{} {}".format(self.first_name, self.last_name)


class _Callback(object):
    data = None

    def __init__(self, call_body):
        self.data = call_body.get("data")


class Parse(object):
    text = ""
    Chat = None
    From = None
    is_group = False

    def __init__(self, body, registry=None):
        _meta_body = self.body_decode(body)
        has_callback = False

        if 'callback_query' in _meta_body:
            self.call_back = _Callback(self.body_decode(body).get("callback_query"))
            _meta_body = _meta_body.get("callback_query")
            has_callback = True

        self.BODY = _meta_body.get("message")
        self.Chat = _Chat(self.BODY.get("chat"))
        self.is_group = True if self.Chat.id < 0 else False
        self.From = _From(self.BODY.get("from"))
        self.text = self.BODY.get("text") if not has_callback else _meta_body.get("data")
        self.command = self.parse_command(self.text)

        print(self.text)
        print(self.command)
        if registry and self.command not in registry:
            self.command = None

    def __load_chat_and_from(self):
        pass

    def body_decode(self, body):
        return json.loads(body.decode("utf-8"))

    def parse_command(self, text):
        if not text or len(text) < 0:
            return None

        if not self.Chat.private:
            return text.split("@")[0]
        return text.split(" ")[0]
