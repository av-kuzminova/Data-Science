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
            // Технология для внешнего почтового сервера не указывается
        }

        // Определение взаимодействий
        user -> ui "Использует"
        ui -> appServer "Отправляет запросы"
        appServer -> database "Сохраняет и извлекает данные"
        appServer -> externalMailServer "Отправляет и получает письма"
    }

    views {
        systemContext emailSystem {
            include user
            include externalMailServer
            autolayout lr
        }

        container emailSystem {
            include ui
            include appServer
            include database
            autolayout lr
        }

        theme default
    }
}
