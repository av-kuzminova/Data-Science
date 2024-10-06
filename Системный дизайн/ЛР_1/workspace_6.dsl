workspace {

    model {
        user = person "Пользователь" {
            description "Пользователь системы электронной почты."
        }

        emailSystem = softwareSystem "Приложение электронной почты (Outlook)" {
            description "Система для управления электронной почтой."

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
        appServer -> database "Сохраняет сообщение в базе данных"
        appServer -> externalMailServer "Отправляет электронное письмо"
        externalMailServer -> appServer "Подтверждение отправки"
        appServer -> ui "Подтверждение отправки сообщения"
    }

    views {
        dynamic emailSystem {
            title "Динамическая диаграмма отправки электронного письма"
            
            // Определяем участников динамической диаграммы
            user -> ui "Заполняет форму и отправляет сообщение"
            ui -> appServer "Отправляет данные формы"
            appServer -> database "Сохраняет сообщение в базе данных"
            appServer -> externalMailServer "Отправляет электронное письмо"
            externalMailServer -> appServer "Подтверждение отправки"
            appServer -> ui "Подтверждение отправки сообщения"
            
            autolayout lr
        }

        theme default
    }
}
