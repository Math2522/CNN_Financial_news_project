# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 08:55:39 2017

@author: au483134
"""

import os
os.chdir(r'C:\Users\au483134\Desktop\20061020_20131126_bloomberg_news\2006-10-20')

list_ = open('inco-s-net-soars-on-higher-metal-prices-breakup-fee-update4-.txt').read().split()

import gensim
import logging

os.chdir(r'C:\Users\au483134\Desktop')
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary = True)

logging.basicConfig(format='%(asctime)s : %levelname)s : %(message)s', level=logging.INFO)

print("Does it include the stop words like \'a\', \'and\', \'the\'? %d %d %d" % ('a' in model.vocab, 'and' in model.vocab, 'the' in model.vocab ))

vocab = model.vocab.keys()
