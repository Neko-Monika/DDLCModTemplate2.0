## screens.rpy

# В этом файле определяются все экраны и стили для DDLC.

## Инициализация
################################################################################

init offset = -1

# Включает возможность добавления в игру таких дополнительных настроек, как режим без цензуры.
default extra_settings = True

## Цветовые схемы
################################################################################

# Эта переменная управляет цветом обводки такого внутриигрового текста, как
# простой текст, диалог, навигация, метки и прочее.
define -2 text_outline_color = "#b59"

## Стили
################################################################################

style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style default_monika is normal:
    slow_cps 30

style edited is default:
    font "gui/font/PTM55F.ttf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

style poemgame_text:
    yalign 0.5
    font "gui/font/comic.ttf"
    size 26
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size


#style bar:
#    ysize gui.bar_size
#    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True

style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

#style vscrollbar:
#    xsize gui.scrollbar_size
#    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
    # background Frame(recolorize("gui/frame.png"), gui.frame_borders, tile=gui.frame_tile)

################################################################################
## Внутриигровые экраны
################################################################################


## Экран разговора #############################################################
##
## Экран разговора используется для показа диалога игроку. Он использует два
## параметра — who и what — что, соответственно, имя говорящего персонажа и
## показываемый текст. (Параметр who может быть None, если имя не задано.)
##
## Этот экран должен создать текст с id "what", чтобы Ren'Py могла показать
## текст. Здесь также можно создать наложения с id "who" и id "window", чтобы
## применить к ним настройки стиля.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

    ## Если есть боковое изображение ("голова"), показывает её поверх текста.
    ## По стандарту не показывается на варианте для мобильных устройств — мало
    ## места.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Transform("gui/textbox.png", xalign=0.5, yalign=1.0)

style window_monika is window:
    background Transform("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, text_outline_color, 0, 0), (1, text_outline_color, 1, 1)]
    #outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]

style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat

## Экран ввода #################################################################
##
## Этот экран используется, чтобы показывать renpy.input. Это параметр запроса,
## используемый для того, чтобы дать игроку ввести в него текст.
##
## Этот экран должен создать наложение ввода с id "input", чтобы принять
## различные вводимые параметры.
##
## http://www.renpy.org/doc/html/screen_special.html#input

image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xpos gui.text_xpos
            xanchor 0.5
            ypos gui.text_ypos

            text prompt style "input_prompt"
            input id "input"


style input_prompt is default

style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.5
    text_align 0.5


## Экран выбора ################################################################
##
## Этот экран используется, чтобы показывать внутриигровые выборы,
## представленные оператором menu. Один параметр, вложения, список объектов,
## каждый с заголовком и полями действия.
##
## Нововведение в 3.0.0
## Теперь вы можете передавать аргументы через варианты меню, чтобы 
## раскрасить их как душе угодно. Допишите (kwargs=[hex-код или название стиля])
## в вариант выбора, и вы получите разные кнопки! 
##
## Примеры: "Вариант 1 (kwargs=#00fbff)" | "Вариант 2 (kwargs=#00fbff, #6cffff)"
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:

        for i in items:
            
            if "kwargs=" in i.caption:

                $ kwarg = i.caption.split("(kwargs=")[-1].replace(")", "")
                $ caption = i.caption.replace(" (kwargs=" + kwarg + ")", "")

                if "#" in kwarg:
                    
                    $ kwarg = kwarg.replace(", ", ",").split(",")
                    
                    if len(kwarg) == 1:
                        $ kwarg.append('#ffe6f4')
                    
                    $ arg1 = kwarg[0]
                    $ arg2 = kwarg[-1]
                    
                    textbutton caption:
                        idle_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_idle_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, arg2)), gui.choice_button_borders)
                        hover_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_hover_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, "#fff")), gui.choice_button_borders)
                        action i.action

                else:

                    textbutton caption:
                        style kwarg
                        action i.action

            else:

                textbutton i.caption action i.action


## Когда этот параметр True, заголовки меню будут проговариваться рассказчиком.
## Когда False, заголовки меню будут показаны как пустые кнопки.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    idle_background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []


init python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)


## Экран быстрого меню #########################################################
##
## Быстрое меню показывается внутри игры, чтобы обеспечить лёгкий доступ к
## внеигровым меню.

