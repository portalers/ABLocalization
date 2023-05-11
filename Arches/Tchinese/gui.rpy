translate Tchinese python:
## 字體設定頁面 ########################################################

## 綁定對話字體粗體
    config.font_replacement_map["font/SourceHanSansTW-Normal.otf", True, False] = ("font/SourceHanSansTW-Bold.otf", False, False)

## 文本對話字體
    gui.text_font = "font/SourceHanSansTW-Normal.otf"

## 遊戲簡介界面字體
    gui.interface_text_font = gui.text_font

## 選項字體和按鈕字體
    gui.button_text_font = gui.text_font
    gui.choice_button_text_font = gui.text_font

## Renpy系統界面字體
    gui.system_font = gui.text_font

## 調整默認文本播放速度
    preferences.text_cps = 15

## 調整主界面字體大小
    if renpy.variant("pc"):
        gui.text_size = 36
        gui.button_text_size = 36
        gui.choice_button_text_size = 36
        gui.quick_button_borders = Borders(30, 6, 30, 15)

## 調整安卓底欄按鈕大小&文本框長度
    if renpy.variant("small"):
        gui.dialogue_width = 1230
        gui.quick_button_text_size = 50
