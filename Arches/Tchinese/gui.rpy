# OBSOLETE
translate Tchinese python:
## 字體設定頁面 ########################################################

## 文本對話字體
    gui.text_font = "ui/Yozai-Regular.ttf"

## 遊戲簡介界面字體
    gui.interface_text_font = gui.button_text_font = "ui/GenSenRounded-B.ttc"

## 選項字體和按鈕字體
    gui.button_text_font = "ui/GenSenRounded-B.ttc"
    gui.choice_button_text_font = "ui/GenSenRounded-B.ttc"

## Renpy系統界面字體
    gui.system_font = "ui/GenSenRounded-B.ttc"

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
