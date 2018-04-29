from django import template
from django.utils.html import format_html

register = template.Library()


PAGE_MENU_LEN = 4


@register.simple_tag
def circle_page(page, loop_page):
	# offset = abs(current_page - loop_page)
	# if offset < PAGE_MENU_LEN:
	# 	if loop_page == current_page:
	# 		page_ele = '''<a href="?page= %d" class="active item" id="current_page">%d</a>''' % (loop_page,loop_page)
	# 	else:
	# 		page_ele = '''<a href="?page= %d" class="item">%d</a>''' % (loop_page,loop_page)
	# 	return format_html(page_ele)
	# else:
	# 	return ""
	current_page = page.page_index
	page_count = page.page_count
	offset = loop_page - current_page
	mid_page = page_count - PAGE_MENU_LEN // 2
	print("current_page==========>",current_page)
	print("loop_page==========>",loop_page)
	print("offset==========>",offset)
	#将页码菜单分段处理，以当前页码加上菜单长度是否大于总页码为界
	if 0 <=offset < PAGE_MENU_LEN and current_page + PAGE_MENU_LEN <= page_count:
		if loop_page == current_page:
			page_ele = '''<a href="?page= %d" class="active item" id="current_page">%d</a>''' % (loop_page,loop_page)
		else:
			page_ele = '''<a href="?page= %d" class="item">%d</a>''' % (loop_page,loop_page)
		return format_html(page_ele)
	elif current_page + PAGE_MENU_LEN > page_count and (page_count - loop_page) <PAGE_MENU_LEN :

		print( 0 <=offset < PAGE_MENU_LEN and current_page + PAGE_MENU_LEN > page_count)
		print(" current_page + PAGE_MENU_LEN==========>", current_page + PAGE_MENU_LEN)
		if loop_page == current_page:
			page_ele = '''<a href="?page= %d" class="active item" id="current_page">%d</a>''' % (loop_page,loop_page)
		else:
			page_ele = '''<a href="?page= %d" class="item">%d</a>''' % (loop_page,loop_page)
		return format_html(page_ele)
	else:
		return ""