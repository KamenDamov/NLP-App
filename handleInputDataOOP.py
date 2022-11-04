#OOP script that will handle the choice of jupyter notebook script wanted
from os import link


class NLPApp: 
    #Create pipeline that will analyze the digitalized data
    import numpy as np
    import pandas as pd
    from textblob import TextBlob
    import nltk
    import seaborn as sns
    import matplotlib.pyplot as plt 

    import functools as f
    from wordcloud import WordCloud
    #Preprocessing the data
    import string
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    from nltk.util import ngrams

    from youtube2text import Youtube2Text
    import subprocess
    from ibm_watson import SpeechToTextV1
    from ibm_watson.websocket import RecognizeCallback, AudioSource
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
    import pysrt

    import os
    import speech_recognition as sr
    import ffmpeg

    def __init__(self, *args):
        link = ""
        if isinstance(link, str, ngram, ):
