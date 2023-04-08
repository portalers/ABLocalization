translate Tchinese python:
## 字體設定頁面 ########################################################

## 綁定對話字體粗體
##    config.font_replacement_map["font/SourceHanSerifCN-Regular.otf", True, False] = ("font/SourceHanSerifCN-Bold.otf", False, False)

## 文本對話字體
    gui.text_font = "font/SourceHanSansTW-Normal.otf"
## 角色名稱字體
    gui.name_text_font = "font/FZYZ.ttf"

## 遊戲簡介界面字體
    gui.interface_text_font = gui.name_text_font

## 選項字體和按鈕字體
    gui.button_text_font = gui.name_text_font
    gui.choice_button_text_font = gui.text_font

## Renpy系統界面字體
    gui.system_font = gui.text_font

## 調整默認文本播放速度
    preferences.text_cps = 15

## 調整主界面字體大小
    gui.button_text_size = 45
    gui.label_text_size = 45
    gui.name_text_size = 62