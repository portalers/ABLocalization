init python:
    config.default_language = "Schinese"
    #修复sin.ttf显示异常
    no_CN = Character('???', color="#ff3333", screen="sayMore", show_col="#ff3333", what_font="fonts/sin_CN.ttf",what_size=55)
    no2_CN = Character('???', color="#255226", screen="sayMore", show_col="#255226", what_font="fonts/sin_CN.ttf",what_size=55)
    nonik_CN = Character('???', color="#ff3333", screen="sayMore", show_col="#ff3333", what_font="fonts/sin_CN.ttf",what_size=55)
    nojack_CN = Character('???', color="#ff3333", screen="sayMore", show_col="#ff3333", what_font="fonts/sin_CN.ttf",what_size=55)
    no_TW = Character('???', color="#ff3333", screen="sayMore", show_col="#ff3333", what_font="fonts/sin_TW.ttf",what_size=55)
    no2_TW = Character('???', color="#255226", screen="sayMore", show_col="#255226", what_font="fonts/sin_TW.ttf",what_size=55)
    nonik_TW = Character('???', color="#255226", screen="sayMore", show_col="#255226", what_font="fonts/sin_TW.ttf",what_size=55)
    nojack_TW = Character('???', color="#255226", screen="sayMore", show_col="#255226", what_font="fonts/sin_TW.ttf",what_size=55)


translate None python:
    if not renpy.variant("pc"):
        gui.button_text_size = 37
    ## 调整默认文本播放速度
    preferences.text_cps = 40
