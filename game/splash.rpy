## splash.rpy

# В этом файле хранятся вступительная заставка, отказ от ответственности и прочий код главного меню.

# Это выражение Python проверяет наличие файлов «audio.rpa», «fonts.rpa» и «images.rpa»
# в папке «game» игры и также проверяет, находится ли проект в папке облака (OneDrive).
# Примечание: Для сборки модификации для ПК/Android вам необходимо сохранить RPA-архивы DDLC и
# распаковать их, дабы сборка дистрибутива работала.
init -100 python:
    if not renpy.android:
        for archive in ["audio", "fonts", "images"]:
            if archive not in config.archives:
                raise DDLCRPAsMissing(archive)

        if renpy.windows:
            onedrive_path = os.environ.get("OneDrive")
            if onedrive_path is not None and onedrive_path in config.basedir:
                raise IllegalModLocation

## Вступительные сообщения
# Это выражение Python указывает, где хранятся вступительные сообщения.
init python:
    # Эта переменная является вступительным сообщением по умолчанию, которое игрок
    # видит во время запуска игры.
    splash_message_default = "Данная игра является неофициальной фанатской работой,\nкоторая никак не связана с Team Salvato."
    # Этот массив хранит разные вступительные сообщения, которые можно использовать для
    # дальнейшего показа игроку во время запуска игры.
    splash_messages = [
        "Пожалуйста, поддержите «Литературный клуб \"Тук-тук!\"».",
        "Моника следит за тем, что вы кодите."
    ]

    ### Нововведение в 3.0.0
    ## Эта функция перекрашивания даёт возможность перекрасить элементы интерфейса DDLC без редактуры
    ## внутриигровых ресурсов.
    ##
    ## Синтаксис использования: recolorize("путь/к/вашему/изображению.формат", "#hexкодцвета1", "#hexкодцвета2", значение контраста)
    ## Пример: recolorize("gui/menu_bg.png", "#bdfdff", "#e6ffff", 1.25)
    def recolorize(path, blackCol="#ffbde1", whiteCol="#ffe6f4", contr=1.29):
        return im.MatrixColor(im.MatrixColor(im.MatrixColor(path, im.matrix.desaturate() * im.matrix.contrast(contr)), im.matrix.colorize("#00f", "#fff")
            * im.matrix.saturation(120)), im.matrix.desaturate() * im.matrix.colorize(blackCol, whiteCol))

    def process_check(stream_list):
        if not renpy.windows:
            for index, process in enumerate(stream_list):
                stream_list[index] = process.replace(".exe", "")
        
        for x in stream_list:
            for y in process_list:
                if re.match(r"^" + x + r"\b", y):
                    return True
        return False

# Это изображение показывает текст вступительного сообщения, когда запускается игра.
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

## Изображения главного меню
# Эти события изображений хранят в себе изображения и координаты расположения логотипа игры,
# а также спрайтов персонажей в главном меню и изображений на экранах главного меню и меню паузы.

# Это изображение показывает логотип DDLC в той точке, на которой он находится в оригинальной игре.
image menu_logo:
    "mod_assets/DDLCModTemplateLogo.png"
    # Composite((512, 512), (0, 0), recolorize("mod_assets/logo_bg.png"), (0, 0), "mod_assets/logo_fg.png")
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

# Это изображение показывает рисунок в горошек на заднем плане экрана главного меню.
image menu_bg:
    topleft
    "gui/menu_bg.png"
    # recolorize("gui/menu_bg.png", "#ffdbf0", "#fff", 1)
    menu_bg_move

# Это изображение показывает рисунок в горошек на заднем плане экрана меню паузы.
image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    # recolorize("gui/menu_bg.png", "#ffdbf0", "#fff", 1)
    menu_bg_loop

# Это изображение показывает белую вспышку в главном меню.
image menu_fade:
    "white"
    menu_fadeout

# Эти изображения показывают соответствующий спрайт персонажа в главном меню на его изначальной позиции и с исходной анимацией.
image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# Эти изображения являют собой то же, что и выше, но они стилизованы под призраков для
# секретного призрачного меню, которое редко появляется в игре.
image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# Это изображение показывает глючный спрайт Сайори в главном меню после прохождения Первого акта.
image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

