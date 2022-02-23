## cgs.rpy

# Этот файл содержит определения всех сценок (CG) у персонажей из DDLC, такие как сценка с Юри
# и шоколадной конфетой, и Нацуки с её мангой.

## Сценка с Юри и шоколадной конфетой [Тропа Юри 2]
# Это задний план сценки (стена класса).
image y_cg2_bg:
    "images/cg/y_cg2_bg1.png"
    6.0
    "images/cg/y_cg2_bg2.png" with Dissolve(1)
    2
    "images/cg/y_cg2_bg1.png" with Dissolve(1)
    1
    repeat

# Это базовая модель Юри, где она читает книгу и держит во рту шоколадку.
image y_cg2_base:
    "images/cg/y_cg2_base.png"

# Это изображение скрывает шоколадку на базовой модели Юри, оставляя её с открытым ртом. 
image y_cg2_nochoc:
    "images/cg/y_cg2_nochoc.png"
    on hide:
        linear 0.5 alpha 0

# Это изображение с трансформациями добавляет пару деталей к сценке, дабы придать ей блеска.
image y_cg2_details:
    "images/cg/y_cg2_details.png"
    alpha 1.00
    6.0
    linear 1.0 alpha 0.35
    1.0
    linear 1.0 alpha 1.0
    repeat

# Это изображение делает у Юри шокированное выражение лица на сценке.
image y_cg2_exp2:
    "images/cg/y_cg2_exp2.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

# Это изображение делает у Юри смущённое выражение лица на сценке.
image y_cg2_exp3:
    "images/cg/y_cg2_exp3.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

# Эти изображения с трансформациями добавляют слой с пылью поверх сценки, дабы придать ей блеска.
image y_cg2_dust1:
    "images/cg/y_cg2_dust1.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        10.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 14.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust2:
    "images/cg/y_cg2_dust2.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        28.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 32.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust3:
    "images/cg/y_cg2_dust3.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        13.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 17.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust4:
    "images/cg/y_cg2_dust4.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        15.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 19.0 xoffset -100 yoffset 100
        repeat

## Сценка с Нацуки, читающей мангу [Тропа Нацуки 1]
# Это задний план сценки (стена класса).
image n_cg1_bg:
    "images/cg/n_cg1_bg.png"

# Это базовая модель Нацуки, где она смотрит, как игрок читает мангу.
image n_cg1_base:
    "images/cg/n_cg1_base.png"

# Это изображение делает у Нацуки радостное выражение лица на сценке.
image n_cg1_exp1:
    "images/cg/n_cg1_exp1.png"

# Это изображение делает у Нацуки смущённое выражение лица на сценке.
image n_cg1_exp2:
    "images/cg/n_cg1_exp2.png"

# Это изображение делает у Нацуки сердитое выражение лица на сценке.
image n_cg1_exp3:
    "images/cg/n_cg1_exp3.png"

# Это изображение делает у Нацуки сонное выражение лица на сценке.
image n_cg1_exp4:
    "images/cg/n_cg1_exp4.png"

# Это изображение делает у Нацуки полусонное выражение лица на сценке.
image n_cg1_exp5:
    "images/cg/n_cg1_exp5.png"

# Это изображение искажает выражение лица Нацуки на сценке во Втором акте.
image n_cg1b = Composite((1280,720), (0,0), "images/cg/n_cg1b.png", (882,325), "n_rects1", (732,400), "n_rects2", (850,475), "n_rects3")

# Эти изображения с трансформациями закрывают глаза Нацуки чёрными квадратами во Втором акте.
image n_rects1:
    RectCluster(Solid("#000"), 12, 30, 30).sm
    pos (899, 350)
    xysize (34, 34)

image n_rects2:
    RectCluster(Solid("#000"), 12, 30, 24).sm
    pos (749, 430)
    xysize (34, 34)

image n_rects3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (764, 490)
    xysize (30, 20)

## Сценка с Нацуки внутри кладовки [Тропа Нацуки 2]
# Это задний план сценки (кладовка).
image n_cg2_bg:
    "images/cg/n_cg2_bg.png"

# Это базовая модель Нацуки, где она перекладывает свою мангу на другую полку.
image n_cg2_base:
    "images/cg/n_cg2_base.png"

# Это изображение делает у Нацуки обеспокоенное выражение лица на сценке.
image n_cg2_exp1:
    "images/cg/n_cg2_exp1.png"

# Это изображение делает у Нацуки кричащее выражение лица на сценке.
image n_cg2_exp2:
    "images/cg/n_cg2_exp2.png"

## Сценка с Нацуки, где произошёл инцидент на кухне [Тропа Нацуки 3]
# Это задний план сценки (кухонный пол).
image n_cg3_base:
    "images/cg/n_cg3_base.png"

# Это изображение добавляет глазурь для кексов на палец Нацуки.
image n_cg3_cake:
    "images/cg/n_cg3_cake.png"

# Это изображение делает у Нацуки такое выражение лица, будто она смеётся, на сценке.
image n_cg3_exp1:
    "images/cg/n_cg3_exp1.png"

# Это изображение делает у Нацуки смущённое выражение лица на сценке.
image n_cg3_exp2:
    "images/cg/n_cg3_exp2.png"

## Сценка с Юри, где она и игрок читают вместе [Тропа Юри 1]
# Это задний план сценки (парта в классе) и базовая модель Юри.
image y_cg1_base:
    "images/cg/y_cg1_base.png"

# Это изображение заставляет Юри посмотреть на Протагониста на сценке.
image y_cg1_exp1:
    "images/cg/y_cg1_exp1.png"

# Это изображение делает у Юри улыбающееся выражение лица на сценке.
image y_cg1_exp2:
    "images/cg/y_cg1_exp2.png"

