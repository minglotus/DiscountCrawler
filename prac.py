#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
def group_words(s):
    regex = []

    # Match a whole word:
    regex += [ur'\w+']

    # Match a single CJK character:
    regex += [ur'[\u4e00-\ufaff]']

    # Match one of anything else, except for spaces:
    regex += [ur'[^\s]']

    regex = "|".join(regex)
    r = re.compile(regex)

    return r.findall(s)

if __name__ == "__main__":
    print group_words(u"Testing English text")
    print group_words(u"我爱蟒蛇")
    print group_words(u"Testing English text我爱蟒蛇")
