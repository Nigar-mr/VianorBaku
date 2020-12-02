from django import template
from generally.models import ContactData
from orders.models import Card_list

register = template.Library()


@register.simple_tag()
def get_contact():
    context = {}
    context['phone'] = ContactData.objects.all()
    for i in ContactData.objects.all():
        context['email'] = i.email
        context['loc'] = i.location
        context['hour'] = i.working_hours
        return context

@register.simple_tag
def url_replace(request, field, value):

    dict_ = request.GET.copy()

    dict_[field] = value
    print(dict_.urlencode())
    return dict_.urlencode()

# @register.inclusion_tag('index.html', takes_context=True)
# def my_bill(context):
#     # contekst = {}
#     request = context['request']
#     user = request.session.session_key
#     cards = Card_list.objects.filter(user__session_key=user)
#     context['order'] = cards
#     return context
