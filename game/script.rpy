## script.rpy

# Этот файл является основным скриптом, который Ren'Py 
# исполняет, чтобы начать историю вашей модификации!

label start:

    # Эта переменная настраивает число анти-чита для игры после прохождения Первого акта.
    # Настоятельно рекомендуется оставить её как есть и использовать в своём скрипте следующее:
    # $ persistent.anticheat = renpy.random.randint(X, Y) 
    # X - минимальное число | Y - максимальное число
    $ anticheat = persistent.anticheat

    # Эта переменная устанавливает номер главы как 0 для использования в модификации.
    $ chapter = 0

    # Эта переменная указывает, может ли игрок пропускать паузы в игре.
    $ _dismiss_pause = config.developer

    ## Имена персонажей
    # Эти переменные настраивают имена персонажей в игре.
    # Чтобы добавить персонажа, используйте нижеприведённый пример: 
    # $ mi_name = "Майк". 
    # Не забудьте добавить своего персонажа в файл «definitions.rpy»!
    $ s_name = "???"
    $ m_name = "Девушка 3"
    $ n_name = "Девушка 2"
    $ y_name = "Девушка 1"

    # Эта переменная указывает, включено ли быстрое меню в диалоговом окне.
    $ quick_menu = True

    # Эта переменная указывает, хотим ли мы нормальный или глючный стиль диалогов.
    # Для глючных диалогов используйте «style.edited».
    $ style.say_dialogue = style.normal

    # Эта переменная указывает, мертва ли сейчас Сайори. Настоятельно рекомендуется
    # оставить её значение как есть.
    $ in_sayori_kill = None
    
    # Эта переменная указывает, может ли игрок пропускать диалоги или переходы.
    $ allow_skipping = True
    $ config.allow_skipping = True

    ## Основная часть скрипта
    # Именно здесь и вызываются ваши скрипты!
    # «persistent.playthrough» указывает прогресс прохождения игрока, т.е. на каком он сейчас акте. (Первый, Второй, Третий, Четвёртый)
    if persistent.playthrough == 0:

        # Эта переменная ставит номер главы на X в зависимости от того, какой главой игрок сейчас наслаждается.
        $ chapter = 0

        # Это выражение вызова запускает конкретный лейбл в скрипте.
        call ch0_main
        
        # Это выражение вызова запускает мини-игру про сочинение стихотворений.
        call poem

        ## День 1
        $ chapter = 1
        call ch1_main

        # Это выражение вызова запускает мини-игру про обмен стихотворениями.
        call poemresponse_start
        call ch1_end

        call poem

        ## День 2
        $ chapter = 2
        call ch2_main
        call poemresponse_start
        call ch2_end

        call poem

        ## День 3
        $ chapter = 3
        call ch3_main
        call poemresponse_start
        call ch3_end

        ## День 4
        $ chapter = 4
        call ch4_main

        # Это выражение Python записывает файл в корневую папку игры или в папку Android/data/имя.пакета.абв/files
        python:
            try: open(user_dir + "/счхстлхвые мхсли.png", "rb")
            except: open(user_dir + "/счхстлхвые мхсли.png", "wb").write(renpy.file("hxppy thxughts.png").read())

        ## День 5
        $ chapter = 5
        call ch5_main

        # Это выражение вызова завершает игру, но не запускает титры.
        call endgame
        return

    elif persistent.playthrough == 1:
        $ chapter = 0
        call ch10_main
        
        # Это выражение прыжка заставляет интерпретатор «перескочить» на Второй акт из начала Первого.
        jump playthrough2


    elif persistent.playthrough == 2:
        ## День 1 - Акт 2
        $ chapter = 0
        call ch20_main

        label playthrough2:

            call poem

            python:
                try: open(user_dir + "/ТЫ МЕНЯ СЛЫШИШЬ.txt", "rb")
                except: open(user_dir + "/ТЫ МЕНЯ СЛЫШИШЬ.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())

            ## День 2 - Акт 2
            $ chapter = 1
            call ch21_main
            call poemresponse_start
            call ch21_end

            # Это выражение вызова запускает мини-игру про обмен стихотворениями, но без перехода.
            call poem(False)

            python:
                try: open(user_dir + "/яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя.txt", "rb")
                except: open(user_dir + "/яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())

            ## День 3 - Акт 2
            $ chapter = 2
            call ch22_main
            call poemresponse_start
            call ch22_end

            call poem(False)

            ## День 4 - Акт 2
            $ chapter = 3
            call ch23_main

            # Это выражение «если» либо вызывает особый обмен стихами, либо продолжает игру как обычно.
            if y_appeal >= 3:
                call poemresponse_start2
            else:
                call poemresponse_start

            # Это выражение «если» является остатками кода из наработок по DDLC,
            # который завершает игру, если она является демоверсией.
            if persistent.demo:
                stop music fadeout 2.0
                scene black with dissolve_cg
                "Конец демоверсии."
                return

            call ch23_end
            return

    elif persistent.playthrough == 3:
        jump ch30_main

    elif persistent.playthrough == 4:

        ## День 1 - Акт 4
        $ chapter = 0
        call ch40_main
        jump credits

# Этот лейбл «завершает» игру во время Первого акта.
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
