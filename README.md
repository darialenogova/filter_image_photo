# Проект "Помощь фотографу"

## Описание проекта
Данный проект создан для помощи фотографам в применении фильтров для фотографии. 

## Цели проекта
- Применять фильтры к фотографиям

## Используемые технологии
- Python для создания программы для обработки фотографий.

## Установка зависимостей
Загрузите на компьютер необходимые файлы, затем используйте `pip` для установки зависимостей и установить зависимости. Зависимости можно установить командой, представленной ниже.
Установите зависимости командой:
```
pip install -r requirements.txt
```

## Пример запуска
Для запуска скрипта у вас уже должен быть установлен Python3.
Для получения сведений о обработке фотографий, необходимо записать:
```
python main.py --file_name "image/photo_1.jpg"
```
Фильтры вызываются отдельно:
- `--bw_photo`: добавляет черно-белый фильтр
- `--contrast_photo`: добавляет контрастный фильтр фильтр
- `--blur_photo`: добавляет фильтр размытия
- `--noise_photo`: добавляет медианный фильтр
- `--border_photo`: добавляет рамку
- `--sepia_photo`: добавляет фильтр сепии

Пример использования программы:
```
python main.py --bw_photo --contrast_photo --file_name "image/photo_1.jpg"
```
Выведет сведения о чёрно-белом фильтре и о контрастном фильтре

Проект выполнен в образовательных целях на онлайн-курсе "Основы Python" школы "Лидер".
