# OBSOLETE
translate Schinese python:
## 字体设定页面 ########################################################

## 绑定对话字体粗体
    config.font_replacement_map["font/SourceHanSansCN-Normal.otf", True, False] = ("font/SourceHanSansCN-Bold.otf", False, False)

## 文本对话字体
    gui.text_font = "font/SourceHanSansCN-Normal.otf"

## 游戏简介界面字体
    gui.interface_text_font = gui.text_font

## 选项字体和按钮字体
    gui.button_text_font = gui.text_font
    gui.choice_button_text_font = gui.text_font

## Renpy系统界面字体
    gui.system_font = gui.text_font

## 调整默认文本播放速度
    preferences.text_cps = 15

## 调整主界面字体大小
    if renpy.variant("pc"):
        gui.text_size = 36
        gui.button_text_size = 36
        gui.choice_button_text_size = 36
        gui.quick_button_borders = Borders(30, 6, 30, 15)

## 调整安卓底栏按钮大小&文本框长度
    if renpy.variant("small"):
        gui.dialogue_width = 1230
        gui.quick_button_text_size = 50