# Это изображение показывает плашку сбоку на экранах главного меню и меню паузы.
image menu_nav:
    "gui/overlay/main_menu.png"
    #recolorize("gui/overlay/main_menu.png", "#ffbde1")
    menu_nav_move

## Эффекты главного меню
# Эти события трансформаций и изображений хранят эффекты, которые
# проигрываются в главном меню во время запуска игры.

# Это событие изображения показывает эффект взрыва частиц в
# главном меню, когда игра была запущена.
image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

# Эта трансформация управляет затуханием частиц в главном меню.
transform particle_fadeout:
    easeout 1.5 alpha 0

# Эта трансформация двигает рисунок в горошек на заднем плане экрана меню в верхний левый угол.
transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

# Эта трансформация зацикливает эффект движения рисунка в горошек.
transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

# Эта трансформация перемещает логотип меню вниз на его изначальное место в игре.
transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

# Эта трансформация выдвигает плашку главного меню слева.
transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

# Эта трансформация управляет затуханием экрана главного меню. 
transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

# Эта трансформация берёт числительные значения z-оси, x-оси и масштаба, а затем
# перемещает спрайты в главном меню на их изначальное место в игре.
transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

## Заставка Team Salvato
# Это изображение показывает логотип Team Salvato во время запуска игры.
image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

# Это изображение являет собой остатки кода из наработок по DDLC, который показывал вступительное сообщение
# во время запуска игры.
image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

# Это выражение Python, исполняемое во время инициализации, проверяет, имеются ли в папке игры файлы персонажей
# и записывает их в папку «characters» в зависимости от прогресса в игре.
init python:
    if not os.path.exists(user_dir + "/characters"): os.mkdir(user_dir + "/characters")
    restore_all_characters()

## Эти изображения являются фоновыми рисунками, которые показываются в игре во время показа отказа от ответственности.
image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

