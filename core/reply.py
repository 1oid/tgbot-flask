import json


def decro(_post, parse_mode=None, disable_web_page_preview=False):
    if parse_mode:
        _post['parse_mode'] = parse_mode
    _post['disable_web_page_preview'] = disable_web_page_preview
    return _post


def ReplyText(text, chat_id, parse_mode=None, disable_web_page_preview=False):
    _post = {
        "text": text,
        "chat_id": chat_id
    }

    if parse_mode:
        _post["parse_mode"] = parse_mode
    _post['disable_web_page_preview'] = disable_web_page_preview
    return _post


def ReplyWithKeyBoardButton(text, chat_id, keyboards, parse_mode=None, disable_web_page_preview=False):
    """
    :param text:
    :param chat_id:
    :param keyboards:
        json.dumps({
            "keyboard": [[
                {"text": "买家中心"},
                {"text": "卖家中心"}
            ], [
                {"text": "充币/提币/转账"},
                {"text": "联系客服"},
            ]]
        })
    :return:
    """
    _post = {
        "text": text,
        "chat_id": chat_id,
        "reply_markup": json.dumps({
            "keyboard": keyboards
        })
    }
    if parse_mode:
        _post["parse_mode"] = parse_mode
    _post['disable_web_page_preview'] = disable_web_page_preview
    return _post


def ReplyWithInlineKeyboardButton(text, chat_id, inline_keyboards, parse_mode=None, disable_web_page_preview=False):
    _post = {
        "text": text,
        "chat_id": chat_id,
        "reply_markup": json.dumps({
            "inline_keyboard": inline_keyboards
        })
    }
    if parse_mode:
        _post["parse_mode"] = parse_mode
    _post['disable_web_page_preview'] = disable_web_page_preview
    return _post