screen quick_menu():

    # Гарантирует, что оно появляется поверх других экранов.
    zorder 100

    if quick_menu:

        # Добавляет внутриигровое быстрое меню.
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995

            #textbutton _("Назад") action Rollback()
            textbutton _("История") action ShowMenu('history')
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Сохранить") action ShowMenu('save')
            textbutton _("Загрузить") action ShowMenu('load')
            #textbutton _("Б.Сохр.") action QuickSave()
            #textbutton _("Б.Загр.") action QuickLoad()
            textbutton _("Настройки") action ShowMenu('preferences')


## Данный код гарантирует, что экран быстрого меню будет показан в игре в любое
## время, если только игрок не скроет интерфейс.
#init python:
#    config.overlay_screens.append("quick_menu")

default quick_menu = True

#style quick_button is default
#style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []


################################################################################
# Экраны Главного и Игрового меню
################################################################################

## Экран навигации #############################################################
##
## Этот экран включает в себя главное и игровое меню, и обеспечивает навигацию к
## другим меню и к началу игры.

init python:
    def FinishEnterName():
        if not player: return
        persistent.playername = player
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        # На мобильных устройствах кнопка "Помощь" с действием по умолчанию бесполезна, а позиция навигации строго зависит от его наполнения - прим. пер.
        if renpy.variant("pc"):
            yalign 0.8
        else:
            yalign 0.6

        spacing gui.navigation_spacing

        if not persistent.autoload or not main_menu:

            if main_menu:

                if persistent.playthrough == 1:
                    textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Введите своё имя", ok_action=Function(FinishEnterName)))
                else:
                    textbutton _("Новая игра") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Введите своё имя", ok_action=Function(FinishEnterName)))

            else:

                textbutton _("История") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

                textbutton _("Сохранить") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

            textbutton _("Загрузить") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

            textbutton _("Галерея") action [ShowMenu("gallery"), SensitiveIf(renpy.get_screen("gallery") == None)]

            textbutton _("Достижения") action [ShowMenu("achievements"), SensitiveIf(renpy.get_screen("achievements") == None)]

            if _in_replay:

                textbutton _("Завершить повтор") action EndReplay(confirm=True)

            elif not main_menu:
                if persistent.playthrough != 3:
                    textbutton _("Главное меню") action MainMenu()
                else:
                    textbutton _("Главное меню") action NullAction()

            textbutton _("Настройки") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]

            #textbutton _("Об игре") action ShowMenu("about")

            if renpy.variant("pc"):

                ## Помощь не необходима и не относится к мобильным устройствам.
                textbutton _("Помощь") action [Help("README.html"), Show(screen="dialog", message="Файл справки открыт в браузере.", ok_action=Hide("dialog"))]

                ## Кнопка выхода блокирована в iOS и не нужна на Android. (Очень даже нужна, иначе девайс будет жрать батарею как не в себя - прим. пер.)
            textbutton _("Выход") action Quit(confirm=not main_menu)
        else:
            timer 1.75 action Start("autoload_yurikill")


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/Rotonda.ttf"
    color "#fff"
    outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
    #outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]


## Экран главного меню #########################################################
##
## Используется, чтобы показать главное меню после запуска игры.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # Этот тег гарантирует, что любой другой экран с тем же тегом будет
    # заменять этот.
    tag menu

    style_prefix "main_menu"

    if persistent.ghost_menu:
        add "white"
        add "menu_art_y_ghost"
        add "menu_art_n_ghost"
    else:
        add "menu_bg"
        add "menu_art_y"
        add "menu_art_n"
        frame

        # Оператор use включает отображение другого экрана в данном. Актуальное
        # содержание главного меню находится на экране навигации.
        use navigation

    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        add "menu_logo"
    if persistent.ghost_menu:
        add "menu_art_s_ghost"
        add "menu_art_m_ghost"
    else:
        if persistent.playthrough in [1, 2]:
            add "menu_art_s_glitch"
        else:
            add "menu_art_s"
        add "menu_particles"
        if persistent.playthrough != 4:
            add "menu_art_m"
        add "menu_fade"

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size


## Экран игрового меню #########################################################
##
## Всё это показывает основную, обобщённую структуру экрана игрового меню. Он
## вызывается с экраном заголовка и показывает фон, заголовок и навигацию.
##
## Параметр scroll может быть либо None, либо "viewport" или "vpgrid", если этот
## экран предназначается для использования с более чем одним дочерним экраном,
## включённым в него.

screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

screen game_menu(title, scroll=None):

    # Добавляет фон.
    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        hbox:

            # Резервирует пространство для навигации.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        yinitial 1.0

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show" action Show("game_menu_m")

    textbutton _("Назад"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"
    # background recolorize("gui/overlay/game_menu.png")

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font "gui/font/Rotonda.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, text_outline_color, 0, 0), (3, text_outline_color, 2, 2)]
    #outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## Экран Об игре ###############################################################
##
## Этот экран показывает авторскую информацию об игре и Ren'Py.
##
## В этом экране нет ничего особенного, и он служит только примером того, каким
## можно сделать свой экран.

screen about():

    tag menu

    # Этот оператор включает игровое меню внутрь этого экрана. Дочерний vbox
    # включён в порт просмотра внутри экрана игрового меню.
    use game_menu(_("Об игре"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Версия [config.version!t]\n")

            # gui.about обычно установлено в options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Сделано на {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## Это переопределяется в options.rpy для добавления текста в экран «Об игре».
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Сохранить"))


screen load():

    tag menu

    use file_slots(_("Загрузить"))

init python:
    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 1 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            return Show(screen="dialog", message="Ошибка чтения: \"characters/sayori.chr\"\n\nФайл отсутствует или повреждён.",
                ok_action=Show(screen="dialog", message="Файл сохранения повреждён. Начинается новая игра.", ok_action=Function(renpy.full_restart, label="start")))
        elif persistent.playthrough == 3 and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="Больше нет смысла сохраняться.\nНе волнуйся, я никуда не уйду.", ok_action=Hide("dialog"))
        else:
            return FileAction(name)


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern="Страница {}") # FilePageNameInputValue(pattern="Страница {}", auto="Автосохранения", quick="Быстрые сохранения")

    use game_menu(title):

        fixed:

            ## Это гарантирует, что ввод будет принимать события выбора
            ## перед остальными кнопками.
            order_reverse True

            ## Номер страницы, который может быть изменён посредством клика на
            ## кнопку.

            button:
                style "page_label"

                #key_events True
                xalign 0.5
                #action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Таблица слотов.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileActionMod(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%d %b %Y в %H:%M"), empty=_("пустой слот")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Кнопки для доступа к другим страницам.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                #textbutton _("<") action FilePagePrevious(max=9, wrap=True)

                #textbutton _("{#auto_page}А") action FilePage("auto")

                #textbutton _("{#quick_page}Б") action FilePage("quick")

                # range(1, 10) задаёт диапазон значений от 1 до 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                #textbutton _(">") action FilePageNext(max=9, wrap=True)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

style slot_button:
    properties gui.button_properties("slot_button")
    idle_background Frame("gui/button/slot_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/slot_hover_background.png", gui.choice_button_borders)

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []


## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    python:
        cols = 4 if not renpy.mobile else 2

    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:
            if extra_settings:
                xoffset 35
            else:
                xoffset 50

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Режим экрана")
                        textbutton _("Оконный") action Preference("display", "window")
                        textbutton _("Полноэкранный") action Preference("display", "fullscreen")
                if config.developer:
                    vbox:
                        style_prefix "radio"
                        label _("Сторона отката")
                        textbutton _("Отключено") action Preference("rollback side", "disable")
                        textbutton _("Левая") action Preference("rollback side", "left")
                        textbutton _("Правая") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Пропускать")
                    textbutton _("Непрочитанное") action Preference("skip", "toggle")
                    textbutton _("После выборов") action Preference("after choices", "toggle")
                    #textbutton _("Переходы") action InvertSelected(Preference("transitions", "toggle"))

                if extra_settings:
                    vbox:
                        style_prefix "check"
                        label _("Доп. настройки")
                        textbutton _("Режим «Без цензуры»") action If(persistent.uncensored_mode, 
                            ToggleField(persistent, "uncensored_mode"), 
                            Show("confirm", message="""Вы уверены, что хотите включить Режим «Без цензуры»?
Это приведёт к показу контента, который предназначен только для взрослых, или контента, который может быть чувствительным для некоторых групп людей.

Поведение настройки зависит от мододела, если тот ввёл соответствующие проверки в своём сценарии.""", 
                                yes_action=[Hide("confirm"), ToggleField(persistent, "uncensored_mode")],
                                no_action=Hide("confirm")
                            ))
                        textbutton _("Режим летсплейщика") action If(persistent.lets_play, 
                            ToggleField(persistent, "lets_play"),
                            [ToggleField(persistent, "lets_play"), Show("dialog", 
                                message="""Вы включили Режим летсплейщика.
Этот режим даёт возможность пропустить контент, который может показаться неприемлемым, или применяет альтернативные сюжетные варианты.

Поведение настройки зависит от мододела, если тот ввёл соответствующие проверки в своём сценарии.""",
                                ok_action=Hide("dialog")
                            )])


                ## Дополнительные vbox'ы типа "radio_pref" или "check_pref"
                ## могут быть добавлены сюда для добавления новых настроек.

            null height (4 * gui.pref_spacing)

            hbox:
                if extra_settings:
                    xoffset 15
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Скорость вывода текста")

                    #bar value Preference("text speed")
                    bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

                    label _("Задержка при авточтении")

                    bar value Preference("auto-forward time")

                vbox:
                    if extra_settings:
                        xoffset 15

                    if config.has_music:
                        label _("Громкость музыки")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Громкость звуков")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Проверка") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Громкость голоса")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Проверка") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Отключить звук"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            if config.developer:
                hbox:
                    vbox:
                        textbutton _("Экспорт иконки модификации в ICO"):
                            action Function(saveIco, "mod_assets/DDLCModTemplateLogo.png")
                            style "navigation_button"

    text "вер. [config.version]":
                xalign 1.0 yalign 1.0
                xoffset -10 yoffset -10
                style "main_menu_version"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font "gui/font/Rotonda.ttf"
    size 24
    color "#fff"
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/comic.ttf"
    outlines []

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/comic.ttf"
    outlines []

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## Экран истории ###############################################################
##
## Этот экран показывает игроку историю диалогов. Хотя в этом экране нет ничего
## особенного, он имеет доступ к истории диалогов, хранимом в _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    tag menu
    predict False

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport")):
        style_prefix "history"
        for h in _history_list:
            window:
                has fixed:
                    yfit True
                if h.who:
                    label h.who:
                        style "history_name"
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                $ what = filter_text_tags(h.what, allow=set([]))
                text what:
                    substitute False
        if not _history_list:
            label _("История диалогов пуста.")

