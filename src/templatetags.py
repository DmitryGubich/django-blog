import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from markdown.extensions.tables import TableExtension

register = template.Library()


@register.filter()
@stringfilter
def render_markdown(value):
    md = markdown.Markdown(
        extensions=[
            "fenced_code",
            "codehilite",
            TableExtension(use_align_attribute=True),
        ]
    )
    return mark_safe(md.convert(value))
