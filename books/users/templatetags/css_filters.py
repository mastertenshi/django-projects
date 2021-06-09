from django import template


register = template.Library()


@register.filter(is_safe=True)
def input_class(value, attrs):
    try:
        # if value.field.widget.input_type in ['text', 'password']:
        value.field.widget.attrs.update({'class': attrs})
    except:
        pass

    return value


@register.filter(is_safe=True)
def printtag(value):
    print(f'\n\ndir: {dir(value)}\n')
    print(f'value: {value}\n\n')
    return value