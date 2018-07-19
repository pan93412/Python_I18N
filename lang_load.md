# Python I18N 簡易模組
gettext 的設定十分繁瑣，對於一些小型專案來說實在沒有必要，希望這個簡單的 I18N 模組能讓你的程式能真正 I18N 化。

## 初始化模組
1. 從 Git 庫下載 lang_load.py，並放置於您程式的根目錄。
2. 確定放置完成後，在程式碼最上方插入以下的程式碼即可。

   ```
   from lang_load import i18nfunc
   ```

## 說明
### 初始化
插入 `i18n = i18nfunc("原始語系檔名", "翻譯語系檔名")` 即完成初始化作業。

> 可以不放「翻譯語系檔名」，代表著始終使用原始語系。

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

### i18n 工具邏輯原則
- 先抓翻譯語系檔案，再抓原始語系檔案
- 如果翻譯語系檔案沒有某字串，那就會採用原始語系的字串。

## 實做
假設原始語系檔名為 original_lang.py，翻譯成中文的語系檔案是
chinese_lang.py。

`main.py`：

```
#!/bin/python3
#-*- coding: utf-8 -*-
from lang_load import i18nfunc

i18n = i18nfunc("original_lang.py", "chinese_lang.py")

# Main Program
print(i18n.str("helloworld"))
print(i18n.str("whatsup"))
```

`original_lang.py`：

```
# Original Language File
helloworld = "Hello World!"
whatsup = "What's up?"
```

`chinese_lang.py`：

```
# Chinese LangFile
helloworld = "哈囉世界！"
```

執行結果：

```
哈囉世界！
What's up?
```

## 製作者
- [pan93412](http://www.github.com/pan93412) (主開發者)
- [cxumol](http://www.github.com/cxumol) (開發指引)