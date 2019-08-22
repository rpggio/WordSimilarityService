import nltk
import json
from nltk.corpus import wordnet as wn

nltk.data.path.append("/tmp")
nltk.download("wordnet", download_dir = "/tmp")

def pairings(source):
  result = []
  for p1 in range(len(source)):
          for p2 in range(p1+1, len(source)):
                  result.append([source[p1],source[p2]])
  return result

def parseWordsFromRequest(event):
    if not "queryStringParameters" in event:
        return []
    queryString = event["queryStringParameters"]
    if queryString is None or not "words" in queryString:
        return []
    return [w.strip() for w in queryString["words"].split(',')]

def handler(event, context):
    words = parseWordsFromRequest(event)
    if(len(words) < 2 or len(words) > 40):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "query parameter 'words' must have between 2 and 40 values"
            })
        }

    synsets = [{ "word": w, "lemma": wn.synsets(w, 'n')[0] } for w in words]
    pairs = pairings(synsets)
    similarities = [[p[0]["word"], p[1]["word"], p[0]["lemma"].wup_similarity(p[1]["lemma"])] for p in pairs]

    return {
        "body": json.dumps(list(similarities))
    }
