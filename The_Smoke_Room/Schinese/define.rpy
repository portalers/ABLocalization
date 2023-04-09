translate Schinese python:
    config.font_replacement_map["font/SourceHanSerifCN-Regular.otf", True, False] = ("font/SourceHanSerifCN-Bold.otf", False, False)
    gui.system_font = gui.main_font = gui.text_font = gui.name_text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = "font/SourceHanSerifCN-Regular.otf"
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