# Это изображение заставляет Юри паниковать, словно яндере, на сценке.
image y_cg1_exp3:
    "images/cg/y_cg1_exp3.png"

## Сценка с Юри, где произошёл инцидент с краской [Тропа Юри 3]
# Это задний план сценки (комната Протагониста) и базовая модель Юри.
image y_cg3_base:
    "images/cg/y_cg3_base.png"

# Это изображение заставляет Юри закрыть глаза на сценке.
image y_cg3_exp1:
    "images/cg/y_cg3_exp1.png"

## Сценка с пиджаком Сайори [Тропа Сайори 1]
# Это задний план сценки (класс) и базовая модель Сайори.
image s_cg1:
    "images/cg/s_cg1.png"

## Сценка с Сайори, где она ударилась головой и упала на пол [Тропа Сайори 2]
# Это задний план сценки (кладовка в классе) и базовая модель Сайори.
image s_cg2_base1:
    "images/cg/s_cg2_base1.png"

# Это альтернативный задний план и базовая модель Сайори, где она держит
# бутылочку с яблочным соком в руке.
image s_cg2_base2:
    "images/cg/s_cg2_base2.png"

# Это изображение заставляет Сайори сжать зубы от боли на сценке.
image s_cg2_exp1:
    "images/cg/s_cg2_exp1.png"

# Это изображение делает у Сайори расстроенное выражение лица на сценке.
image s_cg2_exp2:
    "images/cg/s_cg2_exp2.png"
    
# Это изображение заставляет Сайори закрыть глаза на сценке.
image s_cg2_exp3:
    "images/cg/s_cg2_exp3.png"

## Сценка с Сайори, где она и игрок обнимаются [День 4]
# Это задний план сценки (снаружи дома Протагониста) и базовая модель Сайори.
image s_cg3:
    "images/cg/s_cg3.png"

## Сценка с Сайори, где она свела счёты с жизнью
# Это задний план сценки (комната Сайори).
image s_kill_bg:
    subpixel True
    "images/cg/s_kill_bg.png"

# Это изображение показывает повесившуюся Сайори на сценке.
image s_kill:
    subpixel True
    "images/cg/s_kill.png"

# Это искажённый вариант заднего плана сценки.
image s_kill_bg2:
    subpixel True
    "images/cg/s_kill_bg2.png"

# Это искажённый вариант спрайта повесившейся Сайори.
image s_kill2:
    subpixel True
    "images/cg/s_kill2.png"

## Сценка, где Юри умирает от ножевого ранения
# Это событие, опирающееся на данные условия, показывает конкретные изображения
# покончившей с собой Юри, опираясь на то, сколько времени прошло в игре.
image y_kill = ConditionSwitch(
    "persistent.yuri_kill >= 1380", "images/cg/y_kill/3a.png",
    "persistent.yuri_kill >= 1180", "images/cg/y_kill/3c.png",
    "persistent.yuri_kill >= 1120", "images/cg/y_kill/3b.png",
    "persistent.yuri_kill >= 920", "images/cg/y_kill/3a.png",
    "persistent.yuri_kill >= 720", "images/cg/y_kill/2c.png",
    "persistent.yuri_kill >= 660", "images/cg/y_kill/2b.png",
    "persistent.yuri_kill >= 460", "images/cg/y_kill/2a.png",
    "persistent.yuri_kill >= 260", "images/cg/y_kill/1c.png",
    "persistent.yuri_kill >= 200", "images/cg/y_kill/1b.png",
    "True", "images/cg/y_kill/1a.png"
    )

# Эта трансформация запускает анимацию заднего плана на сценке с повесившейся Сайори.
transform s_kill_bg_start:
    truecenter
    zoom 1.10
    linear 4 zoom 1.00

# Эта трансформация запускает анимацию спрайта повесившейся Сайори на вышеуказанной сценке.
transform s_kill_start:
    truecenter
    xalign 0.3 yalign 0.25 zoom 0.8
    linear 4 zoom 0.75 xalign 0.315 yoffset 10

# Это изображение с трансформацией делает приближение заднего плана на сценке с повесившейся Сайори.
image s_kill_bg_zoom:
    contains:
        "s_kill_bg"
        xalign 0.2 yalign 0.3 zoom 2.0
    dizzy(0.25, 1.0)

# Эта трансформация заставляет изображение или спрайт качаться так, будто у игрока головокружение.
transform dizzy(m, t, subpixel=True):
    subpixel subpixel
    parallel:
        xoffset 0
        ease 0.75 * t xoffset 10 * m
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset -5 * m
        ease 0.75 * t xoffset -3 * m
        ease 0.75 * t xoffset -10 * m
        ease 0.75 * t xoffset 0
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 1.0 * t yoffset 5 * m
        ease 2.0 * t yoffset -5 * m
        easein 1.0 * t yoffset 0
        repeat

# Это изображение с трансформацией делает приближение спрайта повесившейся Сайори на одноимённой сценке.
image s_kill_zoom:
    contains:
        "s_kill"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    dizzy(1, 1.0)

# Это изображение с трансформацией делает приближение искажённого фона сценки с повесившейся Сайори.
image s_kill_bg2_zoom:
    contains:
        "s_kill_bg2"
        xalign 0.2 yalign 0.3 zoom 2.0
    parallel:
        dizzy(0.25, 1.0)
    parallel:
        alpha 0.2
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.2
        repeat

# Это изображение с трансформацией делает приближение искажённого спрайта повесившейся Сайори на вышеуказанной сценке.
image s_kill2_zoom:
    contains:
        "s_kill2"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    parallel:
        dizzy(1, 1.0)
    parallel:
        alpha 0.3
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.4
        repeat
