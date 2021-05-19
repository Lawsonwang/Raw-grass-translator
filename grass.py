from google_trans_new import google_translator
import random
import json

#translator = google_translator(proxies={'http':'113.194.19.200:9999', 'http':'114.239.1.124', 'http':'118.212.104.84'})

translator = google_translator()

tmp = None
with open("lan.txt", encoding='utf-8') as f:
    tmp = f.read()

tmp = json.loads(tmp)['text']

lans = []
for each in tmp:
    lans.append(each[0])

def fanyi(s, from_='auto', to='auto'):
    return translator.translate(s, lang_tgt=to, lang_src=from_)

tmp = None
with open('grass_text.txt', 'r', encoding='utf-8') as f:
    tmp = f.read()

randshuf = input('是否随机生草 (y/n)：')

if randshuf[0] == 'y':
    random.shuffle(lans)

n = int(input('请输入生草翻译次数（包括翻译回中文，建议不要太大）：'))

for i in range(n - 1):
    tmp = fanyi(tmp, to=lans[i])
    print(i + 1, '/', n)

tmp = fanyi(tmp, to='zh-CN')
print(n, '/', n)

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(tmp)

print('生草完成！结果在 result.txt')
