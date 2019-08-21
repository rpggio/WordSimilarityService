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

def handler(event, context):
    words = ['car', 'jet', 'dog', 'wheel', 'pizza', 'airport', 'city', 'friend']
    synsets = [{ "word": w, "lemma": wn.synsets(w, 'n')[0] } for w in words]
    pairs = pairings(synsets)
    similarities = [[p[0]["word"], p[1]["word"], p[0]["lemma"].wup_similarity(p[1]["lemma"])] for p in pairs]

    return list(similarities)
