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
        ## Quick buttons.
        gui.quick_button_text_size = 50


