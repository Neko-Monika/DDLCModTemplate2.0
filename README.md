# Добро пожаловать в Новый клуб модификаций!

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K22K8SU)

<u>Загрузки</u>: [2.4.9 (Стандартный шаблон с поддержкой Android)](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases/2.4.9) | [2.3.1-u8 (Стандартный шаблон)](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases/2.3.1-u8)

**Новый** Мод-шаблон для DDLC - это мод-шаблон, созданный GanstaKingofSA для **оригинальной** игры «Литературный клуб "Тук-тук!"», который придерживается требований [Руководства по использованию интеллектуальной собственности Team Salvato](http://teamsalvato.com/ip-guidelines/) для фанатских модов, работающих на движке Ren'Py версий 6.99.12.4 и 7.3.5 - 7.4.5, а также 7.4.9 - 7.4.10.

### **<u>Просьба разработчика</u>**
> Если этот шаблон был полезен для вас, пожалуйста, упомяните меня в релизах ваших модификаций. Не все разработчики инструментариев для модификаций получают столько же благодарности от людей, не находящихся в моддинг-сообществе, сколько обычные команды разработчиков модификаций, и не было бы лишним поблагодарить тех, кто приложил усилия, чтобы сделать моддинг проще, дабы вы могли создать свою модификацию для других.

### Отказ от ответственности
Данный шаблон предназначен для оригинальных фанатских игр по DDLC и модификаций, использующих ресурсы DDLC. 
Он не предназначен для проектов, которые их не используют, или в качестве кода, который будет скопирован в ваш проект, не относящийся к DDLC.
Большая часть кода в данном шаблоне является интеллектуальной собственностью Team Salvato, и она не может быть скопирована в фанатские проекты или модификации, не имеющие отношения к DDLC.
Мод-шаблон для DDLC никоим образом не связан с Team Salvato.

### Начало работы для новичков (Ren'Py 6)
Следуйте шагам, приведённым [здесь](https://ganstakingofsa.github.io/information/guides/Installing-the-Mod-Template-Legacy.html), чтобы установить мод-шаблон.
> Как только вы закончите писать свой скрипт, выберите *Построить дистрибутивы*. Снимите флажки со всех вариантов и отметьте только `DDLC-совместимый мод на Ren'Py 6`, после чего нажмите на <u>Построить</u>. Это создаст кроссплатформенный .ZIP-архив с файлами вашей модификации.

### Начало работы для продвинутых пользователей (Ren'Py 7)
Следуйте шагам, приведённым [здесь](https://ganstakingofsa.github.io/information/guides/Installing-the-Mod-Template-Recent.html), чтобы установить мод-шаблон.
> Как только вы закончите писать свой скрипт, выберите *Построить дистрибутивы*. Снимите флажки со всех вариантов и отметьте только `DDLC-совместимый мод на Ren'Py 7`, после чего нажмите на <u>Построить</u>. Это создаст кроссплатформенный .ZIP-архив с файлами вашей модификации.

### Начало работы для портирования/моддинга на Android (шаблоны версии 2.4.0 и выше)
Прочтите файл [*guide.pdf*](guide.pdf) для подробной информации о создании вашей модификации на Android.
> В случае со старыми шаблонами, читайте PDF-документ, вложенный в ZIP-архив вашей копии шаблона, так как последняя ревизия руководства может не подойти к вашему текущему шаблону.

### Template Features
1. Сборка на Ren'Py версий 6 или 7!
2. Заставка при первом запуске вашей модификации.
3. Оригинальные RPY-файлы DDLC с пояснениями.
4. Кастомизация! Используйте шаблон как отправную точку для любых идей, которые вы хотите воплотить в реальность.
5. Поддержка Пакетов приложений macOS (`.app`) и Bash-файлов Linux (`.sh`).
6. Поддержка Android!
7. Поддержка Xcode! Открыв этот проект в Xcode, вы сможете редактировать, собирать и запускать модификацию, не открывая Лаунчер Ren'Py!
    > Примечание: Вам понадобится изменить значение переменной `RENPY_TOOL` и директорию пакета приложения Ren'Py в целевой схеме Xcode. [Подробнее &rsaquo;](XCODE.md)
8. [БЕТА] Поддержка местоимений! Дайте возможность пользователям выбрать подходящее для них местоимение!
    > См. файл *pronoun_example.rpy* в папке `game`, чтобы ознакомиться с примером использования этой функции.
9. Улучшенный Синий экран смерти! Теперь создать свой внутриигровой Синий экран смерти стало проще, чем когда-либо, на всех операционных системах! (даже на macOS и Linux!)

### Добавленные особенности
1. Подробное руководство по мини-игре по написанию стихотворения от Terra!
2. Поддержка Xcode для macOS от Alicerunsonfedora!
3. Поддержка NVL, спасибо Yagamirai01!

### Возвращённые функции
1. Призрачное меню (жуткая пасхалка от Дэна).
2. Скрипт убийства Сайори (если вы удалите Сайори до начала игры, появится новый экран).
3. Скрипт убийства Моники (если вы удалите Монику перед тем, как начать новую игру, запустится новый скрипт).
4. Особые стихотворения! (случайные стихи, появляющиеся во втором акте DDLC).
5. Реакции на стихотворения! (девушки делятся своим мнением о ваших стихотворениях!)

Данный шаблон идёт в комплекте с [DDMMaker](https://github.com/GanstaKingofSA/DDLC-ModMaker/releases), версией Ren'Py SDK, которая собирает только модификации для DDLC.

Авторское право © 2019-2021 GanstaKingofSA. Все права защищены.

Игра «Литературный клуб "Тук-тук!"» и её составляющие являются собственностью Team Salvato (Dan Salvato LLC). Авторское право © 2017 Team Salvato. Все права защищены.

Перевод оригинального сценария (с рядом мелких правок) и прочие оптимизации для кроссплатформенности позаимствованы из русификатора от Энтузиасты Team.
