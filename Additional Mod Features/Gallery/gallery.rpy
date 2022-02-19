## Авторское право 2019-2023 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.

# gallery.rpy
# Данный файл содержит код меню галереи, отображающей фоны и
# спрайты вашей модификации.

default persistent.gallery_imgs = {}

init -1 python in gallery:
    from store import Transform, persistent, config, Hide, Composite
    import os
    import renpy.display.image as imgcore
    galleryList = {}
    user_dir = os.environ["ANDROID_PUBLIC"] if renpy.android else config.basedir

    # Этот класс определяет код для создания изображения для меню Галереи.
    # Синтаксис:
    # image - Эта переменная содержит путь к изображению или тег оного
    #         (напр. sayori 1a).
    # small_size - Эта переменная содержит путь к уменьшенной версии
    #              изображения или тег оной.
    # name - Эта переменная содержит читабельное название изображения
    #        в Галерее.
    # artist - Эта переменная содержит читабельное имя автора изображения.
    # sprite - Эта переменная указывает, является ли объявленное изображение
    #          спрайтом персонажа.
    # already_unlocked - Эта переменная указывает, что изображение будет
    #                    открытым сразу же после запуска игры.
    class GalleryImage:

        def __init__(self, image, small_size=None, name=None, artist=None, sprite=False, already_unlocked=False):
            # Тег изображения или путь к оному.
            self.file = image

            # Читабельное название изображения.
            if name: self.name = name
            else: self.name = image

            if self.name not in persistent.gallery_imgs:
                persistent.gallery_imgs[self.name] = {
                    "unlocked": True if already_unlocked else False
                }

            # Читабельное имя автора изображения.
            self.artist = artist

            # Это условие указывает, является ли данное изображение спрайтом.
            self.sprite = sprite

            self.unlocked = persistent.gallery_imgs[self.name]['unlocked']

            if sprite:
                self.image = Composite(
                    (config.screen_width, config.screen_height), (0, 0), 
                    "black", (0.2 * (config.screen_width / 1280.0), 0), 
                    Transform(image, zoom=0.75*0.95)
                )

                # Уменьшенная версия главного изображения.
                if small_size:
                    self.small_size = small_size 
                else:               
                    self.small_size = Composite(
                        (234, 132), (0, 0), 
                        "black", (0.2, 0), 
                        Transform(image, zoom=0.137)
                    )
            else:
                self.image = Transform(image, size=(config.screen_width, config.screen_height-40))

                if small_size:
                    self.small_size = small_size 
                else:     
                    self.small_size = Transform(image, size=(234, 132))

            galleryList[self.name] = self
        
        def unlock(self):
            self.unlocked = True
            persistent.gallery_imgs[self.name]['unlocked'] = True

        # Эта функция экспортирует выбранное изображение на устройство игрока.
        def export(self):
            try: os.mkdir(f"{user_dir}/gallery")
            except: pass

            if self.sprite: renpy.show_screen("dialog", message=_("Спрайты не могут быть экспортированы в папку галереи. Повторите попытку с другим изображением."), ok_action=Hide("dialog"))
            else:
                renpy.file(self.file)
                export = self.file

                with open(f"{user_dir}/gallery/{os.path.splitext(export)[0].split('/')[-1]}{os.path.splitext(export)[-1]).replace('\\', '/')}", "wb") as p:
                    p.write(renpy.file(export).read())

                renpy.show_screen("dialog", message=f"Изображение «{self.name}» было экспортировано в папку галереи."), ok_action=Hide("dialog"))

