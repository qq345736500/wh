from __future__ import print_function, unicode_literals
import example_helper
import json
from torchmoji.create_vocab import extend_vocab, VocabBuilder
from torchmoji.word_generator import WordGenerator

new_words = ['#zzzzaaazzz', 'newword', 'newword']
word_gen = WordGenerator(new_words)
vb = VocabBuilder(word_gen)
vb.count_all_words()

with open('../model/vocabulary.json') as f:
    vocab = json.load(f)

print(len(vocab))
print(vb.word_counts)
extend_vocab(vocab, vb, max_tokens=1)

# 'newword' should be added because it's more frequent in the given vocab
print(vocab['newword'])
print(len(vocab))