import requests
import json

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
    if(len(words) < 2 or len(words) > 30):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "query parameter 'words' must have between 2 and 40 values"
            })
        }

    pairs = pairings(words)
    body = [ [{ "term": p[0] },{ "term": p[1] }] for p in pairs]
    print(data)
    response = requests.request(
        method = "POST",
        url = "http://api.cortical.io/rest/compare/bulk",
        params = {
            "retina_name": "en_associative"
        },
        data = json.dumps(body),
        headers = {
            "content-type": "application/json"
            # "api-key": "c992aea0-c472-11e9-8f72-af685da1b20e"
        }
        )

    responseRows = json.loads(response.text)
    jaccards = [r["jaccardDistance"] for r in responseRows]
    distances = list(zip(pairs, jaccards))
    distances.sort(key=lambda dist: dist[1])

    return { "body": json.dumps(distances) }