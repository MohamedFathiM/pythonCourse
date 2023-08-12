# group , flags

import re

my_website = "http://www.youtube.com/watch?v=MLb7pPOEJlg&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs&index=102"
search = re.search('(https?)://(www)?\.?(\w+)\.(com|org|net):?(\d+)?/?(.+)?',my_website)
# search = re.search('(https?)://(www)?\.?(\w+)\.(com|org|net):?(\d+)?/?(.+)?',my_website,re.M) # using flags

print(search.groups())
print("*" * 10)
print(search.group(1))
print("*" * 10)
print(f"Protocol => {search.group(1)} , Sub Domain =>{search.group(2)} , Domain Name {search.group(3)} , Top Level Domain => {search.group(4)} , Port => {search.group(5)} , Query String => {search.group(6)}")
