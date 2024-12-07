workspace {

    model {
        user = person "Пользователь" {
            description "Пользователь системы электронной почты."
        }

        emailSystem = softwareSystem "Приложение электронной почты (Outlook)" {
            description "Система для управления электронной почтой."

            // Основные агрегаты
            userAccount = container "Учетная запись пользователя" {
                description "Содержит информацию о пользователе и его предпочтениях."
                technology "Java, Spring Boot"
            }

            emailMessage = container "Сообщение электронной почты" {
                description "Содержит данные о сообщении, включая отправителя, получателя, тему и содержание."
                technology "Java, Spring Boot"
            }

            inbox = container "Входящие сообщения" {
                description "Содержит все входящие сообщения пользователя."
                technology "Java, Spring Boot"
            }

            ui = container "Пользовательский интерфейс" {
                description "Веб-приложение для доступа к электронной почте."
                technology "HTML, CSS, JavaScript"
            }

            appServer = container "Сервер приложений" {
                description "Обрабатывает бизнес-логику и взаимодействие с пользователем."
                technology "Java, Spring Boot"
            }

            database = container "База данных" {
                description "Хранит данные о пользователях и сообщениях."
                technology "PostgreSQL"
            }
        }

        externalMailServer = softwareSystem "Внешний почтовый сервер" {
            description "Система для отправки и получения электронной почты."
        }

        // Определение взаимодействий
        user -> ui "Заполняет форму и отправляет сообщение"
        ui -> appServer "Отправляет данные формы"
        appServer -> userAccount "Проверяет учетные данные"
        appServer -> emailMessage "Создает новое сообщение"
        appServer -> inbox "Сохраняет сообщение во входящих"
        appServer -> database "Сохраняет сообщение в базе данных"
        appServer -> externalMailServer "Отправляет электронное письмо"
        externalMailServer -> appServer "Подтверждение отправки"
        appServer -> ui "Подтверждение отправки сообщения"
    }

    views {
        // Диаграмма контекста
        systemContext emailSystem {
            title "Диаграмма контекста приложения электронной почты"
            include *
            autolayout lr
        }

        // Диаграмма контейнеров
        container emailSystem {
            title "Контейнерная диаграмма приложения электронной почты"
            include *
            autolayout lr
        }

        // Динамическая диаграмма отправки электронного письма
        dynamic emailSystem {
            title "Динамическая диаграмма отправки электронного письма"

            // Определяем участников динамической диаграммы
            user -> ui "Заполняет форму и отправляет сообщение"
            ui -> appServer "Отправляет данные формы"
            appServer -> emailMessage "Создает новое сообщение"
            appServer -> inbox "Сохраняет сообщение во входящих"
            appServer -> database "Сохраняет сообщение в базе данных"
            appServer -> externalMailServer "Отправляет электронное письмо"
            externalMailServer -> appServer "Подтверждение отправки"
            appServer -> ui "Подтверждение отправки сообщения"
            
            autolayout lr
        }

        theme default
    }
}
