## credits.rpy

# Этот файл управляет концовкой DDLC и вашей модификации!

# Эти определения изображений показывают сценки, которые можно было увидеть в игре,
# а затем, если игра была пройдена не на 100%, происходит их «удаление» из титров.
image credits_cg1:
    "images/cg/credits/1.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2:
    "images/cg/credits/2.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3:
    "images/cg/credits/3.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4:
    "images/cg/credits/4.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5:
    "images/cg/credits/5.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6:
    "images/cg/credits/6.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7:
    "images/cg/credits/7.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8:
    "images/cg/credits/8.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9:
    "images/cg/credits/9.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10:
    "images/cg/credits/10.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

# Эти определения изображений показывают неувиденные сценки в игре, а затем происходит
# их «удаление» из титров.
image credits_cg1_locked:
    "images/cg/credits/1b.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2_locked:
    "images/cg/credits/2b.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3_locked:
    "images/cg/credits/3b.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4_locked:
    "images/cg/credits/4b.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5_locked:
    "images/cg/credits/5b.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6_locked:
    "images/cg/credits/6b.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7_locked:
    "images/cg/credits/7b.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8_locked:
    "images/cg/credits/8b.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9_locked:
    "images/cg/credits/9b.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10_locked:
    "images/cg/credits/10b.png"
    xysize (640, 360)
    8.6
    "images/menu/notfound.png"

