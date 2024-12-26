import pkg_resources

# Получаем все установленные библиотеки и их версии
installed_packages = pkg_resources.working_set

# Выводим их
for package in installed_packages:
    print(f"{package.key}=={package.version}")