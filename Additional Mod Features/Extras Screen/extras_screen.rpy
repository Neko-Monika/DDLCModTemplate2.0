## Авторское право 2019-2023 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.

# extras_screen.rpy
# В этом файле содержится код экрана для меню Доп. контента, которое отображает 
# кнопки перехода на другие экраны (Достижения/Галерея).
#
# Для добавления нового слота в этом меню увеличьте число строк или столбцов, а затем скопируйте
# и вставьте нижеприведённые рамки для основы вашего отдельного пункта меню Доп. контента.
# Убедитесь, что vpgrid заполнен, в противном случае у вас возникнет исключение.
# Используйте `null` (без знаков `), если вам нужно заполнить пустое пространство, либо добавьте
# свойство `allow_underfull True` (также без знаков `).

default enable_gallery = True
default enable_achievements = True

screen extras():
    tag menu
    style_prefix "extras"

    use game_menu(_("Доп. контент")):

        fixed:

            vpgrid id "ext":

                rows 1
                cols 3

                xalign 0.5
                yalign 0.4

                spacing 18

                if enable_gallery:
                    frame:
                        xsize 160
                        ysize 140

                        vbox:
                            xalign 0.5
                            yalign 0.5

                            imagebutton:
                                idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/gallery.png", (32, 75), Text(_("Галерея"), style="extras_text"))
                                hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/gallery.png", (30, 73), Text(_("Галерея"), style="extras_hover_text"))
                                action ShowMenu("gallery")

                if enable_achievements: 
                    frame:
                        xsize 160
                        ysize 140

                        vbox:
                            xalign 0.5
                            yalign 0.5

                            imagebutton:
                                idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/achievements.png", (29, 75), Text(_("Награды"), style="extras_text"))
                                hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/achievements.png", (27, 73), Text(_("Награды"), style="extras_hover_text"))
                                action ShowMenu("achievements")

                frame:
                    xsize 160
                    ysize 140

                    vbox:
                        xalign 0.5
                        yalign 0.5

                        imagebutton:
                            idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/about.png", (36, 75), Text(_("Авторы"), style="extras_text"))
                            hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/about.png", (34, 73), Text(_("Авторы"), style="extras_hover_text"))
                            action ShowMenu("about")

            vbar value YScrollValue("ext") xalign 0.99 ysize 560

style extras_text:
    font gui.interface_font
    color "#000"
    outlines []
    size 20

style extras_hover_text is extras_text:
    outlines [(2, "#cacaca", 0, 0), (2, "#cacaca", 2, 2)]

style extras_image_button:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
