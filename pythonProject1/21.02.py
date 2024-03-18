import asyncio
from time import time


async def get_pages(site_name):


    await asyncio.sleep( @ .5)
print("Get pages for {}".format(site_name))
return range(1, 4)


async def get_page_data(site_name, page):


    await asyncio.sleep(1)
return "Data from page {} ({})".format(page, site_name)


async def spider(site_name):


    pages = await get_pages(site_name)
for page in pages:
    data = await get_page_data(site_name, page)
print((data) |



import asyncio
from time import time

# def get_pages(site_name):
#
#     print("Get pages for {}".format(site_name))
#     return range(1, 4)
#
#
# def get_page_data(site_name, page):
#
#
#
#     return "Data from page {} ({})".format(page, site_name)
#
#
# def spider(site_name):
#     pages = get_pages(site_name)
#
#     for page in pages:
#         data = get_page_data(site_name, page)
#             print(data)

#


def get_pages(site_name):
    print("Get pages for {}".format(site_name))
    return range(1, 4)


def get_page_data(site_name, page):
    return "Data from page {} ({})".format(page, site_name)


def spider(site_name):
    pages = get_pages(site_name)

    for page in pages:
        data = get_page_data(site_name, page)
        print(data)


spider("Blog")
spider("News")
spider("Fucher")


# def get_pages(site_name):
#
#     print("Get pages for {}".format(site_name))
#     return range(1, 4)
#
#
# get_pages("what")
# a = get_pages("what")
# print(a)
#
# for i in a:
#     print(i)
#
#
# for i in a:
#     print("12")


