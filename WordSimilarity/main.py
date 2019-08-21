import nltk
import json
from nltk.corpus import wordnet as wn

nltk.data.path.append("/tmp")
nltk.download("wordnet", download_dir = "/tmp")

def handler(event, context):
    
    print(event)
    print(context)

    return {"message": wn.synsets('cat', 'n')[0].name()}
