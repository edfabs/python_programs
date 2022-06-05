from collections import OrderedDict

favorite_lenguages = OrderedDict()

favorite_lenguages['jen'] = 'python'
favorite_lenguages['sarah'] = 'c'
favorite_lenguages['edward'] = 'ruby'
favorite_lenguages['phil'] = 'python'

for name, language in favorite_lenguages.items():
    print(name.title() + "'s favorite lenguage is " + language.title() + ".")
