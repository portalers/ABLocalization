translate Tchinese python:

## 字體設定頁面 ########################################################

## 綁定對話字體粗體
    config.font_replacement_map["fonts/SourceHanSerifTW-Regular.otf", True, False] = ("fonts/SourceHanSerifTW-Bold.otf", False, False)

## 文本對話字體
    gui.text_font = gui.preference("font_a", "fonts/SourceHanSerifTW-Regular.otf")

## 角色名稱字體
    gui.name_text_font = gui.preference("font_b", "fonts/TW+PlayfairDisplaySCBold.ttf")

## 遊戲簡介界面字體
    gui.interface_text_font = gui.preference("font_C", "fonts/SourceHanSerifTW-Bold.otf")

## 選項字體和按鈕字體
    gui.button_text_font = gui.interface_text_font
    gui.choice_button_text_font = gui.interface_text_font

## Renpy系統界面字體
    gui.system_font = gui.interface_text_font

## 調整默認文本播放速度
    preferences.text_cps = 15

## 更改選擇點字體大小
    gui.choice_button_text_size = 36

## 安卓界面配置微調
    if renpy.variant("small"):
        gui.text_size = 43
        gui.dialogue_width = 1230
        gui.label_text_size = 42
        gui.button_text_size = 37
        gui.interface_text_size = 42
        gui.history_name_xpos = 0.15
        gui.history_height = 285
        gui.history_text_width = 1035
        ## Quick buttons.
        gui.quick_button_text_size = 50
        gui.quick_button_borders = Borders(45, 5, 45, 8)  

## PC界面配置微調
    if renpy.variant("pc"):
        gui.text_size = 36
        gui.quick_button_text_size = 30
        gui.quick_button_borders = Borders(30, 6, 30, 15)
