translate Tchinese python:
    config.font_replacement_map["font/SourceHanSansTC-Normal.otf", True, False] = ("font/SourceHanSansTC-Bold.otf", False, False)
    gui.system_font = gui.main_font = gui.text_font = gui.name_text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = "font/SourceHanSansTC-Normal.otf"
    preferences.text_cps = 14

    if renpy.variant("pc"):
        ## Font sizes.
        gui.text_size = 36
        gui.button_text_size = 36
        gui.choice_button_text_size = 36
    if renpy.variant("small"):
        ## Adjust dialogue.
        gui.dialogue_width = 1230
        gui.label_text_size = 51
        gui.history_name_xpos = 0.15
        ## 优化安卓版存档缩略图大小
        gui.slot_button_width = 400
        gui.slot_button_height = 240
        config.thumbnail_width = 384
        config.thumbnail_height = 216
        gui.history_height = 285
        gui.history_text_width = 1035
        ## Quick buttons.
        gui.quick_button_text_size = 50