import nltk
import json
from nltk.corpus import wordnet as wn

# nltk.data.path.append("/tmp")
# nltk.download("wordnet", download_dir = "/tmp")

# def pairings(source):
#   result = []
#   for p1 in range(len(source)):
#           for p2 in range(p1+1, len(source)):
#                   result.append([source[p1],source[p2]])
#   return result

# def parseWordsFromQuery(queryString):
#     if not "words" in queryString:
#         return None
#     return [w.strip() for w in queryString["words"].split(',')]

def handler(event, context):
    return event