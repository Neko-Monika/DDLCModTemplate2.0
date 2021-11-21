
## Оператор init offset повышает приоритет инициализации в этом файле над
## другими файлами, из-за чего инициализация здесь запускается первее.

init -2 python:
    # Устанавливает разрешение окна DDLC на 1280x720@60 Гц
    gui.init(1280, 720)

## Конфигурационные переменные интерфейса
define -2 gui.hover_sound = "gui/sfx/hover.ogg" # Звук при наведении на кнопку
define -2 gui.activate_sound = "gui/sfx/select.ogg" # Звук нажатия на кнопку
define -2 gui.activate_sound_glitch = "gui/sfx/select_glitch.ogg" # Глючный звуковой эффект

## Цвета!
## Эти строки кода настраивают цвет текста в DDLC

## Акцентный цвет используется в заголовках и подчёркнутых текстах.
define -2 gui.accent_color = '#ffffff'

## Цвет, используемый в текстовой кнопке, когда она не выбрана и не наведена.
define -2 gui.idle_color = '#aaaaaa'

## Small_color используется в маленьком тексте, который должен быть ярче/темнее,
## для того, чтобы выделяться.
define -2 gui.idle_small_color = '#333'

## Цвет, используемых в кнопках и панелях, когда они наведены.
define -2 gui.hover_color = '#cc6699'

## Цвет, используемый текстовой кнопкой, когда она выбрана, но не наведена.
define -2 gui.selected_color = '#bb5588'

## Цвет, используемый текстовой кнопкой, когда она не может быть выбрана.
define -2 gui.insensitive_color = '#aaaaaa7f'

## Цвета, используемые для частей панелей, которые не заполняются. Они
## используются не напрямую, а только при воссоздании файлов изображений.
define -2 gui.muted_color = '#6666a3'
define -2 gui.hover_muted_color = '#9999c1'

## Цвета, используемые в тексте диалогов и выборов.
define -2 gui.text_color = '#ffffff'
define -2 gui.interface_text_color = '#ffffff'

## Шрифты и их размеры

## Шрифт, используемый внутриигровым текстом.
define -2 gui.default_font = "gui/font/comic.ttf"

## Шрифт, используемый именами персонажей.
define -2 gui.name_font = "gui/font/Rotonda.ttf"

## Шрифт, используемый текстом вне игры.
define -2 gui.interface_font = "DejaVuSans.ttf"

## Размер нормального текста диалога.
define -2 gui.text_size = 20

## Размер имён персонажей.
define -2 gui.name_text_size = 22

## Размер текста в пользовательском интерфейсе.
define -2 gui.interface_text_size = 22

## Размер заголовков в пользовательском интерфейсе.
define -2 gui.label_text_size = 24

## Размер текста на экране уведомлений.
define -2 gui.notify_text_size = 16

## Размер заголовка игры.
define -2 gui.title_text_size = 38

## Главное и игровое меню

## Устанавливает фоновое изображение для Главного меню
define -2 gui.main_menu_background = "menu_bg"

## Устанавливает фоновое изображение для экрана Паузы
define -2 gui.game_menu_background = "game_menu_bg"

## Контролирует поведение отображения плашки с названием и версией игры
define -2 gui.show_name = False

## Диалог

## Высота текстового окна, содержащего диалог.
define -2 gui.textbox_height = 182

## Местоположение текстового окна по вертикали экрана. 0.0 — верх, 0.5 — центр и
## 1.0 — низ.
define -2 gui.textbox_yalign = 0.99

## Местоположение имени говорящего персонажа по отношению к текстовому окну.
## Это могут быть целые значения в пикселях слева и сверху от начала окна или
## процентное отношение, например, 0.5 для центрирования.
define gui.name_xpos = 350
define gui.name_ypos = -3

## Горизонтальное выравнивание имени персонажа. Это может быть 0.0 для
## левоориентированного, 0.5 для центрированного и 1.0 для правоориентированного
## выравнивания.
define gui.name_xalign = 0.5

## Ширина, высота и границы окна, содержащего имя персонажа или None, для
## автоматической размерки.
define gui.namebox_width = 168
define gui.namebox_height = 39

## Границы окна, содержащего имя персонажа слева, сверху, справа и снизу по
## порядку.
define gui.namebox_borders = Borders(5, 5, 5, 2)

## Если True, фон текстового окна будет моститься (расширяться по эффекту
## плитки). Если False, фон текстового окна будет фиксированным.
define gui.namebox_tile = False


## Размещение диалога по отношению к текстовому окну. Это могут быть целые
## значения в пикселях слева и сверху от текстового окна или процентное
## отношение, например, 0.5 для центрирования.
define gui.text_xpos = 268
define gui.text_ypos = 62

## Максимальная ширина текста диалога в пикселях.
define gui.text_width = 744

## Горизонтальное выравнивание текста диалога. Это может быть 0.0 для
## левоориентированного, 0.5 для центрированного и 1.0 для правоориентированного
## выравнивания.
define gui.text_xalign = 0.0

## Кнопки

## Эти переменные, вместе с файлами изображений в gui/button, контролируют
## аспекты того, как отображаются кнопки.

## Ширина и высота кнопки в пикселях. Если None, Ren'Py самостоятельно
## рассчитает размер.
define gui.button_width = None
define gui.button_height = 36

## Границы каждой стороны кнопки в порядке слева, сверху, справа, снизу.
define gui.button_borders = Borders(4, 4, 4, 4)

## Если True, фоновое изображение будет моститься. Если False, фоновое изображение будет
## линейно масштабировано.
define gui.button_tile = False

