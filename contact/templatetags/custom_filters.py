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

@register.simple_tag
def mailchimp_landing_link():
    """PUll landing page link out of settings."""
    if settings.MAILCHIMP_LANDING_PAGE_LINK:
        return settings.MAILCHIMP_LANDING_PAGE_LINK
    else:
        return ""