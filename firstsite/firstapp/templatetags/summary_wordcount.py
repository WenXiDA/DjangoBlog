from django import template

register = template.Library()

@register.filter(name="slice_words")
def slice_words(summary,limit):
	limit = eval(limit)
	return summary if len(summary) < limit else summary[:limit+1]+"...."