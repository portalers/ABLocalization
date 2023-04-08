translate Schinese python:
## 字体设定页面 ########################################################

## 绑定对话字体粗体
##    config.font_replacement_map["font/SourceHanSerifCN-Regular.otf", True, False] = ("font/SourceHanSerifCN-Bold.otf", False, False)

## 文本对话字体
    gui.text_font = "font/SourceHanSansCN-Normal.otf"
## 角色名称字体
    gui.name_text_font = "font/FZYZ.ttf"

## 游戏简介界面字体
    gui.interface_text_font = gui.name_text_font

## 选项字体和按钮字体
    gui.button_text_font = gui.name_text_font
    gui.choice_button_text_font = gui.text_font

## Renpy系统界面字体
    gui.system_font = gui.text_font

## 调整默认文本播放速度
    preferences.text_cps = 15

## 调整主界面字体大小
    gui.button_text_size = 45
    gui.label_text_size = 45
    gui.name_text_size = 62