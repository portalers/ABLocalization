## Ruby效果微調
style ruby_style is default:
    size 20
    yoffset -34

style history_ruby_style is default:
    size 20
    yoffset -29

style say_dialogue:
    line_leading 5
    ruby_style style.ruby_style


style history_text:
    line_leading 5
    ruby_style style.history_ruby_style

## 本地化配置文件
translate Tchinese python:
    config.font_replacement_map["font/SourceHanSerifTW-Regular.otf", True, False] = ("font/SourceHanSerifTW-Bold.otf", False, False)
    gui.system_font = gui.main_font = gui.text_font = gui.name_text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = "font/SourceHanSerifTW-Regular.otf"
    preferences.text_cps = 15
    if renpy.variant("pc"):
        ## Font sizes.
        gui.text_size = 36
        gui.button_text_size = 36
        gui.choice_button_text_size = 36
    if renpy.variant("small"):
        ## Adjust dialogue.
        gui.dialogue_width = 1230
        gui.label_text_size = 51
        gui.button_text_size = 36
        gui.history_name_xpos = 0.15
        gui.history_height = 285
        gui.history_text_width = 1035
        ## Quick buttons.
        gui.quick_button_text_size = 50