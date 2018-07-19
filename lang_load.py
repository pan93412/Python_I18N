#!/bin/python3
#-*- coding: utf-8 -*-
# author: pan93412, cxumol
# DO NOT REMOVE AUTHOR INFORMATION!

# lang_load.py 可以被修改。你可以在這裡
# 修改顯示出的文字。
origlang_not_found = "[ERR] 原始語系檔案不存在！"
values_not_found = "[ERR] 找不到對應的字串！"

import os
class i18nfunc:
    '''
    i18n 函式。
    初始化：i18nfunc(原始語言檔案, [翻譯語言檔案])
    載入字串：str(翻譯字串 ID)
    '''
    def __init__(self, origlang, langfile=False):
        '''
        透過 i18nfunc(原始語言檔案, 翻譯語言檔案) 初始化 i18n
        翻譯語言檔案非必要，即代表始終使用原始語言。

        若原始語系不存在，則返回錯誤 ModuleNotFoundError。

        若翻譯語系檔案定義錯誤，則忽略改使用原始語言檔案。
        '''
        if os.path.exists(origlang):
            exec("import " + origlang[:-3] + " as origlang")
            self.module = locals()['origlang']
        else:
            raise ModuleNotFoundError(origlang_not_found)
        if langfile != False:
            if os.path.exists(langfile):
                exec("import " + langfile[:-3] + " as langf")
                self.langmod = locals()['langf']
    
    def str(self, strid):
        '''
        載入語言檔案中相對應的字串。
        若翻譯語言的某字串未找到，則返回原始翻譯語言的字串。
        若原始翻譯語言亦未找到字串，則發生 NameError 錯誤。
        '''
        try:
            return eval("self.langmod." + strid)
        except:
            try:
                return eval("self.module." + strid)
            except:
                raise NameError(values_not_found)