# Эти определения изображений показывают все просмотренные сценки в игре,
# и их «удаление» из титров НЕ происходит, т.к. игра была пройдена на 100%.
image credits_cg1_clearall:
    "images/cg/credits/1.png"
    xysize (640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    xysize (640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    xysize (640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    xysize (640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    xysize (640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    xysize (640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    xysize (640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    xysize (640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    xysize (640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.png"
    xysize (640, 360)

# Это определение изображения показывает логотип DDLC с применёнными к нему трансформациями.
image credits_logo:
    "gui/logo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

# Это определение изображения показывает логотип Team Salvato с применёнными к нему трансформациями.
image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

# Этот стиль объявляет оформление заголовков (роль человека в разработке игры)
# в титрах.
style credits_header:
    font "gui/font/v_CCBellyLaugh.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

# Этот стиль объявляет оформление абзацев (имя/прозвище человека, участвовавшего
# в разработке игры) в титрах.
style credits_text:
    font "gui/font/comic.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

# Этот стиль объявляет оформление текста песни Моники в титрах.
style monika_credits_text:
    font "gui/font/Adventure.ttf"
    color "#fff"
    size 30
    text_align 0.5
    line_leading 1
    outlines []

# Это определение изображения показывает заголовки в титрах (напр. «Концепция и дизайн игры»).
image credits_header = ParameterizedText(style="credits_header", ypos=-40)

# Это определение изображения показывает абзацы в титрах (напр. «Дэн Салвато»).
image credits_text = ParameterizedText(style="credits_text", ypos=40)

# Прим. пер.: эти определения изображений взяты из русификатора от Энтузиасты Team
# и необходимы для корректного отображения текста в титрах

# Заголовки, два человека
image credits_header2 = ParameterizedText(style="credits_header", ypos=-55)

# Абзацы, два человека
image credits_text2 = ParameterizedText(style="credits_text", ypos=30)

# Заголовки, три человека
image credits_header_3 = ParameterizedText(style="credits_header", ypos=-85)

# Абзацы, три человека
image credits_text_3 = ParameterizedText(style="credits_text", ypos=30)

# Заголовки, пять человек
image credits_header_5 = ParameterizedText(style="credits_header", ypos=-140)

# Абзацы, пять человек
image credits_text_5 = ParameterizedText(style="credits_text", ypos=25)

# Это определение изображения показывает текст песни Моники в титрах.
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)

# Эта трансформация управляет анимацией прокручивания титров.
transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

# Эта трансформация управляет анимацией прокручивания текста титров.
transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

# Эта трансформация управляет анимацией прокручивания чибиков в титрах.
transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

# Эта трансформация управляет анимацией прокручивания титров справа.
transform credits_scroll_right:
    xalign 0.9
    credits_scroll

# Эта трансформация управляет анимацией прокручивания титров слева.
transform credits_scroll_left:
    xalign 0.1
    credits_scroll

# Эта трансформация управляет анимацией прокручивания текста титров справа.
transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

# Эта трансформация управляет анимацией прокручивания текста титров слева.
transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

# Эта трансформация управляет анимацией чибика Сайори в титрах.
transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll

# Эта трансформация управляет анимацией чибика Нацуки в титрах.
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll

# Эта трансформация управляет анимацией чибика Юри в титрах.
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll

# Эта трансформация управляет анимацией чибика Моники в титрах.
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

# Эта переменная указывает позицию текста песни Моники по вертикали.
define credits_ypos = 250

# Эти изображения с трансформациями показывают текст песни «Твоя реальность»,
# исполняемой Моникой.
image mcredits_1a:
    ypos credits_ypos
    xoffset -340
    "black"
    10.33
    Text("День за днём,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.5, ramplen=4, alpha=False)

image mcredits_1b:
    ypos credits_ypos
    xoffset -30
    "black"
    11.75
    Text("строю мир в голове, где будем", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 7.0, ramplen=4, alpha=False)

image mcredits_1c:
    ypos credits_ypos
    xoffset 307
    "black"
    13.76
    Text("лишь мы с тобой.", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_2a:
    ypos credits_ypos + 50
    xoffset -340
    "black"
    19.45
    Text("На листе", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.5, ramplen=4, alpha=False)

image mcredits_2b:
    ypos credits_ypos + 50
    xoffset -60
    "black"
    20.9
    Text("пером выведу стих, в котором", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 7.0, ramplen=4, alpha=False)

image mcredits_2c:
    ypos credits_ypos + 50
    xoffset 285
    "black"
    23.27
    Text("ты здесь, со мной.", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("Тёмной лужей чернила вдруг стали,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.5, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    "black"
    32.9
    Text("Просто пиши - дай им стать большой рекой.", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 7.5, ramplen=4, alpha=False)

image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("В мире, где миллионы решений,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 11.5, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -185
    "black"
    42.0
    Text("Куда же плыть", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 6.5, ramplen=4, alpha=False)

image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 110
    "black"
    43.47
    Text("вместе с нею за мечтой?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 6.5, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

# Это определение изображения является остатками кода текста песни Моники
# из тестовой версии DDLC.
image mcredits_1_test:
    ypos credits_ypos + 300
    Text("Какой же путь вместе нас сведёт с тобой?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4)

# Эти определения изображений показывают искажённое изображение Моники со стихотворением перед началом титров.
image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

# Этот лейбл запускает первую часть титров с Моникой.
label credits:
    # Это объявление переменной указывает, что если вдруг игрок закрыл игру,
    # при следующем запуске начнутся титры.
    $ persistent.autoload = "credits" 

    # Эта команда сохраняет постоянные данные игры в отдельный файл.
    $ renpy.save_persistent()

    # Нижеследующие команды отвязывают горячие клавиши вызова Игрового меню и скрытия
    # диалогового окна, а затем идёт обновление кэша привязок для вступления изменений в силу.
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()

    # Эти объявления переменных блокируют функцию Пропуска и доступ к Быстрому меню,
    # пока идут титры.
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False

    scene black

    # Эта команда воспроизведения запускает диалог Моники в титрах.
    play music "bgm/end-voice.ogg" noloop

    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    show end_glitch1 zorder 2
    show black as bar zorder 9:
        alpha 0.3
        xysize (1280,500)
        block:
            ypos 720
            linear 15 ypos -500
            repeat

    pause 39
    scene black
    pause 0.5
    $ run_input(__("renpy.music.play(\"ddlc.ogg\")"), __("Воспроизведение \"ddlc.ogg\"..."))
    pause 1.0
    hide screen console_screen
    # Эта команда воспроизведения запускает «Твоя реальность» и играет его ровно 50 секунд.
    play music "<to 50.0>bgm/credits.ogg" noloop

    # В этом разделе выводятся на экран строчки из текста песни.
    show mcredits_1a zorder 50
    show mcredits_1b zorder 49
    show mcredits_1c zorder 48
    show mcredits_2a zorder 47
    show mcredits_2b zorder 46
    show mcredits_2c zorder 45
    show mcredits_3 zorder 44
    show mcredits_4 zorder 43
    show mcredits_5 zorder 42
    show mcredits_6a zorder 41
    show mcredits_6b zorder 40
    show mcredits_7 zorder 51

    pause 50
    jump credits2

# Этот лейбл запускает вторую часть титров с командой разработчиков.
label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    play music "<from 50.0>bgm/credits.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    pause 9.12

    # Эти объявления переменных и команда отображения определяют, какая сценка в титрах
    # будет показана цветной или чёрно-белой (неоткрытой) и будет ли она удалена впоследствии.
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    show expression f"credits_cg1{lockedtext}" as credits_image_1 at credits_scroll_right

    # Эти команды отображения показывают заголовок (роль человека в разработке
    # игры) и абзац (имя/прозвище человека, участвовавшего в разработке игры) титров.
    # Прим. пер.: обязательно учитывайте кол-во людей в абзаце, иначе текст будет отображаться некорректно.
    show credits_header "Концепция и дизайн игры" as credits_header_1 at credits_text_scroll_left
    show credits_text "Дэн Салвато" as credits_text_1 at credits_text_scroll_left

    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        $ run_input("os.remove(\"images/cg/n_cg1.png\")", __("Удалено: \"n_cg1.png\"."))
    else:
        $ pause(len("os.remove(\"images/cg/n_cg1.png\")") / 30.0 + 0.5)
    show expression f"credits_cg2{lockedtext}" as credits_image_2 at credits_scroll_left

    show credits_header "Художник по персонажам" as credits_header_2 at credits_text_scroll_right
    show credits_text "Satchely" as credits_text_2 at credits_text_scroll_right

    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        $ run_input("os.remove(\"images/cg/n_cg2.png\")", __("Удалено: \"n_cg2.png\"."))
    else:
        $ pause(len("os.remove(\"images/cg/n_cg2.png\")") / 30.0 + 0.5)
    show expression f"credits_cg3{lockedtext}" as credits_image_1 at credits_scroll_right

    show credits_header "Художник по фонам" as credits_header_1 at credits_text_scroll_left
    show credits_text "Velinquent" as credits_text_1 at credits_text_scroll_left

    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        $ run_input("os.remove(\"images/cg/y_cg1.png\")", __("Удалено: \"y_cg1.png\"."))
    else:
        $ pause(len("os.remove(\"images/cg/y_cg1.png\")") / 30.0 + 0.5)
    show expression f"credits_cg4{lockedtext}" as credits_image_2 at credits_scroll_left

    show credits_header "Автор сценария" as credits_header_2 at credits_text_scroll_right
    show credits_text "Дэн Салвато" as credits_text_2 at credits_text_scroll_right

    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        $ run_input("os.remove(\"images/cg/y_cg2.png\")", __("Удалено: \"y_cg2.png\"."))
    else:
        $ pause(len("os.remove(\"images/cg/y_cg2.png\")") / 30.0 + 0.5)
    show expression f"credits_cg5{lockedtext}" as credits_image_1 at credits_scroll_right

    show credits_header "Композитор" as credits_header_1 at credits_text_scroll_left
    show credits_text "Дэн Салвато" as credits_text_1 at credits_text_scroll_left

    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(54.30 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        $ run_input("os.remove(\"images/cg/n_cg3.png\")", __("Удалено: \"n_cg3.png\"."))
    else:
        $ pause(len("os.remove(\"images/cg/n_cg3.png\")") / 30.0 + 0.5)
    show expression f"credits_cg6{lockedtext}" as credits_image_2 at credits_scroll_left

    show credits_header2 "Исполнители песни" as credits_header_2 at credits_text_scroll_right
    show credits_text2 "Джиллиан Эшкрафт\nAka" as credits_text_2 at credits_text_scroll_right

    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(63.10 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        $ run_input("os.remove(\"images/cg/y_cg2.png\")", __("Удалено: \"y_cg2.png\"."))
    else:
        $ pause(len("os.remove(\"images/cg/y_cg2.png\")") / 30.0 + 0.5)
    show expression f"credits_cg7{lockedtext}" as credits_image_1 at credits_scroll_right

    show credits_header_5 "Перевод оригинала" as credits_header_1 at credits_text_scroll_left
    show credits_text_5 "Erizo\nMamavl\nDOOMer\nFibYar\nAka" as credits_text_1 at credits_text_scroll_left

    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(71.30 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        $ run_input("os.remove(\"images/cg/s_cg1.png\")", __("Удалено: \"s_cg1.png\"."))
    else:
        $ pause(len("os.remove(\"images/cg/s_cg1.png\")") / 30.0 + 0.5)
    show expression f"credits_cg8{lockedtext}" as credits_image_2 at credits_scroll_left

    show credits_header_3 "Особая благодарность" as credits_header_2 at credits_text_scroll_right
    show credits_text_3 "Маша Гутин\nKagefumi\nДэвид Ивлин" as credits_text_2 at credits_text_scroll_right

    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.clearall:
        $ run_input("os.remove(\"images/cg/s_cg2.png\")", __("Удалено: \"s_cg2.png\"."))
    else:
        $ pause(len("os.remove(\"images/cg/s_cg2.png\")") / 30.0 + 0.5)
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show expression f"credits_cg9{lockedtext}" as credits_image_1 at credits_scroll_right

    show credits_header_3 "Особая благодарность" as credits_header_1 at credits_text_scroll_left
    show credits_text_3 "Кори Шин\nАлесия Бардачино\nМэтт Нэплс" as credits_text_1 at credits_text_scroll_left

    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        $ run_input("os.remove(\"images/cg/s_cg3.png\")", __("Удалено: \"s_cg3.png\"."))
    else:
        $ pause(len("os.remove(\"images/cg/s_cg3.png\")") / 30.0 + 0.5)
    show expression f"credits_cg10{lockedtext}" as credits_image_2 at credits_scroll_left

    show credits_header "Особая благодарность" as credits_header_2 at credits_text_scroll_right
    show credits_text "Моника\n[player]" as credits_text_2 at credits_text_scroll_right

    $ pause(103.50 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        $ run_input("os.remove(\"images/cg/m_cg1.png\")", __("Удалено: \"m_cg1.png\"."))
    else:
        $ pause(len("os.remove(\"images/cg/m_cg1.png\")") / 30.0 + 0.5)

    $ run_input("os.remove(\"game/screens.rpy\")", __("Удалено: \"screens.rpy\"."))
    $ run_input("os.remove(\"game/gui.rpy\")", __("Удалено: \"gui.rpy\"."))
    $ run_input("os.remove(\"game/menu.rpy\")", __("Удалено: \"menu.rpy\"."))
    $ run_input("os.remove(\"game/script.rpy\")", __("Удалено: \"script.rpy\"."))
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())

    hide screen console_screen
    show credits_ts
    show credits_text "сделано с любовью":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3
    play sound page_turn
    show poem_end with Dissolve(1)

    # Этот лейбл запускает цикл с концом игры и выводит на экран прощальное письмо Моники или особенное письмо Дэна,
    # а при нажатии любой клавиши, которая должна в теории пролистать текст дальше - выводит ложное окно с сообщением
    # о повреждении/отсутствии файлов и единственной кнопкой, которая закрывает игру.
    label postcredits_loop:
        $ persistent.autoload = "postcredits_loop"
        $ renpy.save_persistent()
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False

        scene black

        # Эта команда отображения показывает прощальное письмо Моники или особенное письмо Дэна.
        show poem_end
        # Эта команда ставит пропускаемую паузу.
        $ pause()

        # Эта команда показа экрана выводит на экран ложное окно с сообщением
        # о повреждении/отсутствии файлов и единственной кнопкой, которая закрывает игру.
        call screen dialog("Ошибка: некоторые файлы повреждены или отсутствуют.\nПереустановите игру.", Quit(confirm=False))
        return
