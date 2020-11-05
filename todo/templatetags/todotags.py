from django import template


register = template.Library()

SIZES = {
    1: ('XS', 'xtrasmall'),
    2: ('S', 'small'),
    3: ('M', 'medium'),
    4: ('L', 'large'),
    5: ('XL', 'xtralarge'),
}

@register.filter()
def as_task_size(size_level, format="short"):
    if size_level < 0 or size_level >5:
        return size_level
    t = SIZES.get(size_level)
    if format == 'long':
        index = 1
    else:
        index = 0
    return t[index]


@register.inclusion_tag('todo/show_priority.html')
def show_priority(task):
    return {'task': task}


@register.inclusion_tag('todo/show_size.html')
def show_size(task):
    return {
        'size': task.size,
        'label': SIZES.get(task.size)[0] 
        }
