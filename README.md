# gen_big5_codecs_table

## 緣由

因為有需求要查 Big5 語系的內碼表，結果發現網路上的 Big5 內碼表全都長得不一樣，每一份都對不起來... 也沒說清是哪個版本的內碼表。

只好自己做了一個能夠產出 Big5 語系內碼表的東西，自己對自己的就不會有錯了。

## Big5

Big5碼是一套雙位元組字元集，以兩個位元組來安放一個字。第一個位元組稱為「高位位元組」，第二個位元組稱為「低位位元組」。

「高位位元組」使用了`0x81-0xFE`

「低位位元組」使用了`0x40-0x7E`，及`0xA1-0xFE`。在Big5的分割區中：

位元組結構　|說明|
------|:---:|
0x8140-0xA0FE   |    使用者造字區    |
0xA140-0xA3BF   |    標點符號、希臘字母、特殊符號    |
0xA3C0-0xA3FE   |    保留(不開放造字)    |
0xA440-0xC67E   |    常用漢字    |
0xC6A1-0xC8FE   |    使用者造字區    |
0xC940-0xF9D5   |    次常用漢字    |
0xF9D6-0xF9DC   |    倚天擴充字(碁銹裏墻恒粧嫺)    |
0xF9DD-0xFEFE   |    使用者造字區    |

## Feature and use

```
Default codec is Big5, print result as Markdown style.

optional arguments:

  -h, --help            show this help message and exit

  -c, --codec           The codec you want to generate. ( big5, cp950, big5hkscs )

  -p, --plain           Final result will print as plain text
```

Pirnt `cp950` internal table as Markdown:

`python main.py -c cp950`

Pirnt `big5hkscs` internal table as plain text:

`python main.py -c big5hkscs -p`

## Results

Final result ( markdown style ) at my gists:

[Big5 interal table](https://gist.github.com/Vic-Chang/19e905cff96d633f1573ab9dcebdd1c3)

[cp950 interal table](https://gist.github.com/Vic-Chang/05b7441d95ae49e577ffec2e3e1223fb)

[Big5hkscs interal table](https://gist.github.com/Vic-Chang/0f4e3034723df023ebc028fdd3be9888)