## Отказ от ответственности при первом запуске
# Этот лейбл вызывает экран отказа от ответственности, который появляется во время запуска игры.
label splashscreen:
    # Это выражение Python делает забор имени пользователя и списка запущенных процессов на компьютере.
    python:
        process_list = []
        currentuser = ""

        if renpy.windows:
            try: process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except subprocess.CalledProcessError:
                try:
                    process_list = subprocess.check_output("powershell (Get-Process).ProcessName", shell=True).lower().replace("\r", "").split("\n") # Для инсайдерских сборок Windows 11

                    for x in enumerate(process_list):
                        process_list[x] += ".exe"
                except subprocess.CalledProcessError: pass            
        else:
            try: process_list = subprocess.check_output("ps -A --format cmd", shell=True).split(b"\n") # Linux
            except subprocess.CalledProcessError: process_list = subprocess.check_output("ps -A -o command", shell=True).split(b"\n") # MacOS

            for x in enumerate(process_list):
                process_list[x] = process_list[x].decode('utf-8').split("/")[-1]
            process_list.pop(0)

        if renpy.windows:
            try: currentuser = os.environ.get("USERNAME") # "%username%" из Винды никуда не денется, так что оставлять перебор разных переменных сред - кринж — прим. пер.
            except: pass
        elif renpy.linux or renpy.macintosh:
            try:
                import pwd
                currentuser = pwd.getpwuid(os.getuid()).pw_gecos.replace(",","") # это нужно для забора "человеческого" имени на Unix-like системах — прим. пер.
            except: pass
        if renpy.windows:
            try: currentuser = os.environ.get("USERNAME") # "%username%" из Винды никуда не денется, так что оставлять перебор разных переменных сред - кринж — прим. пер.
            except: pass
        elif renpy.linux or renpy.macintosh:
            try:
                import pwd
                currentuser = pwd.getpwuid(os.getuid()).pw_gecos.replace(",","") # это нужно для забора "человеческого" имени на Unix-like системах — прим. пер.
            except: pass
        if renpy.windows:
            try: currentuser = os.environ.get("USERNAME") # "%username%" из Винды никуда не денется, так что оставлять перебор разных переменных сред - кринж — прим. пер.
            except: pass
        elif renpy.linux or renpy.macintosh:
            try:
                import pwd
                currentuser = pwd.getpwuid(os.getuid()).pw_gecos.replace(",","") # это нужно для забора "человеческого" имени на Unix-like системах — прим. пер.
            except: pass
        if renpy.windows:
            try: currentuser = os.environ.get("USERNAME") # "%username%" из Винды никуда не денется, так что оставлять перебор разных переменных сред - кринж — прим. пер.
            except: pass
        elif renpy.linux or renpy.macintosh:
            try:
                import pwd
                currentuser = pwd.getpwuid(os.getuid()).pw_gecos.replace(",","") # это нужно для забора "человеческого" имени на Unix-like системах — прим. пер.
            except: pass

    ## Это выражение «если» проверяет, прошли ли мы экран отказа от ответственности,
    ## и равняется ли текущая версия модификации старой, или стоит ли автозагрузка на
    ## финальном стихе в титрах.
    if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
        $ quick_menu = False
        scene black

        menu:
            "Обнаружены файлы сохранений. Хотите ли вы удалить их и начать игру заново?"
            "Да, удалить существующие сохранения.":
                "Файлы сохранений удаляются...{nw}"
                python:
                    delete_all_saves()
                    renpy.loadsave.location.unlink_persistent()
                    renpy.persistent.should_save_persistent = False
                    renpy.utter_restart()
            "Нет, продолжить оттуда, где я остановился.":
                $ restore_relevant_characters()

    # Эти переменная и выражение «если» нужны для программной блокировки,
    # впервые появившейся в версии 2.4.6 этого шаблона. НЕ ИЗМЕНЯЙТЕ ЭТИ СТРОКИ.
    default persistent.lockdown_warning = False

    if not persistent.lockdown_warning:
        if config.developer:
            call lockdown_check
        else:
            $ persistent.lockdown_warning = True

    ## Это устанавливает значение «ложь» у переменной первого запуска, чтобы показать текст отказа от ответственности.
    default persistent.first_run = False

    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0

        ## Вы можете отредактировать это сообщение, но вы ДОЛЖНЫ указать, что ваша модификация
        ## никак не связана с Team Salvato, и что игрок обязан пройти DDLC перед началом игры, а также то, 
        ## что в модификации есть спойлеры, связанные с оригинальной игрой, и где можно достать файлы DDLC.
        "«[config.name]» является фанатской модификацией к игре «Литературный клуб \"Тук-тук!\"», которая никак не связана с Team Salvato."
        "В неё рекомендуется играть только после прохождения оригинальной игры, также в модификации имеются спойлеры, связанные с последней."
        "Для игры в эту модификацию необходимы файлы игры «Литературный клуб \"Тук-тук!\"», скачать их можно на сайте: {a=https://ddlc.moe}https://ddlc.moe{/a} или в Магазине Steam."

        menu:
            "Играя в «[config.name]», вы соглашаетесь с тем, что прошли полностью игру «Литературный клуб \"Тук-тук!\"» и готовы к любым спойлерам."
            "Я согласен.":
                pass

        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0

        ## Это выражение «если» проверяет, запущено ли у нас какое-нибудь распространённое стриминговое/записывающее ПО, 
        ## дабы игра могла автоматически включить Режим летсплейщика и уведомить игрока о том, включены
        ## ли дополнительные настройки.
        if extra_settings:
            if process_check(["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]):
                $ persistent.lets_play = True
                call screen dialog("""Режим летсплейщика был включён автоматически.
Этот режим даёт возможность пропустить контент, который может показаться неприемлемым, или применяет альтернативные сюжетные варианты.

Поведение настройки зависит от мододела, если тот ввёл соответствующие проверки в своём сценарии.

Чтобы выключить Режим летсплейщика, откройте Настройки и снимите флажок с соответствующего пункта.""", 
                    [Hide("dialog"), Return()])
        scene white

    ## Это выражение Python указывает, должен ли показаться экран с ранним убийством Сайори. 
    ## Данная функция была закомментирована из соображений безопасности, но вы можете использовать её,
    ## если возникнет такая необходимость.

    # python:
    #     s_kill_early = None
    #     if persistent.playthrough == 0:
    #         try: open(user_dir + "/characters/sayori.chr", "rb")
    #         except: s_kill_early = True
    #     if not s_kill_early:
    #         if persistent.playthrough <= 2 and persistent.playthrough != 0:
    #             try: open(user_dir + "/characters/monika.chr", "rb")
    #             except: open(user_dir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
    #         if persistent.playthrough <= 1 or persistent.playthrough == 4:
    #             try: open(user_dir + "/characters/natsuki.chr", "rb")
    #             except: open(user_dir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    #             try: open(user_dir + "/characters/yuri.chr", "rb")
    #             except: open(user_dir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
    #         if persistent.playthrough == 4:
    #             try: open(user_dir + "/characters/sayori.chr", "rb")
    #             except: open(user_dir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())


    # Это выражение «если» указывает, какие особые стихи будут показаны игроку во время игры.
    if not persistent.special_poems:
        python hide:
            # Этой переменной присваивается массив нулей для дальнейшего присвоения номеров конкретных стихов.
            persistent.special_poems = [0,0,0]
            
            # Это указывает радиус, из которого надо брать номера стихов.
            a = range(1,12)

            # Этот код исполняется 3 раза (согласно массиву чисел для особых стихов) и
            # вставляет случайное число в массив.
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                # Эта строка удаляет уже вставленное число из радиуса,
                # дабы избежать дублей.
                a.remove(b)

    ## Эта переменная делает так, чтобы путь к рабочей директории имел Unix-like представление,
    ## нежели оное в Windows, ибо Python и Ren'Py предпочитают именно первое.
    $ basedir = user_dir.replace('\\', '/')

    ## Это выражение «если» проверяет, прописан ли у нас лейбл в автозагрузке,
    ## дабы запустить его, а не переходить в главное меню.
    if persistent.autoload:
        jump autoload

    ## Эта переменная запрещает пропуск во время показа вступительной заставки.
    $ config.allow_skipping = False

    ## Это выражение «если» проверяет, находимся ли мы на Втором акте, не видели ли мы призрачное меню
    ## раньше, и является ли случайно выбранное в промежутке 0-63 число нулём.
    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        # Эти переменные подменяют заставку и экран меню под призрачную тематику.
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return

    ## Это выражение «если» проверяет, был ли удалён файл «sayori.chr» после прохождения
    ## экрана отказа от ответственности. Данная функция была закомментирована из соображений
    ## безопасности, но вы можете использовать её, если возникнет такая необходимость.

    # if s_kill_early:
    #     show black
    #     play music "bgm/s_kill_early.ogg"
    #     $ pause(1.0)
    #     show end with dissolve_cg
    #     $ pause(3.0)
    #     scene white
    #     show expression "images/cg/s_kill_early.png":
    #         yalign -0.05
    #         xalign 0.25
    #         dizzy(1.0, 4.0, subpixel=False)
    #     show white as w2:
    #         choice:
    #             ease 0.25 alpha 0.1
    #         choice:
    #             ease 0.25 alpha 0.125
    #         choice:
    #             ease 0.25 alpha 0.15
    #         choice:
    #             ease 0.25 alpha 0.175
    #         choice:
    #             ease 0.25 alpha 0.2
    #         choice:
    #             ease 0.25 alpha 0.225
    #         choice:
    #             ease 0.25 alpha 0.25
    #         choice:
    #             ease 0.25 alpha 0.275
    #         choice:
    #             ease 0.25 alpha 0.3
    #         pass
    #         choice:
    #             pass
    #         choice:
    #             0.25
    #         choice:
    #             0.5
    #         choice:
    #             0.75
    #         repeat
    #     show noise:
    #         alpha 0.1
    #     with Dissolve(1.0)
    #     show expression Text("Теперь все будут счастливы.", style="sayori_text"):
    #         xalign 0.8
    #         yalign 0.5
    #         alpha 0.0
    #         600
    #         linear 60 alpha 0.5
    #     pause
    #     $ renpy.quit()

    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    $ pause(2.5)
    hide intro with Dissolve(0.5, alpha=True)
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    $ pause(1.5)
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ pause(0.5)
    $ config.allow_skipping = True
    return

## Этот лейбл являет собой остатки кода из наработок по DDLC, который скрывает
## логотип Team Salvato и показывает вступительное сообщение.
label warningscreen:
    hide intro
    show warning
    pause 3.0

## Этот лейбл использовался, когда файл «monika.chr» был удалён перед началом игры на Первом акте. 
## Данная функция была закомментирована из соображений безопасности, но вы
## можете использовать её, если возникнет такая необходимость.

# label ch0_kill:
#     $ s_name = "Сайори"
#     show sayori 1b zorder 2 at t11
#     s "..."
#     s "..."
#     s "Ч-что..."
#     s 1g "..."
#     s "Это..."
#     s "Что это?.."
#     s "О нет..."
#     s 1u "Нет..."
#     s "Этого не может быть."
#     s "Такого просто не может быть."
#     s 4w "Что это?"
#     s "Что я такое?"
#     s "Стойте!"
#     s "ПУСТЬ ЭТО ПРЕКРАТИТСЯ!"

#     $ delete_character("sayori")
#     $ delete_character("natsuki")
#     $ delete_character("yuri")
#     $ delete_character("monika")
#     $ renpy.quit()
#     return

# Этот лейбл проверяет, совпадает ли значение анти-чита в загружаемом сохранении с оным в файле постоянных данных.
label after_load:
    $ restore_all_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    ## Это выражение «если» проверяет, находимся ли мы на сценке покончившей с собой Юри во Втором акте,
    ## дабы вернуть нас на сцену в указанное время.
    # if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
    #     if persistent.yuri_kill >= 1380:
    #         $ persistent.yuri_kill = 1440
    #     elif persistent.yuri_kill >= 1180:
    #         $ persistent.yuri_kill = 1380
    #     elif persistent.yuri_kill >= 1120:
    #         $ persistent.yuri_kill = 1180
    #     elif persistent.yuri_kill >= 920:
    #         $ persistent.yuri_kill = 1120
    #     elif persistent.yuri_kill >= 720:
    #         $ persistent.yuri_kill = 920
    #     elif persistent.yuri_kill >= 660:
    #         $ persistent.yuri_kill = 720
    #     elif persistent.yuri_kill >= 460:
    #         $ persistent.yuri_kill = 660
    #     elif persistent.yuri_kill >= 260:
    #         $ persistent.yuri_kill = 460
    #     elif persistent.yuri_kill >= 200:
    #         $ persistent.yuri_kill = 260
    #     else:
    #         $ persistent.yuri_kill = 200
    #     jump expression persistent.autoload

    ## Используйте «elif» вместо «if», если вы раскомментировали код выше.
    ## Это выражение проверяет, равняется ли число анти-чита оному в файле
    ## постоянных данных, в противном случае возникнет ошибка.
    if anticheat != persistent.anticheat:
        stop music
        scene black
        "Сохранение не может быть загружено."
        "Кого ты пытаешься обмануть?"
        $ m_name = "Моника"
        show monika 1 at t11
        if persistent.playername == "":
            m "Ты такой смешной."
        else:
            m "Ты такой смешной, [persistent.playername]."
        $ renpy.utter_restart()
    else:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Подсказка: используйте кнопку «Пропуск» для\nбыстрой прокрутки уже прочитанного текста.", ok_action=Return())
    return

# Этот лейбл загружает лейбл, сохранённый в переменной автозагрузки.
label autoload:
    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    # if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
    #     $ persistent.yuri_kill += 200

    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

## Этот лейбл используется при запуске игры, дабы вернуть нас прямо на сценку
## покончившей с собой Юри из главного меню.
# label autoload_yurikill:
#     if persistent.yuri_kill >= 1380:
#         $ persistent.yuri_kill = 1440
#     elif persistent.yuri_kill >= 1180:
#         $ persistent.yuri_kill = 1380
#     elif persistent.yuri_kill >= 1120:
#         $ persistent.yuri_kill = 1180
#     elif persistent.yuri_kill >= 920:
#         $ persistent.yuri_kill = 1120
#     elif persistent.yuri_kill >= 720:
#         $ persistent.yuri_kill = 920
#     elif persistent.yuri_kill >= 660:
#         $ persistent.yuri_kill = 720
#     elif persistent.yuri_kill >= 460:
#         $ persistent.yuri_kill = 660
#     elif persistent.yuri_kill >= 260:
#         $ persistent.yuri_kill = 460
#     elif persistent.yuri_kill >= 200:
#         $ persistent.yuri_kill = 260
#     else:
#         $ persistent.yuri_kill = 200
#     jump expression persistent.autoload

## Этот лейбл устанавливает главную тему DDLC в качестве музыки в главном меню
## перед запуском самого меню.
label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

# Этот лейбл являет собой остатки кода из наработок по DDLC, который завершает работу
# игры, но перед этим на мгновение показывает лицо призрачной Моники вблизи.
label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return
