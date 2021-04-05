# These next two lines are necessary for Django to recognize that 
# the following function calls are for custom filters.

from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter
register = template.Library()

# Custom filters go here.

# Register filter with library and define it as a function that only 
# takes strings to avoid AttributeErrors

@register.simple_tag
def mailchimp_integration_script(format_html=True):
    """Pull in mailchimp integration script."""
    if settings.MAILCHIMP_INTEGRATION_SCRIPT:
        return settings.MAILCHIMP_INTEGRATION_SCRIPT
    else:
        return ""