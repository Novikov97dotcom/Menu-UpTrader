# Django Tree Menu

[English](#english) | [Русский](#russian)

<a name="english"></a>
## English

A Django application that implements a tree-like menu system with the following features:

### Features
- Multiple menus on one page (identified by name)
- Unlimited nesting levels
- Active item detection based on current URL
- Support for both explicit URLs and named URLs
- Single database query per menu rendering
- Standard Django admin interface for management
- Easy template integration: `{% draw_menu 'main_menu' %}`

### Requirements
- Python 3.8+
- Django 3.2+

### Installation
1. Clone the repository or copy the `menu` directory to your project
2. Add `'menu'` to `INSTALLED_APPS` in `settings.py`:
    ```python
    INSTALLED_APPS = [
        # ...
        'menu',
    ]
    ```
3. Run migrations:
    ```bash
    python manage.py makemigrations menu
    python manage.py migrate
    ```
4. Create a superuser (if needed):
    ```bash
    python manage.py createsuperuser
    ```

### Usage
1. Create menu items in Django admin:
   - Set Menu Name (e.g., 'main_menu', 'footer_menu')
   - Set Name (display text)
   - Set URL or Named URL (one of them)
   - Set Parent for nesting
   - Set Order for sorting

2. Add menu to your template:
    ```django
    {% load menu_tags %}
    {% draw_menu 'main_menu' %}
    ```

3. Multiple menus on one page:
    ```django
    {% draw_menu 'main_menu' %}
    {% draw_menu 'footer_menu' %}
    ```

### Menu Behavior
- Active item is determined by current URL
- All ancestors of active item are expanded
- First level of children under active item is expanded

### Example Menu Structure
```
main_menu
├── Home (/)
├── About (/about/)
├── Services
│   ├── Development (/services/dev/)
│   └── Design (/services/design/)
└── Contact (/contacts/)
```

### Code Quality
- PEP8 compliant
- Type hints
- Single database query per menu
- No external dependencies

### License
MIT

---

<a name="russian"></a>
## Русский

Django-приложение, реализующее древовидное меню со следующими возможностями:

### Возможности
- Несколько меню на одной странице (определяются по названию)
- Неограниченная вложенность
- Определение активного пункта по текущему URL
- Поддержка как явных, так и именованных URL
- Один SQL-запрос на отрисовку каждого меню
- Стандартный интерфейс админки Django для управления
- Простая интеграция в шаблоны: `{% draw_menu 'main_menu' %}`

### Требования
- Python 3.8+
- Django 3.2+

### Установка
1. Склонируйте репозиторий или скопируйте директорию `menu` в ваш проект
2. Добавьте `'menu'` в `INSTALLED_APPS` в `settings.py`:
    ```python
    INSTALLED_APPS = [
        # ...
        'menu',
    ]
    ```
3. Выполните миграции:
    ```bash
    python manage.py makemigrations menu
    python manage.py migrate
    ```
4. Создайте суперпользователя (если нужно):
    ```bash
    python manage.py createsuperuser
    ```

### Использование
1. Создайте пункты меню в админке Django:
   - Укажите Menu Name (например, 'main_menu', 'footer_menu')
   - Укажите Name (отображаемый текст)
   - Укажите URL или Named URL (одно из двух)
   - Укажите Parent для вложенности
   - Укажите Order для сортировки

2. Добавьте меню в шаблон:
    ```django
    {% load menu_tags %}
    {% draw_menu 'main_menu' %}
    ```

3. Несколько меню на одной странице:
    ```django
    {% draw_menu 'main_menu' %}
    {% draw_menu 'footer_menu' %}
    ```

### Поведение меню
- Активный пункт определяется по текущему URL
- Все предки активного пункта раскрыты
- Первый уровень вложенности под активным пунктом раскрыт

### Пример структуры меню
```
main_menu
├── Главная (/)
├── О нас (/about/)
├── Услуги
│   ├── Разработка (/services/dev/)
│   └── Дизайн (/services/design/)
└── Контакты (/contacts/)
```

### Качество кода
- Соответствие PEP8
- Типизация
- Один SQL-запрос на меню
- Без внешних зависимостей

### Лицензия
MIT 