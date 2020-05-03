from typing import Any, Protocol, cast

from mako.lookup import TemplateLookup as MakoTemplateLookup


class FormatTemplate(Protocol):
    def format(self, **kwargs: Any) -> str:  # noqa: A003
        ...  # noqa: WPS428  # pragma: no cover


class TemplateLookup(MakoTemplateLookup):
    def get_template(self, uri: str) -> FormatTemplate:
        template = super().get_template(uri)
        template.format = template.render
        return cast(FormatTemplate, template)


_TEMPLATE_LOOKUP = TemplateLookup(
    directories=["app/resources/templates"], input_encoding="utf-8"
)

HELLO_MESSAGE_TEMPLATE = _TEMPLATE_LOOKUP.get_template("chat_created.txt.mako")
HELP_COMMAND_MESSAGE_TEMPLATE = _TEMPLATE_LOOKUP.get_template("help.txt.mako")
HELP_COMMAND_DESCRIPTION = "Показать список команд"
HELP_LABEL = "/help"
