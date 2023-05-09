from typing import NewType

RawHTML = NewType("RawHTML", str)


def as_raw_html(html_data: str) -> RawHTML:
    if not (isinstance(html_data, str) and html_data.isascii()):
        raise ValueError()
    return RawHTML(html_data)
