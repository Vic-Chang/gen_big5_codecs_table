# gen_big5_codecs_table

## 緣由

因為有需求要查 Big5 語系的內碼表，結果發現網路上的 Big5 內碼表全都長得不一樣，每一份都對不起來... 也沒說清是哪個版本的內碼表。

只好自己做了一個能夠產出 Big5 語系內碼表的東西，自己對自己的就不會有錯了。

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

## Result

Final result ( markdown style ) at my gists:

[Big5 interal table](https://gist.github.com/Vic-Chang/19e905cff96d633f1573ab9dcebdd1c3)

[cp950 interal table](https://gist.github.com/Vic-Chang/05b7441d95ae49e577ffec2e3e1223fb)

[Big5hkscs interal table](https://gist.github.com/Vic-Chang/0f4e3034723df023ebc028fdd3be9888)