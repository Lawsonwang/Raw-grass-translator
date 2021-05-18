from google_trans_new import google_translator
import json

#translator = google_translator(proxies={'http':'113.194.19.200:9999', 'http':'114.239.1.124', 'http':'118.212.104.84'})

translator = google_translator()

lans = ['ar', 'vi', 'ja', 'ru', 'eo', 'my', 'it', 'tt', 'tg', 'zh-CH']

def fanyi(s, from_='auto', to='auto'):
    return translator.translate(s, lang_tgt=to, lang_src=from_)

tmp = None
with open('grass_text.txt', 'r', encoding='utf-8') as f:
    tmp = f.read()

n = len(lans)
for i in range(n):
    tmp = fanyi(tmp, to=lans[i])
    print(i + 1, '/', n)

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(tmp)
