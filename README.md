# Семинар 12 — задачи по NumPy и Pandas

Семь учебных проектов. В каждом проекте две вещи:

* модуль с заданием — функции с заглушкой `raise NotImplementedError("Implement me")` и докстрингом-условием;
* файл с тестами — `test_*.py`, который проверяет вашу реализацию.

Функции с пометкой «Дано — не трогайте» уже написаны — их менять не нужно.

## Структура

```
.
├── README.md
├── project01/
│   ├── pixel_filters.py         # задание
│   └── test_pixel_filters.py    # тесты
├── project02/
│   ├── game_of_life.py
│   └── test_game_of_life.py
├── project03/
│   ├── wrapped_stats.py
│   └── test_wrapped_stats.py
├── project04/
│   ├── league_table.py
│   └── test_league_table.py
├── project05/
│   ├── pixel_art.py
│   └── test_pixel_art.py
├── project06/
│   ├── sudoku.py
│   └── test_sudoku.py
└── project07/
    ├── nearest_neighbour.py
    └── test_nearest_neighbour.py
```

Тест импортирует модуль-сосед из той же папки (например, `test_pixel_filters.py` — `pixel_filters.py`),
поэтому запускать `pytest` нужно из корня репозитория или из папки проекта. Отдельный `conftest.py` не нужен:
`pytest` сам добавляет папку теста в `sys.path`.

## Что нужно установить

* Python 3.10+
* `numpy`, `pandas`, `pytest` — они перечислены в `requirements.txt`

```bash
python -m pip install -r requirements.txt
```

При желании — в виртуальном окружении:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Как запускать тесты

### Все проекты сразу (из корня репозитория)

```bash
pytest
```

или, если команда `pytest` не в PATH:

```bash
python -m pytest
```

### Один проект

По папке — запустятся оба файла проекта:

```bash
pytest project01
```

по конкретному файлу:

```bash
pytest project01/test_pixel_filters.py
```

### Один тест

```bash
pytest project01/test_pixel_filters.py::test_invert
```

### Из папки проекта

Можно зайти внутрь и запустить только этот проект:

```bash
cd project01
pytest
```

### Полезные флаги

| Флаг | Что делает |
| --- | --- |
| `-v` | подробный вывод: имя каждого теста |
| `-q` | краткий вывод |
| `-x` | остановиться на первой ошибке |
| `-k "blur"` | запустить только тесты, в имени которых есть `blur` |
| `--collect-only -q` | только список тестов, без запуска |

Пример: `pytest project05 -v -k ascii`

> Пока функции не реализованы, тесты падают с `NotImplementedError: Implement me` — это нормально.
> После каждой реализованной функции соответствующие тесты начинают проходить.

## Проекты

| Папка | Модуль | Тестов | Тема |
| --- | --- | --- | --- |
| `project01` | `pixel_filters.py` | 27 | «Фильтры»: `view` против копии, переполнение `uint8`, булевы маски, `np.where`/`np.count_nonzero`, `np.pad` и скользящие окна, `np.dstack` |
| `project02` | `game_of_life.py` | 13 | «Жизнь» Конвея: `np.pad` и скользящие окна, сложение сдвинутых копий, `np.where`, `np.array_equal` |
| `project03` | `wrapped_stats.py` | 9 | «Wrapped» на Pandas: `groupby(...).agg`, `value_counts`, `nlargest`, `dt`-аксессор, `to_numpy` |
| `project04` | `league_table.py` | 11 | «Таблица лиги» на Pandas: `pd.concat`, `rename`, `groupby`, производные колонки через `np.where`, `sort_values` |
| `project05` | `pixel_art.py` | 12 | «Пиксель-арт»: `reshape`, `.mean(axis=...)`, broadcasting через `[:, None, :]`, `argmin`, `np.unique(axis=0)` |
| `project06` | `sudoku.py` | 11 | «Судоку»: `reshape(3,3,3,3).swapaxes(1,2)`, broadcasting-сравнения, `np.argwhere`, рекурсия |
| `project07` | `nearest_neighbour.py` | 13 | «Ближайший сосед»: попарные расстояния через broadcasting, `argmin(axis=1)`, `np.random.default_rng` |

Всего — 96 тестов.
