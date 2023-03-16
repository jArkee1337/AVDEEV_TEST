Нужно сделать простой сервис проведения тестирования по каким-либо темам. Т.е. есть тесты с вариантами ответов, один или несколько вариантов должны быть правильными. Тесты группируются в наборы тестов, которые затем пользователь может проходить и видеть свой результат.
Функциональные части сервиса:

    • Регистрация пользователей
    • Аутентификация пользователей
    • Зарегистрированные пользователи могут проходить любой из тестовых наборов
    ▪ Последовательный ответ на все вопросы, каждый вопрос должен выводится на новой странице с отправкой формы (перескакивать через тесты или оставлять неотмеченными нельзя)
    ▪ После завершения тестирования смотреть результат:
    • количество правильных/неправильных ответов
    • процент правильных ответов
    • Админка. Стандартная админка Django. 
        Разделы:
        ◦ Стандартный раздел пользователей
        ◦ Раздел с наборами тестов
    ▪ Возможность на странице набора тестов добавлять вопросы/ответы к вопросам/отмечать правильные ответы
    ▪ Валидация на то, что должен быть хотябы 1 правильный вариант
    ▪ Валидация на то, что все варианты не могут быть правильными
    ▪ Удаление вопросов/вариантов ответов/изменение правильных решений при редактировании тестового набора


    
