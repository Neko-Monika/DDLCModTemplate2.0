
# exceptions.rpy
# В данном файле содержатся сообщения об исключениях во время работы DDLC/мод-шаблона
# НЕ ИЗМЕНЯЙТЕ ЭТОТ ФАЙЛ!

python early:
    
    class NotRenPyEight(Exception):
        def __str__(self):
            return "Данная версия мод-шаблона предназначена для Ren'Py 8.\nСкачайте последнюю версию SDK с официального сайта, или, если оная у вас уже есть, соберите свою модификацию на ней."

    class DDLCRPAsMissing(Exception):
        def __init__(self, archive):
            self.archive = archive

        def __str__(self):
            return "Файл «" + self.archive + ".rpa» не был найден в папке игры. Проверьте правильность установки модификации на оригинальную DDLC и повторите попытку."

    class IllegalModLocation(Exception):
        def __str__(self):
            return "Модификации для DDLC и проекты оных не могут быть запущены из папки облачного хранилища. Переместите папку модификации/проекта в другую директорию и повторите попытку."
