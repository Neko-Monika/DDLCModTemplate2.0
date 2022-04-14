## Авторское право 2019-2022 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.

## renpy_patches.rpy
# Этот файл, в основном, предназначен для патчинга конкретных версий Ren'Py, которые ломают
# DDLC или модификации к ней, путём внесения правок в движок Ren'Py перед стартом.

init -1 python:
    ## Исправляет спецэффекты в классе, витающем в космосе, где игрок сидит наедине с Моникой, но это
    ## отключает OpenGL 2 даже в тех модификациях, которые его используют. Если вы используете OpenGL 2,
    ## закомментируйте нижеприведённые строки.
    if renpy.version_tuple >= (7, 4, 5, 1648):
        config.gl2 = False

### НЕ МОДИФИЦИРУЙТЕ НИЧЕГО, ЧТО ИДЁТ ПОСЛЕ ЭТОГО КОММЕНТАРИЯ ###

## Исправляет команды «wmic» так, чтобы вместо них использовались оные для «powershell».
python early:
    import os
    os.environ['wmic process get Description'] = "powershell (Get-Process).ProcessName"
    os.environ['wmic os get version'] = "powershell (Get-WmiObject -class Win32_OperatingSystem).Version"

init -1 python:
    ## Исправляет баги трансформаций в версиях 7.4.6 - 7.4.8.
    if renpy.version_tuple >= (7, 4, 6, 1693) and renpy.version_tuple < (7, 4, 9, 2142):

        class NewSceneLists(renpy.display.core.SceneLists):

            @staticmethod
            def add(self,
                layer,
                thing,
                key=None,
                zorder=0,
                behind=[ ],
                at_list=[ ],
                name=None,
                atl=None,
                default_transform=None,
                transient=False,
                keep_st=False):

                if not isinstance(thing, renpy.display.core.Displayable):
                    raise Exception("Попытка отобразить что-то, что не является отображаемым элементом: " + repr(thing))

                if layer not in self.layers:
                    raise Exception("Попытка добавить что-то на несуществующий слой '%s'." % layer)

                if key:
                    self.remove_hide_replaced(layer, key)
                    self.at_list[layer][key] = at_list

                if key and name:
                    self.shown.predict_show(layer, name)

                if transient:
                    self.additional_transient.append((layer, key))

                l = self.layers[layer]

                if atl:
                    thing = renpy.display.motion.ATLTransform(atl, child=thing)

                add_index, remove_index, zorder = self.find_index(layer, key, zorder, behind)

                at = None
                st = None

                if remove_index is not None:
                    sle = l[remove_index]
                    old = sle.displayable

                    at = sle.animation_time

                    if keep_st:
                        st = sle.show_time

                    if (not atl and
                            not at_list and
                            renpy.config.keep_running_transform and
                            isinstance(old, renpy.display.motion.Transform)):

                        thing = sle.displayable._change_transform_child(thing)
                    else:
                        thing = self.transform_state(l[remove_index].displayable, thing)

                    thing.set_transform_event("replace")

                else:

                    if not isinstance(thing, renpy.display.motion.Transform):
                        thing = self.transform_state(default_transform, thing)

                    thing.set_transform_event("show")

                sle = renpy.display.core.SceneListEntry(key, zorder, st, at, thing, name)
                l.insert(add_index, sle)
                
                if remove_index is not None:
                    if add_index <= remove_index:
                        remove_index += 1

                    self.hide_or_replace(layer, remove_index, "replaced")

                # используется visit_all вместо _show() в связи с устареванием
                thing.visit_all(lambda d : None)

        renpy.display.core.SceneLists.add = NewSceneLists.add

    ## Исправляет проблему, из-за которой некоторые переходы (задний план меню) начинали проигрываться заново.
    if renpy.version_tuple >= (7, 4, 7, 1862):
        config.atl_start_on_show = False 