python early:
    import renpy.text.textsupport as textsupport
    from renpy.text.textsupport import TAG, PARAGRAPH
    def filter_text_tags(s, allow=None, deny=None):
        if (allow is None and deny is None) or (allow is not None and deny is not None):
            raise Exception("Функции filter_text_tags должен быть передан только один из ключевых аргументов allow или deny.")
        tokens = textsupport.tokenize(unicode(s))
        rv = [ ]
        for tokentype, text in tokens:
            if tokentype == PARAGRAPH:
                rv.append("\n")
            elif tokentype == TAG:
                kind = text.partition("=")[0]
                if kind and (kind[0] == "/"):
                    kind = kind[1:]
                if allow is not None:
                    if kind in allow:
                        rv.append("{" + text + "}")
                else:
                    if kind not in deny:
                        rv.append("{" + text + "}")
            else:
                rv.append(text)
        return "".join(rv)

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Экран помощи ################################################################
##
## Экран, дающий информацию о клавишах управления. Он использует другие экраны
## (keyboard_help, mouse_help, и gamepad_help), чтобы показывать актуальную
## помощь.

#screen help():
#
#    tag menu
#
#    default device = "keyboard"
#
#    use game_menu(_("Помощь"), scroll="viewport"):
#
#        style_prefix "help"
#
#        vbox:
#            spacing 15
#
#            hbox:
#
#                textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
#                textbutton _("Мышь") action SetScreenVariable("device", "mouse")
#
#                if GamepadExists():
#                    textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")
#
#            use expression device + "_help"
#
#
#
#screen keyboard_help():
#
#    hbox:
#        label _("Enter")
#        text _("Прохождение диалогов и активация интерфейса.")
#
#    hbox:
#        label _("Пробел")
#        text _("Прохождение диалогов без возможности делать выбор.")
#
#    hbox:
#        label _("Стрелки")
#        text _("Навигация по интерфейсу.")
#
#    hbox:
#        label _("Esc")
#        text _("Вход в игровое меню.")
#
#    hbox:
#        label _("Ctrl")
#        text _("Пропускает диалоги, пока зажат.")
#
#    hbox:
#        label _("Tab")
#        text _("Включает режим пропуска.")
#
#    hbox:
#        label _("Page Up")
#        text _("Откат назад по сюжету игры.")
#
#    hbox:
#        label _("Page Down")
#        text _("Откатывает предыдущее действие вперёд.")
#
#    hbox:
#        label _("H")
#        text _("Скрывает интерфейс пользователя.")
#
#    hbox:
#        label _("S")
#        text _("Делает снимок экрана.")
#
#    hbox:
#        label _("V")
#        text _("Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}.")
#
#
#screen mouse_help():
#
#    hbox:
#        label _("Левая кнопка")
#        text _("Прохождение диалогов и активация интерфейса.")
#
#    hbox:
#        label _("Средняя кнопка")
#        text _("Скрывает интерфейс пользователя.")
#
#    hbox:
#        label _("Правая кнопка")
#        text _("Вход в игровое меню.")
#
#    hbox:
#        label _("Колёсико вверх\nКлик на сторону отката")
#        text _("Откат назад по сюжету игры.")
#
#    hbox:
#        label _("Колёсико вниз")
#        text _("Откатывает предыдущее действие вперёд.")
#
#
#screen gamepad_help():
#
#    hbox:
#        label _("Правый триггер\nA/Нижняя кнопка")
#        text _("Прохождение диалогов и активация интерфейса.")
#
#    hbox:
#        label ("Левый триггер\nЛевый бампер")
#        text _("Откат назад по сюжету игры.")
#
#    hbox:
#        label _("Правый бампер")
#        text _("Откатывает предыдущее действие вперёд.")
#
#    hbox:
#        label _("Крестовина, Стики")
#        text _("Навигация по интерфейсу.")
#
#    hbox:
#        label _("Старт, Гид")
#        text _("Вход в игровое меню.")
#
#    hbox:
#        label _("Y/Верхняя кнопка")
#        text _("Скрывает интерфейс пользователя.")
#
#    textbutton _("Калибровка") action GamepadCalibrate()
#
#
#style help_button is gui_button
#style help_button_text is gui_button_text
#style help_label is gui_label
#style help_label_text is gui_label_text
#style help_text is gui_text
#
#style help_button:
#    properties gui.button_properties("help_button")
#    xmargin 8
#
#style help_button_text:
#    properties gui.button_text_properties("help_button")
#
#style help_label:
#    xsize 250
#    right_padding 20
#
#style help_label_text:
#    size gui.text_size
#    xalign 1.0
#    text_align 1.0



