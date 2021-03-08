Adresses = ['https://www.delfi.lv', 'https://www.google.co.uk', 'https://www.wikipedia.org',
            'https://www.lattelecom.lv', 'http://www.optimalit.net']


def top_level_domain(lst):  # 1. variants
    my_list = []
    for item in lst:
        my_list.append(item.split(".")[-1])
    return "Top level domains: " + str(list(set(my_list)))  # Domains shouldn't repeat?


def top_level_domain2(lst):  # 2. variants
    my_list = []
    for item in lst:
        my_list.append(item[item.rindex('.') + 1:])
    return "Top level domains: " + str(list(set(my_list)))


print(top_level_domain(Adresses))
# print(top_level_domain2(Adresses))
