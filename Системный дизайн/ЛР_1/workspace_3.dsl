workspace {

    model {
        user = person "Пользователь" {
            description "Пользователь системы электронной почты."
        }

        emailSystem = softwareSystem "Приложение электронной почты (Outlook)" {
            description "Система для управления электронной почтой."
        }

        externalMailServer = softwareSystem "Внешний почтовый сервер" {
            description "Система для отправки и получения электронной почты."
        }

        user -> emailSystem "Читает и отправляет электронные письма"
        emailSystem -> externalMailServer "Отправляет и получает письма"
    }

    views {
        systemContext emailSystem {
            include user
            include externalMailServer
            autolayout lr
        }

        theme default
    }
}
