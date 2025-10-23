translate Schinese python:

## 字体设定页面 ########################################################

## 绑定对话字体粗体
    config.font_replacement_map["fonts/SourceHanSerifCN-Regular.otf", True, False] = ("fonts/SourceHanSerifCN-Bold.otf", False, False)

## 文本对话字体
    gui.text_font = gui.preference("font_a", "fonts/SourceHanSerifCN-Regular.otf")

## 角色名称字体
    gui.name_text_font = gui.preference("font_b", "fonts/CN+PlayfairDisplaySCBold.ttf")

## 游戏简介界面字体
    gui.interface_text_font = gui.preference("font_C", "fonts/SourceHanSerifCN-Bold.otf")

## 选项字体和按钮字体
    gui.button_text_font = gui.interface_text_font
    gui.choice_button_text_font = gui.interface_text_font

## Renpy系统界面字体
    gui.system_font = gui.interface_text_font

## 调整默认文本播放速度
    preferences.text_cps = 15

## 更改选择点字体大小
    gui.choice_button_text_size = 36

## 安卓界面配置微调
    if renpy.variant("small"):
        gui.text_size = 38
        gui.dialogue_width = 1230
        gui.label_text_size = 37
        gui.button_text_size = 15
        gui.interface_text_size = 37
        gui.history_name_xpos = 0.15
        gui.history_height = 285
        gui.history_text_width = 1035
        ## Quick buttons.
        gui.quick_button_text_size = 39
        gui.quick_button_borders = Borders(45, 5, 45, 8)  

## PC界面配置微调
    if renpy.variant("pc"):
        gui.text_size = 30
        gui.quick_button_text_size = 16
        gui.quick_button_borders = Borders(30, 6, 30, 8)
