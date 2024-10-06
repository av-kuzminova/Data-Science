workspace {

    model {
        user = person "Пользователь"
        emailSystem = softwareSystem "Система электронной почты" {
            user -> this "Отправка и получение писем"
        }
    }

    views {
        systemContext emailSystem {
            include user
            include emailSystem
            autolayout lr
        }

        theme default
    }
}