init python:
    # from store.gallery import GalleryImage, galleryList
    current_img_name = None
    # Эта функция совершает переход к следующему/предыдущему изображению в галерее.
    def next_image(back=False):
        global current_img_name

        # Создаёт новый список на основе ключей словаря.
        all_keys = [k for k, v in galleryList.items() if v.unlocked]

        # Берёт текущий ключ в качестве индекса.
        current_index = all_keys.index(current_img_name)

        # Берёт следующий ключ в качестве индекса.
        next_index = current_index - 1 if back else current_index + 1

        try: 
            all_keys[next_index]
            current_img_name = all_keys[next_index]
        except IndexError: current_img_name = all_keys[0]

    # В этом разделе объявляются изображения, показываемые в галерее. См. 
    # синтаксис класса GalleryMenu, чтобы добавить своё изображение.
    residential = GalleryImage("bg residential_day", already_unlocked=True)
    s1a = GalleryImage("sayori 1", sprite=True, already_unlocked=True)
    m1a = GalleryImage("monika 1", name=_("Моника"), artist="Satchely", sprite=True)

    # Быстрая сортировка (НЕ УДАЛЯТЬ)
    galleryList = {k: galleryList[k] for k in sorted(galleryList)}

## Экран Галереи ##############################################################
##
## Этот экран используется для создания галереи внутриигровых артов, которые
## игрок может просмотреть в главном меню.
##
## Синтаксис:
## gl.image - Эта переменная содержит путь к изображению или тег оного
##            (напр. sayori 1a).
## gl.small_size - Эта переменная содержит путь к уменьшенной версии
##                 изображения или тег оной.
## gl.name - Эта переменная содержит читабельное название изображения
##           в галерее.
## gl.sprite - Эта переменная проверяет, является ли объявленное
##             изображение спрайтом персонажа.
## gl.locked - Эта переменная указывает, должно ли добавляться это изображение
##             в галерею, если оно ещё не было увидено в игре.
screen gallery():

    tag menu

    use game_menu(_("Галерея")):

        fixed:

            vpgrid:
                id "gvp"

                rows math.ceil(len(galleryList) / 3.0)

                if len(galleryList) > 3:
                    cols 3
                else:
                    cols len(galleryList)

                spacing 25
                mousewheel True

                xalign 0.5
                yalign 0.5

                for name, gl in galleryList.items():
                    vbox:
                        if gl.unlocked:
                            imagebutton:
                                idle gl.small_size
                                action [SetVariable("current_img_name", name), ShowMenu("preview"), With(Dissolve(0.5))]
                            text "[name!t]":
                                xalign 0.5
                                color "#555"
                                outlines []
                                size 14
                        else:
                            imagebutton:
                                idle "mod_assets/mod_extra_images/galleryLock.png"
                                action Show("dialog", message=_("Это изображение закрыто. Продолжайте своё прохождение «[config.name!t]», чтобы открыть его."), ok_action=Hide("dialog"))
                            text _("Закрыто"):
                                xalign 0.5
                                color "#555"
                                outlines []
                                size 14

            vbar value YScrollValue("gvp") xalign 0.99 ysize 560

## Экран Галереи ##################################################################
##
## Этот экран показывает выбранное игроком изображение крупным планом.
screen preview():

    tag menu

    hbox: 
        add galleryList[current_img_name].image yoffset 40
    hbox:
        add Solid("#fcf") size(config.screen_width, 40)

    hbox:
        ypos 0.005
        xalign 0.5 
        text current_img_name: 
            color "#000"
            outlines []
            size 24 

    hbox:
        ypos 0.005
        xalign 0.98
        if galleryList[current_img_name].artist:
            textbutton "?":
                text_style "navigation_button_text"
                action Show("dialog", message=_(f"Художник: {galleryList[current_img_name].artist}"), ok_action=Hide("dialog"))

        textbutton _("Э"):
            text_style "navigation_button_text"
            action Function(galleryList[current_img_name].export) 

        textbutton _("Х"):
            text_style "navigation_button_text"
            action ShowMenu("gallery")

    textbutton "<":
        text_style "navigation_button_text"
        xalign 0.0
        yalign 0.5
        action Function(next_image, True)

    textbutton ">":
        text_style "navigation_button_text"
        xalign 1.0
        yalign 0.5
        action Function(next_image)

    on "replaced" action With(Dissolve(0.5))