## Шрифт, используемый кнопкой.
define gui.button_text_font = gui.interface_font

## Размер текста, используемый кнопкой.
define gui.button_text_size = gui.interface_text_size

## Цвет текста в кнопке в различных состояниях.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Горизонтальное выравнивание текста в кнопке. (0.0 — лево, 0.5 — по центру,
## 1.0 — право).
define gui.button_text_xalign = 0.0

## Эти переменные переписывают настройки различных видов кнопок. Пожалуйста,
## посмотрите документацию по gui для просмотра всех вариаций кнопок и для чего
## каждая из них нужна.
##
## Эти настройки используются стандартным интерфейсом:

define gui.radio_button_borders = Borders(28, 4, 4, 4)

define gui.check_button_borders = Borders(28, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

#define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = "#522"
define gui.quick_button_text_hover_color = "#fcc"
define gui.quick_button_text_selected_color = gui.accent_color
define gui.quick_button_text_insensitive_color = "#a66"

## Вы также можете добавить собственные настройки, добавляя правильно
## именованные переменные. Например, вы можете раскомментировать следующую
## строчку, чтобы установить ширину кнопок навигации.

# define gui.navigation_button_width = 250

## Кнопки выбора

## Кнопки выбора используются во внутриигровых меню.

define gui.choice_button_width = 420
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.default_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#000"
define gui.choice_button_text_hover_color = "#fa9"

## Кнопки слотов

## Кнопка слотов — особый вид кнопки. Она содержит миниатюру и текст,
## описывающий слот сохранения. Слот сохранения использует файлы из gui/button,
## как и другие виды кнопок.

## Кнопка слота сохранения.
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_hover_color = gui.hover_color

## Ширина и высота миниатюры, используемой слотом сохранения.
define config.thumbnail_width = 256
define config.thumbnail_height = 144

## Количество колонок и рядов в таблице слотов.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

## Позиционирование и интервалы

## Эти переменные контролируют позиционирование и интервалы различных элементов
## пользовательского интерфейса.

## Местоположение левого края навигационных кнопок по отношению к левому краю
## экрана.
define gui.navigation_xpos = 80

## Вертикальная позиция индикатора пропуска.
define gui.skip_ypos = 10

## Вертикальная позиция экрана уведомлений.
define gui.notify_ypos = 45

## Интервал между выборами в меню.
define gui.choice_spacing = 22

## Кнопки в секции навигации главного и игрового меню.
define gui.navigation_spacing = 6

## Контролирует интервал между настройками.
define gui.pref_spacing = 10

## Контролирует интервал между кнопками настройки.
define gui.pref_button_spacing = 0

## Интервал между кнопками страниц.
define gui.page_spacing = 0

## Интервал между слотами.
define gui.slot_spacing = 10

## Рамки

## Эти переменные контролируют вид рамок, содержащих компоненты
## пользовательского интерфейса, когда наложения или окна не представлены.

## Генерируем рамки.
define gui.frame_borders = Borders(4, 4, 4, 4)

## Рамки, используемые в частях экрана подтверждения.
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

## Рамки, используемые в частях экрана пропуска.
define gui.skip_frame_borders = Borders(16, 5, 50, 5)

## Рамки, используемые в частях экрана уведомлений.
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

## Должны ли фоны рамок моститься?
define gui.frame_tile = False

## Панели, Полосы прокрутки и Ползунки

## Эти настройки контролируют вид и размер панелей, полос прокрутки и ползунков.

## Стандартный GUI использует только ползунки и вертикальные полосы прокрутки.
## Все остальные полосы используются только в новосозданных экранах.

## Высота горизонтальных панелей, полос прокрутки и ползунков. Ширина
## вертикальных панелей, полос прокрутки и ползунков.
define gui.bar_size = 36
define gui.scrollbar_size = 12
define gui.slider_size = 30

## True, если изображения панелей должны моститься. False, если они должны быть
## линейно масштабированы.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Горизонтальные границы.
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

## Вертикальные границы.
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

## Что делать с непрокручиваемыми полосами прокрутки в интерфейсе. "hide" прячет
## их, а None их показывает.
define gui.unscrollable = "hide"

## История

## Экран истории показывает диалог, который игрок уже прошёл.

## Количество диалоговых блоков истории, которые Ren'Py будет хранить.
define config.history_length = 50

## Высота доступных записей на экране истории, или None, чтобы задать высоту в
## зависимости от производительности.
define gui.history_height = None

## Местоположение, ширина и выравнивание заголовка, показывающего имя говорящего
## персонажа.
define gui.history_name_xpos = 150
define gui.history_name_ypos = 0
define gui.history_name_width = 150
define gui.history_name_xalign = 1.0

## Местоположение, ширина и выравнивание диалогового текста.
define gui.history_text_xpos = 170
define gui.history_text_ypos = 5
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0

## Режим NVL

## Экран режима NVL показывает диалог NVL персонажей.

## Границы фона окна NVL.
define gui.nvl_borders = Borders(0, 10, 0, 20)

## Высота доступных строчек в режиме NVL. Установите на None, чтобы строчки
## динамически регулировали свою высоту.
define gui.nvl_height = 115

## Интервал между строчками в режиме NVL, если gui.nvl_height имеет значение
## None, а также между строчками и меню режима NVL.
define gui.nvl_spacing = 10

## Местоположение, ширина и выравнивание заголовка, показывающего имя говорящего
## персонажа.
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

## Местоположение, ширина и выравнивание диалогового текста.
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

## Местоположение, ширина и выравнивание текста nvl_thought (текст от лица
## персонажа nvl_narrator).
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

## Местоположение кнопок меню NVL.
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

