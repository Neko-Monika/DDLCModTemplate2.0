# Использование Мод-шаблона для DDLC с Xcode

![Модификация для DDLC в Xcode](https://marquiskurt.net/images/covers/2019-06-09-cover.png)

Данный шаблон идёт с поддержкой сборки и запуска в Xcode, что освещено в этом обучении по Ren'Py/Xcode: https://marquiskurt.net/2019/06/09/post.html.

Но перед тем, как запустить проект, есть пара вещей, которые *надо* настроить, дабы всё работало нормально.

## Изменить значение `RENPY_TOOL`

Измените в файле **Config.xcconfig** значение переменной `RENPY_TOOL` так, чтобы она указывала на директорию установленной копии Ren'Py. Например:

```xcconfig
// Измените строку ниже так, чтобы она указывала на директорию вашей установленной копии Ren'Py!
//RENPY_TOOL=/какая-то/директория/renpy/renpy.sh
RENPY_TOOL=/Applications/renpy-6.99.12.4-sdk/renpy.sh
```

## Изменить исполняемый файл в Схемах

1. На панели инструментов Xcode выберите строку, в которой написано "DDLCModTemplate > Мой Mac", и выберите "Редактировать схему".
2. На панели Информация, под разделом "Запуск", щёлкните на поле **Исполняемый файл** и выберите "Другое".
3. Появится диалоговое окно с выбором файла; перейдите в директорию, где установлена ваша копия Ren'Py, и выберите `renpy.app`.

## Проверка изменений

После того, как вы внесёте эти правки и добавите файлы DDLC, необходимые для нормального запуска шаблона, щёлкните на кнопку Играть или нажмите клавиши Command+R на клавиатуре, чтобы протестировать процедуру сборки/запуска.

Если у вас всё ещё возникают проблемы, следуйте шагам в [обучении](https://marquiskurt.net/2019/06/09/post.html) и проверьте, что параметры проекта указаны корректно.
