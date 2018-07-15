# Python I18N 簡易元件
author = pan93412

## 初始化
在 python 程式碼內插入這一段，或是建立一個檔案後
用 `from 檔案 import i18nfunc`。

```
import os
class i18nfunc:
    '''i18n 函式'''
    def __init__(self, origlang, langfile=False):
        '''透過 i18nfunc(原始語言檔案, 翻譯語言檔案) 初始化 i18n'''
        if os.path.exists(origlang):
            exec("import " + origlang[:-3] + " as lango")
            self.module = locals()['lango']
        else:
            print("DEBUG: origlang is invaild!")
        if langfile != False:
            if os.path.exists(langfile):
                exec("import " + langfile[:-3] + " as langf")
                self.langmod = locals()['langf']
            else:
                print("DEBUG: langfile is invaild!")
    def str(self, strid):
        '''載入語言檔案中相對應的字串'''
        try:
            return eval("self.langmod." + strid)
        except:
            return eval("self.module." + strid)
```

## 說明
### 初始化
輸入 `i18n = i18nfunc("原始語系檔名", "翻譯語系檔名")` 即完成初始化作業。

> Tip: 可以不放「翻譯語系檔名」，代表著始終使用原始語系。

### 語系檔案
語系檔案須以 .py 為副檔名。

原始語系檔案（假設 orig_lang.py）：

```
helloworld = "Hello World!"
```

翻譯語系檔案（假設 tran_lang.py）：

```
helloworld = "哈囉！世界。"
```

格式就是 `字串 ID = "字串"`。

### 調用字串
用〈初始化〉舉的 i18n 函式和
〈語系檔案〉舉的檔案與字串 ID 為例。

假設我想要取得 helloworld 這個字串 ID，
那就輸入 i18n.str("helloworld")，
其就會回傳 helloworld 的字串檔案。

### 原則
- 先抓翻譯語系檔案，再抓原始語系檔案
- 如果翻譯語系檔案沒有某字串，那就會採用原始語系的字串。

## 實做
假設原始語系檔名為 original_lang.py，翻譯成中文的語系檔案是
chinese_lang.py。

main.py：

```
#!/bin/python3
#-*- coding: utf-8 -*-

# i18n 函式
import os

class i18nfunc:
    '''i18n 函式'''
    def __init__(self, origlang, langfile=False):
        '''透過 i18nfunc(原始語言檔案, 翻譯語言檔案) 初始化 i18n'''
        if os.path.exists(origlang):
            exec("import " + origlang[:-3] + " as lango")
            self.module = locals()['lango']
        else:
            print("DEBUG: origlang is invaild!")
        if langfile != False:
            if os.path.exists(langfile):
                exec("import " + langfile[:-3] + " as langf")
                self.langmod = locals()['langf']
            else:
                print("DEBUG: langfile is invaild!")
    def str(self, strid):
        '''載入語言檔案中相對應的字串'''
        try:
            return eval("self.langmod." + strid)
        except:
            return eval("self.module." + strid)

i18n = i18nfunc("original_lang.py", "chinese_lang.py")

# Main Program
print(i18n.str("helloworld"))
print(i18n.str("whatsup"))
```

original_lang.py：

```
# Original Language File
helloworld = "Hello World!"
whatsup = "What's up?"
```

chinese_lang.py：

```
# Chinese LangFile
helloworld = "哈囉世界！"
```

結果：

```
哈囉世界！
What's up?
```

## 製作者
- [pan93412](http://www.github.com/pan93412) (主開發者)
- [cxumol](http://www.github.com/cxumol) (開發指引)