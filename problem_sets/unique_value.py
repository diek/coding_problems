#!/bin/python3

import json

# import math
# import random
# import re
# import sys
from operator import itemgetter

import requests


def topArticles(limit):
    url = f"https://jsonmock.hackerrank.com/api/articles?page={limit}"
    response = requests.get(url)
    api_data = json.loads(response.text)
    api_data.sort(key=itemgetter("num_comments"))
    titles = []
    for idx in range(limit + 1):
        for k, y in api_data["data"][idx].items():
            if k == "title":
                titles.append(y)

    return titles


# title UK votes to leave EU
# url http://www.bbc.co.uk/news/uk-politics-36615028
# author dmmalam
# num_comments 2531
# story_id None
# story_title None
# story_url None
# parent_id None
# created_at 1466740137


if __name__ == "__main__":
    limit = int(input().strip())
    result = topArticles(limit)
    for title in result:
        print(title)