################################################################################
## Дополнительные экраны
################################################################################


## Экран подтверждения #########################################################
##
## Экран подтверждения вызывается, когда Ren'Py хочет задать игроку вопрос,
## подразумевающий ответы «Да» и «Нет».
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen name_input(message, ok_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            input default "" value VariableInputValue("player") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

            #hbox:
            #    xalign 0.5
            #    style_prefix "radio_pref"
            #    textbutton "Мужчина" action NullAction()
            #    textbutton "Женщина" action NullAction()
            hbox:
                xalign 0.5
                spacing 100

                textbutton _("ОК") action ok_action

screen dialog(message, ok_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("ОК") action ok_action

image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

screen confirm(message, yes_action, no_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            if in_sayori_kill and message == layout.QUIT:
                add "confirm_glitch" xalign 0.5

            else:
                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Да") action yes_action
                textbutton _("Нет") action no_action

    ## Правая кнопка мыши и Esc выбирают «Нет».
    #key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame("gui/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    # background Frame(recolorize("gui/frame.png"), gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")


## Экран индикатора пропуска ###################################################
##
## Экран индикатора пропуска появляется для того, чтобы показать, что идёт
## пропуск.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen fake_skip_indicator():
    use skip_indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Пропуск")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Эта трансформация используется, чтобы стрелки мигали одна за другой.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Нам надо использовать шрифт, имеющий в себе символ U+25B8 (стрелку выше).
    font "DejaVuSans.ttf"


## Экран уведомлений ###########################################################
##
## Экран уведомлений используется, чтобы показать игроку оповещение. (Например,
## когда игра автосохранилась или был сделан скриншот)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size

## Экран NVL ###################################################################
##
## Этот экран используется в диалогах и меню режима NVL.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Показывает диалог или в vpgrid, или в vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Показывает меню, если есть. Меню может показываться некорректно, если
        ## config.narrator_menu установлено на True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

## Экран Синего экрана смерти ############################################################
## Авторское право 2019-2022 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.
## Вы можете использовать этот файл или функцию только в модификациях для DDLC;
## использование в патчерах DDLC, неофициальных фиксах и т.д. запрещено.
##
## Этот экран используется для мимикрии СЭС/паники ядра на компьютере игроков на всех
## возможных платформах (на мобильных устройствах будет использоваться экран паники ОС Linux).
##
## Синтаксис:
## bsodCode - Код ошибки, который вы хотите показать игроку. Если не дано, будет 
##                подставлено «DDLC_ESCAPE_PLAN_FAILED».
## bsodFile (только Windows 7 и Linux) - Мимикрия имени файла, из-за которого 
##               возникла проблема. Если не дано, будет подставлено «libGLESv2.dll».
## rsod (только Windows 11) - Меняет Синий ЭС Windows 11 на Красный.
##
## Примеры:
## show screen bsod("DOKI_DOKI", "renpy32.dll", False) 
## show screen bsod("EILEEN_EXCEPTION_NOT_HANDLED", rsod=True) 

init python:
    import subprocess, platform

    cursor = 0

    def fakePercent(st, at, winver):

        if int(0 + (st * 5)) < 100:
            percent = int(0 + (st * 5))
        else:
            percent = 100

        if winver == 8:
            d = Text("автоматически выполнена перезагрузка. (выполнено: " + str(percent) + "%)\n", style="bsod_win8_text", size=26)
        else:
            d = Text(str(percent) + "% завершено", style="bsod_win10_text", line_leading=25)

        if percent < 100:
            return d, renpy.random.randint(1, 3)
        else:
            return d, None

    def constantCursor(st, at):
        global cursor
        if cursor == 0:
            cursor = 1
            return Text("  _", style="bsod_linux_text"), 0.5
        else:
            cursor = 0
            return Text("   ", style="bsod_linux_text"), 0.5


    if renpy.windows:
        try: osVer = tuple(map(int, subprocess.check_output("powershell (Get-WmiObject -class Win32_OperatingSystem).Version", shell=True).split("."))) # Vista+
        except: osVer = tuple(map(int, platform.version().split("."))) or (5, 1, 2600) # XP возвращает JIC (хотя кто пользуется XP в наши дни?)

screen bsod(bsodCode="DDLC_ESCAPE_PLAN_FAILED", bsodFile="libGLESv2.dll", rsod=False):

    layer "master"

    if renpy.windows:

        if osVer < (6, 2, 9200): # Windows 7
            
            add Solid("#000082")

            vbox:

                style_prefix "bsod_win7"

                text "Вследствие возникшей проблемы система Windows принудительно завершила работу для предотвращения урона компьютеру."
                text "Проблема была вызвана следующим файлом: " + bsodFile.upper()
                text bsodCode.upper()
                text "Если вы впервые видите этот Синий экран останова, перезагрузите компьютер. Если этот экран появился снова, следуйте нижеприведённым шагам:"
                text "Убедитесь, что новое оборудование или ПО установлено корректно. Если оборудование/ПО было установлено впервые, попросите у производителя оборудования/ПО обновления Windows, которые могут вам понадобиться."
                text "Если проблема не была устранена, отключите или удалите любое только что установленное оборудование или ПО. Отключите такие параметры памяти BIOS, как кэширование и теневое копирование. Если для удаления/отключения компонентов вам необходимо воспользоваться Безопасным режимом, перезагрузите компьютер, нажмите F8 для входа в Дополнительные параметры загрузки, а затем выберите Безопасный режим."
                text "Техническая информация:"
                text "*** STOP: 0x00000051 (OXFD69420, 0x00000005, OXFBF92317" + ", 0x00000000)\n"
                text "*** " + bsodFile.upper() + "  -  Address FBF92317 base at FBF102721, Datestamp 3d6dd67c"

        elif osVer < (10, 0, 10240): # Windows 8/8.1
            
            add Solid("#1273aa")

            style_prefix "bsod_win8"

            vbox:

                xalign 0.5
                yalign 0.4

                text ":(" style "bsod_win8_sad_text"
                text "На вашем ПК возникла проблема, и его необходимо перезагрузить."
                text "Мы лишь собираем некоторые сведения об ошибке, а затем будет"
                add DynamicDisplayable(fakePercent, 8)
                text "При желании вы можете найти в Интернете информацию по этому коду ошибки: " + bsodCode.upper() style "bsod_win8_sub_text"

        else: # Windows 10 (up to 21H1)/Windows 11/Windows 11 RSOD
            
            if osVer < (10, 0, 22000):
            
                add Solid("#0078d7")

            else:

                if not rsod:

                    add Solid("#000000")
                    python:
                        blackCol = "#0078d7"

                else:

                    add Solid("#d40e0eff")
                    python:
                        blackCol = "#f00"

            style_prefix "bsod_win10"

            vbox:

                xalign 0.3
                yalign 0.3

                text ":(" style "bsod_win10_sad_text"

                if osVer < (10, 0, 22000):

                    text "На вашем ПК возникла проблема, и его необходимо перезагрузить."
                    text "Мы лишь собираем некоторые сведения об ошибке, а затем будет"
                    text "автоматически выполнена перезагрузка."

                else:

                    text "На вашем устройстве возникла проблема, и его необходимо перезагрузить."
                    text "Мы лишь собираем некоторые сведения об ошибке, а затем будет"
                    text "автоматически выполнена перезагрузка."

                add DynamicDisplayable(fakePercent, 10)

                hbox:

                    if osVer < (10, 0, 22000):

                        vbox:
                            text "" line_leading -3
                            add im.MatrixColor("mod_assets/frame.png", im.matrix.colorize("#0078d7", "#fff"), ) at bsod_qrcode(100)
                        vbox:
                            xpos 0.03
                            spacing 4
                            text "Дополнительные сведения об этой проблеме и возможных способах её решения см. на странице https://www.windows.com/stopcode" style "bsod_win10_info_text" line_leading 25
                            text "При обращении в службу поддержки предоставьте следующие данные:" style "bsod_win10_sub_text" line_leading 25
                            text "Код остановки: " + bsodCode.upper() style "bsod_win10_sub_text"

                    else:

                        vbox:
                            text "" line_leading -3
                            add im.MatrixColor("mod_assets/frame.png", im.matrix.colorize(blackCol, "#fff"), ) at bsod_qrcode(150)
                        vbox:
                            xpos 0.03
                            spacing 4
                            text "Дополнительные сведения об этой проблеме и возможных способах её решения см. на странице" style "bsod_win10_info_text" line_leading 25
                            text "https://www.windows.com/stopcode\n" style "bsod_win10_info_text"
                            text "При обращении в службу поддержки предоставьте следующие данные:" style "bsod_win10_sub_text"
                            text "Код остановки: " + bsodCode.upper() style "bsod_win10_sub_text"
        
    elif renpy.macintosh:

        add Solid("#222")

        add im.MatrixColor("mod_assets/DDLCModTemplateLogo.png", im.matrix.desaturate() * im.matrix.brightness(-0.36)) at bsod_qrcode(440) xalign 0.5 yalign 0.54
        vbox:

            style_prefix "bsod_mac"
            xalign 0.53
            yalign 0.51

            text "Вам необходимо перезагрузить компьютер. Удерживайте\n"
            text "кнопку Питания, пока он не выключится, затем нажмите эту же\n"
            text "кнопку снова." line_spacing 25
            text "Redémarrez l'ordinateur. Enfoncez le bouton de démarrage\n"
            text "jusqu'à l'extinction, puis appuyez dessus une nouvelle fois." line_spacing 25
            text "Debe reiniciar el o rdenador. Mantenga pulsado el botón de\n"
            text "arranque hasta que se apague y luego vuelva a pulsarlo." line_spacing 25
            text "Sie müssen den Computer neu starten. Halten Sie den\n"
            text "Ein-/Ausschalter gedrückt bis das Gerät ausgeschaltet ist\n"
            text "und drücken Sie ihn dann erneut." line_spacing 25
            text "{font=gui/font/SourceHanSansLite.ttf}コンピュータの再起動が必要です。電源が切れるまでパワーボタンを{/font}"
            text "{font=gui/font/SourceHanSansLite.ttf}押し続けてから、もう一度パワーボタンを押します。{/font}"
            # text "Devi riavviare il computer. Tieni premuto il pulsante di\n"
            # text "accensione finché non si spegne, quindi premi di nuovo il\n"
            # text "pulsante di accensione."

    else:

        add Solid("#000")

        vbox:
            style_prefix "bsod_linux"

            text "metaverse-pci.c:v[config.version] 9/22/2017 Metaverse Enterprise Solutions\n"
            text "  https://www.metaverse-enterprise.com/network/metaverse-pci.html"
            text "hda0: METAVERSE ENTERPRISE VIRTUAL HARDDISK, ATA DISK drive"
            text "ide0 at 0x1f0 - 0x1f7, 0x3f6 on irq 14"
            text "hdc: METAVERSE ENTERPRISE VIRTUAL CD-ROM, ATAPI CD/DVD-ROM drive"
            text "ide1 at 0x444 - 0x910, 0x211 on irq 15"
            text "fd0: METAVERSE ENTERPRISE VIRTUAL FLOPPY, ATA FLOPPY drive"
            text "ide2 at 0x7363-0x6e6565, 0x4569 on irq 16"
            text "ACPI: PCI Interrupt Link [[LNKC] ebabked at IRQ 10"
            text "ACPI: PCI Interrupt 0000:00:03:.0[[A] -> Link [[LNKC] -> GSI 10 (level, low) -> IRQ 10"
            text "eno1: Metaverse Enterprise LIB-0922 found at 0xc453, IRQ 10, 09:10:21:86:75:30"
            text "hda: max request size: 512KiB"
            text "hda: 2147483648 sectors (1 TB) w/256KiB Cache, CHS=178/255/63, (U)DMA"
            text "hda: hda1"
            text "hdc: ATAPI 4x CD-ROM drive, 512kB Cache, (U)DMA"
            text "Uniform CD-ROM driver Revision: 3.20"
            text "Готово."
            text "Запуск: DDLC.so"
            text "Готово."
            text "DDLC.so: глобальная переменная natsukiTime не объявлена."
            text "DDLC.so: глобальная переменная sayoriTime не объявлена."
            text "DDLC.so: глобальная переменная yuriTime не объявлена."
            text "DDLC.so: глобальная переменная monikaTime не объявлена."
            text "DDLC.so: УСПЕШНО."
            text "Запуск: DDLC.so -> linux-4.12.14"
            text "/init: /init: 151: " + bsodCode.upper() + ": 0xforce=panic"
            text "Паника ядра - невозможность синхронизации: Попытка убить инициализацию!"
            add DynamicDisplayable(constantCursor)

    add Solid("#000000") at bsod_transition

style bsod_win7_text is gui_text
style bsod_win7_text:
    font "C:/Windows/Fonts/lucon.ttf"
    antialias False
    size 13
    line_leading 15
    line_spacing -14
    xsize 1279
    outlines []

style bsod_win8_text is gui_text
style bsod_win8_text:
    font "C:/Windows/Fonts/segoeuil.ttf"
    size 25
    line_spacing 5
    xsize 600
    outlines []

style bsod_win8_sad_text is gui_text
style bsod_win8_sad_text is bsod_win8_text:
    size 128
    xpos -8

style bsod_win8_sub_text is gui_text
style bsod_win8_sub_text is bsod_win8_text:
    size 11

style bsod_win10_text is bsod_win8_text
style bsod_win10_text:
    font "C:/Windows/Fonts/segoeuil.ttf"
    size 24
    line_leading 3
    line_spacing 0
    xsize 800
    outlines []

style bsod_win10_info_text is bsod_win10_text
style bsod_win10_info_text:
    size 16

style bsod_win10_sad_text is bsod_win10_text
style bsod_win10_sad_text:
    size 136
    xpos -8

style bsod_win10_sub_text is bsod_win10_text
style bsod_win10_sub_text:
    size 11

style bsod_mac_text is gui_text
style bsod_mac_text:
    font gui.default_font
    size 28
    outlines []
    line_spacing -30

style bsod_linux_text is gui_text
style bsod_linux_text:
    font "gui/font/consola.ttf"
    size 15
    outlines []
    line_leading 5
            
transform bsod_transition:
    "black"
    0.1
    yoffset 250
    0.1
    yoffset 500
    0.1
    yoffset 750

transform bsod_qrcode(x):
    size(x,x)

## Это контролирует максимальное число строк NVL, способных показываться за раз.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
