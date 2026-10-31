# FireWatch AI — проектная документация

A Planet on Fire: Why Forest Fires Are a Wake-Up Call for Renewable Energy

Seeing the Monroe Canyon Fire in a New Light - NASA Science

RiskLabs: Next Generation Wildfire Intelligence

FireWatch AI — полноценная геоинформационная платформа для мониторинга активных пожаров, анализа экологических рисков и изучения исторической пожарной активности на основе спутниковых данных NASA.

Срок разработки

# 8–12 недель

Формат

# Web platform

Научная основа

## NASA FIRMS

Основная технология

## GeoAI + GIS

Главная идея: не просто показать точки пожаров на карте, а объединить спутниковые наблюдения, временной анализ, погодные факторы, обнаружение аномалий и объяснимую оценку риска в одной системе.

Важное научное ограничение: NASA FIRMS обнаруживает тепловые аномалии и активные очаги по спутниковым наблюдениям. Это не гарантирует обнаружение каждого пожара и само по себе не даёт достоверного прогноза того, куда распространится огонь. Поэтому FireWatch AI будет разделять наблюдаемые факты, статистические оценки риска и прогнозные модели.

## 1. Что именно мы создаём

Платформа будет состоять из шести крупных подсистем.

Data Overview - NASA Science

01. Live Fire Map

Интерактивная карта активных термических аномалий. Фильтры по региону, дате, спутнику, доверительному уровню обнаружения и типу данных. Кластеризация точек при большом масштабе данных.

SciFire Alerts Version 2.0: Scaling Predictive Protection in the Western Ghats — Scigram

02. Fire Intelligence

Анализ активности пожаров по дням, неделям, месяцам и сезонам. Сравнение регионов, поиск необычных всплесков, динамика за несколько лет.

GIS-Based Frequency Ratio and Analytic Hierarchy Process for Forest Fire Susceptibility Mapping in the Western Region of Syria

03. Risk Engine

Расчёт индекса риска на основе погоды, истории возгораний, сезонности и доступных показателей сухости растительности. Отдельная карта риска с описанием факторов, повлиявших на оценку.

Wildfire Experts

04. Anomaly Detection

Поиск необычных скоплений очагов и скачков активности относительно исторического фона. Выявление зон, которые требуют дополнительной проверки.

TelePIX | Extracting Insights from Space

05. AI Research Assistant

Вопросы на естественном языке, сводки по выбранной области, объяснение графиков и автоматическое формирование отчётов с источниками данных.

Esri Recognizes Partners for Extending the Reach of GIS in Innovative Ways | Summer 2025 | ArcNews

06. Alerts & Reports

Пользовательские географические зоны, уведомления о новых обнаружениях, пороговые правила, экспорт CSV/GeoJSON и отчётов PDF.

## 2. Реальные API и источники данных

Я бы строил систему на официальных открытых научных данных, а не на случайных наборах из Kaggle. Основой будут четыре источника с разными задачами.

1. NASA FIRMS — главный источник обнаружений

ОбязательныйОфициальный сервис: [FIRMS](<https://firms.modaps.eosdis.nasa.gov/?utm_source=chatgpt.com>) · [API documentation](<https://firms.modaps.eosdis.nasa.gov/api/?utm_source=chatgpt.com>)

Предоставляет обнаружения активных термических аномалий с приборов MODIS и VIIRS, включая координаты, время наблюдения, показатели качества и другие характеристики набора данных. Глобальные NRT-данные обычно поступают в течение примерно трёх часов после спутникового наблюдения, но задержка зависит от продукта и региона.

FIRMS

+1

Для запросов через API понадобится бесплатный `MAP_KEY`. Зарегистрируй ключ заранее: [Получить FIRMS MAP\_KEY](<https://firms.modaps.eosdis.nasa.gov/api/map_key/?utm_source=chatgpt.com>). Указанный NASA лимит — 5000 транзакций за 10 минут; крупные запросы могут учитываться как несколько транзакций.

FIRMS

Что реализовать: загрузку данных за последние сутки, 7 дней и выбранный период, фильтрацию по области, нормализацию данных и сохранение в PostgreSQL.

2. NASA EONET — каталог природных событий

[EONET API v3 documentation](<https://eonet.gsfc.nasa.gov/docs/v3?utm_source=chatgpt.com>)

Содержит метаданные о природных событиях, в том числе лесных пожарах, с категориями, датами, координатами и ссылками на связанные материалы.

Welcome

+1

Что реализовать: дополнительную ленту событий, карточки подтверждённых источником событий и сопоставление с близлежащими обнаружениями FIRMS. Не считать две записи одним пожаром автоматически только потому, что они находятся рядом.

3. NASA POWER — метеорологический контекст

[NASA POWER API documentation](<https://power.larc.nasa.gov/docs/services/api/?utm_source=chatgpt.com>)

Предоставляет метеорологические и солнечные данные, включая временные ряды температуры, осадков и скорости ветра в зависимости от выбранного продукта. Метеорологические данные имеют пространственное разрешение порядка 0,5° × 0,625°, поэтому не подходят для оценки условий на уровне отдельного дерева или небольшого участка.

Docs

+1

Что реализовать: сопоставление пожарной активности с температурой, осадками, ветром и историческими климатическими условиями. Эти данные полезны для анализа факторов риска, но не являются полноценным локальным прогнозом погоды.

4. NASA GIBS / Worldview — спутниковые изображения

[GIBS](<https://www.earthdata.nasa.gov/data/tools/gibs?utm_source=chatgpt.com>) · [Worldview](<https://worldview.earthdata.nasa.gov/?utm_source=chatgpt.com>)

Позволяет отображать спутниковые растровые слои и визуально сопоставлять очаги с изображениями Земли. GIBS предназначен именно для быстрого просмотра геопространственных изображений.

NASA Open Data Portal

+1

Что реализовать: переключаемые слои, выбор даты изображения и прозрачность наложения. Изображения могут иметь другую дату наблюдения, чем очаги FIRMS, поэтому интерфейс должен показывать временную метку каждого слоя.

### Дополнительный источник для продвинутой версии

Можно добавить спутниковые показатели растительности, например NDVI, и оценивать их сезонные изменения. Это поможет исследовать связь между растительностью и пожарной активностью. Но для первого релиза не стоит строить сложную обработку спутниковых снимков с нуля: достаточно подключить готовые слои, а полноценную обработку растров добавить как отдельный модуль.

## 3. Архитектура платформы

Рекомендую модульный backend с отдельными процессами фоновой обработки данных. Для университетского проекта это проще поддерживать, чем десятки микросервисов, но при этом архитектура остаётся расширяемой.

### Frontend — Next.js + TypeScript

Карта · Аналитика · Риск · ИИ-чат · Оповещения · Отчёты

### Backend API — FastAPI

Авторизация · Валидация · Геозапросы · Аналитика · Отчёты

PostgreSQL + PostGIS

Очаги, зоны, история, пользователи

ML Engine

Риск, аномалии, объяснения

Worker

Сбор, обработка и расписание

Report Engine

CSV, GeoJSON, PDF

### Внешние источники

NASA FIRMS · NASA EONET · NASA POWER · NASA GIBS

### Рекомендуемый стек технологий

| Слой | Технология | Задача |
| --- | --- | --- |
| Frontend | Next.js, React, TypeScript | Интерфейс платформы |
| Дизайн | Tailwind CSS, shadcn/ui | Адаптивный интерфейс |
| Карта | MapLibre GL JS | Карта, слои, географические фильтры |
| Графики | Apache ECharts | Временные ряды и аналитика |
| Backend | Python, FastAPI, Pydantic | API и бизнес-логика |
| База данных | PostgreSQL, PostGIS | Геоданные и пространственные запросы |
| Миграции | Alembic | Версионирование схемы БД |
| Очереди | Redis + Celery | Фоновая загрузка и расчёты |
| Научная обработка | Pandas, NumPy, scikit-learn | Аналитика и машинное обучение |
| Тесты | Pytest, Vitest, Playwright | Проверка backend, frontend и сценариев |
| Контейнеризация | Docker Compose | Воспроизводимый запуск |
| Документация API | OpenAPI / Swagger | Интерактивная документация |

На первом этапе не нужны Kubernetes, сложная облачная инфраструктура или платные картографические сервисы. Лучше потратить время на корректность данных, аналитику и работающий интерфейс.

### Как должна проходить обработка данных

1. Worker по расписанию запрашивает новые записи NASA FIRMS.
2. Backend проверяет формат, координаты, дату и идентификаторы источника.
3. Данные преобразуются в единую внутреннюю модель.
4. Новые записи сохраняются, а повторные не создают дубликаты.
5. Обновляются агрегаты по регионам и временным интервалам.
6. Рассчитываются статистические показатели и аномалии.
7. Система проверяет пользовательские правила оповещений.
8. Frontend получает свежие данные через API.

Если NASA API временно недоступен, приложение продолжает показывать последнее успешно загруженное состояние с отметкой времени обновления. Оно не должно выдавать устаревшие данные за актуальные.

## 4. Структура базы данных

Используем PostgreSQL с расширением PostGIS. Это позволит хранить не только записи о пожарах, но и географические зоны, выполнять поиск в радиусе и пересечения с регионами.

Предлагаемая схема данных для первой полноценной версии

### fire\_detections

Основная таблица спутниковых обнаружений

id · source · source\_record\_id · satellite · instrument · observed\_at · latitude · longitude · brightness\_temperature · confidence · frp · geometry · raw\_payload

### regions

id · name · region\_type · geometry · country\_code · created\_at

Границы стран, областей и пользовательских зон.

### weather\_observations

id · latitude · longitude · observed\_at · temperature · precipitation · wind\_speed · relative\_humidity · source

Метеорологические значения и происхождение данных.

### risk\_assessments

id · region\_id · assessed\_at · horizon · risk\_score · risk\_class · model\_version · feature\_snapshot · explanation

Оценки риска с версией модели и использованными факторами.

### anomalies

id · region\_id · detected\_at · anomaly\_type · severity · baseline\_value · observed\_value · method · status

### users / watch\_zones / alert\_rules / notifications

Пользователи, подписки на географические зоны, правила уведомлений и журнал отправки.

### data\_ingestion\_runs / audit\_logs

Статус импорта, количество загруженных записей, ошибки, время последнего успешного обновления и аудит важных действий.

### Важные решения по хранению

- Уникальность обнаружений обеспечивать ключом, основанным на источнике и идентификаторе записи, если он доступен; иначе — документированным составным ключом с учётом специфики набора.
- Хранить исходное время наблюдения в UTC, не путать его со временем загрузки.
- Создать пространственный индекс GiST по `geometry` и B-tree индексы по времени, источнику и спутнику.
- Для большого объёма данных предусмотреть партиционирование по времени, но включать его только при необходимости.
- Сохранять происхождение, единицы измерения и исходные значения. Например, FRP — это мощность теплового излучения пожара, а не площадь выгоревшей территории.
- Не смешивать измеренные значения, вычисленные показатели и прогнозы в одних полях.

### Пример API платформы

| Endpoint | Назначение |
| --- | --- |
| `GET /api/v1/fires` | Получить обнаружения с фильтрами |
| `GET /api/v1/fires/{id}` | Подробности обнаружения |
| `GET /api/v1/analytics/timeseries` | Динамика активности |
| `GET /api/v1/analytics/regions` | Сравнение регионов |
| `GET /api/v1/risk/map` | Сетка оценок риска |
| `GET /api/v1/anomalies` | Найденные аномалии |
| `GET /api/v1/weather` | Погодный контекст |
| `GET /api/v1/events` | Природные события EONET |
| `POST /api/v1/watch-zones` | Создать зону наблюдения |
| `GET /api/v1/alerts` | Список уведомлений |
| `POST /api/v1/reports` | Сформировать отчёт |
| `POST /api/v1/assistant/query` | Запрос к ИИ-ассистенту |
| `GET /api/v1/system/data-status` | Состояние источников и обновлений |

Все endpoints должны иметь схемы запросов и ответов, пагинацию, ограничения диапазонов и единый формат ошибок.

## 5. Научная и ИИ-часть

Это самая важная часть проекта. Именно здесь FireWatch AI перестаёт быть обычной картой с данными и становится исследовательской платформой.

Я рекомендую сделать три независимых аналитических механизма вместо одной «магической нейросети».

### Модуль A. Обнаружение аномалий

Задача — определить, когда количество или интенсивность обнаружений в районе необычно высоки по сравнению с историческим фоном.

Входные данные:

- количество обнаружений в географической ячейке за временной интервал;
- число наблюдений по предыдущим периодам;
- сезон и день недели, если это обосновано данными;
- исторические значения FRP, если они доступны и сопоставимы;
- качество и полнота спутниковых наблюдений, если такие сведения доступны.

Алгоритм: сначала сезонный статистический baseline, затем Isolation Forest как дополнительный метод.

Для базовой модели можно рассчитать робастную стандартизованную оценку:

$$
z_{\mathrm{robust}} =
\frac{x_t-\operatorname{median}(X)}
{1.4826\cdot\operatorname{MAD}(X)+\epsilon}
$$

Здесь $x_t$ — текущая активность, $X$ — сопоставимая историческая выборка, MAD — медианное абсолютное отклонение, а $\epsilon$ предотвращает деление на ноль.

Важное условие: сравнивать нужно с историей для сопоставимого сезона и временного окна. Для редких событий или почти нулевого MAD потребуется отдельная обработка.

Результат:

- оценка необычности;
- базовое ожидаемое значение;
- фактическое значение;
- объяснение, почему сработал детектор;
- версия алгоритма.

Аномалия означает «необычная активность», а не автоматически «новый опасный пожар».

### Модуль B. Оценка пожарного риска

Здесь необходимо разделить два понятия:

- Текущая пожарная активность — то, что наблюдают спутники.
- Риск будущего возгорания — вероятность будущего события при определённых условиях.

Нельзя обучить достоверный прогноз, просто передав в модель текущие точки пожаров и попросив предсказать следующую точку. Это создаст ложное впечатление научности.

Для университетской версии предлагаю следующую стратегию.

Этап 1. Прозрачный индекс риска

Составить индекс на основе исторической пожарной активности, температуры, осадков, ветра, влажности и сезонности. Каждый фактор нормализовать, документировать и проверить чувствительность результата к весам.

Этап 2. Обучаемая модель

При наличии достаточного набора исторических данных и корректных меток — обучить градиентный бустинг или логистическую регрессию для оценки вероятности обнаружения пожара в ячейке в будущем временном окне.

Этап 3. Проверка качества

Сравнить с простым baseline, оценить precision, recall, PR-AUC, калибровку вероятностей и качество на более позднем периоде, не использованном при обучении.

Для обучаемой модели нужна целевая переменная, например: «было ли хотя бы одно обнаружение пожара в данной ячейке в следующие 24 часа». Но это будет вероятность будущего спутникового обнаружения, а не доказанная вероятность возникновения пожара: на результат влияют пролёты спутников, облачность, качество данных и пропущенные события.

Если полноценной обучающей выборки не хватит, индекс риска должен оставаться индексом, а не выдаваться за обученную вероятность.

### Модуль C. Пространственно-временная аналитика

Для каждого региона и временного окна вычислять:

- число обнаружений;
- медиану и сумму FRP, если сравнение методологически корректно;
- изменение активности относительно baseline;
- плотность обнаружений на единицу площади;
- число активных дней;
- повторяемость активности в ячейках;
- долю данных с пропущенными или сомнительными значениями.

Для карты использовать географическую сетку, например H3 с выбираемым разрешением. При сравнении регионов нужно учитывать их площадь и доступность наблюдений.

### Как оценивать результат модели

Нельзя случайным образом перемешивать соседние точки и разделять их на train/test: модель может запомнить географические особенности и показать искусственно хорошее качество.

Используй временное разделение:

- Train — ранние периоды.
- Validation — более поздний период для выбора модели.
- Test — самый поздний период, не используемый для подбора.

Для редких событий accuracy почти бесполезна: модель, которая всегда предсказывает отсутствие пожара, может показать высокий процент правильных ответов. Лучше использовать PR-AUC, recall, precision, Brier score и калибровочные графики — в зависимости от задачи.

## 6. Дизайн и структура интерфейса

Предлагаю тёмный научный интерфейс, напоминающий геоинформационную систему центра мониторинга.

UI Design Daily | Nasa Worldview

Dashboard

Главная страница: количество обнаружений за выбранный период, статус данных, активные аномалии, мини-график активности и карта последних событий.

Live Map

Основной рабочий экран. Слева фильтры и слои, по центру карта, справа панель выбранного обнаружения. Обязательно легенда, масштаб и время наблюдения.

OBSERVER: Exploring wildfire emissions with CAMS Fire Emissions Watch | EU Space Support Office | EU Space Policy

Analytics Lab

Сравнение временных периодов, графики, тепловая карта активности, выбор регионов и экспорт результатов.

RiskLabs: Next Generation Wildfire Intelligence

Risk Explorer

Карта оценки риска с выбором горизонта, деталями факторов и предупреждением об ограничениях модели. Цвета не должны заменять численные значения и легенду.

TerraLens: See Your Planet. Shape Its Future. 🌍 - DEV Community

AI Research Assistant

Чат с историей диалога, ссылками на используемые данные, временными интервалами и контекстом выбранного региона.

Не нужно делать каждый экран отдельным красивым макетом без связи с сервером. Все карточки, графики, фильтры и показатели должны работать на реальных API и состоянии приложения.

## 7. ИИ-ассистент: как сделать его действительно полезным

Не стоит обучать собственную большую языковую модель за время университетского проекта. Лучше сделать инструментальный ИИ-ассистент, который использует реальные функции backend.

Примеры запросов пользователя:

- «Сравни активность пожаров в Чуйской области за последние 7 дней и за аналогичный период прошлого года».
- «Покажи ячейки, где количество обнаружений необычно высокое».
- «Какие погодные факторы совпадали с высокой пожарной активностью в выбранном регионе?»
- «Создай отчёт по обнаружениям в радиусе 50 км от выбранной точки».

Архитектура ответа:

1. Ассистент распознаёт задачу и необходимые параметры.
2. Backend выполняет разрешённые аналитические функции с валидацией входных данных.
3. Результаты вычислений передаются модели.
4. Модель формирует объяснение и ссылки на источники.
5. Интерфейс отображает ответ, график или таблицу.

ИИ не должен иметь прямого доступа к произвольному SQL, секретам или возможности выполнять команды на сервере. Для начала достаточно трёх-четырёх инструментов: `get_fire_statistics`, `get_regional_anomalies`, `compare_periods` и `create_report`.

Если ключ к платной языковой модели недоступен, приложение должно продолжать работать: аналитика, карты и отчёты не должны зависеть от ИИ-чата.

## 8. План разработки на 12 недель

Это реалистичный план для одного разработчика, активно использующего ИИ-программиста. Основной риск — не написание кода, а интеграция API, качество данных и проверка аналитики.

### Неделя 1 — фундамент

Этап 1

- Утвердить область MVP и архитектуру.
- Получить FIRMS MAP\_KEY и проверить реальные ответы API.
- Создать репозиторий, Docker Compose и конфигурацию окружения.
- Поднять frontend, FastAPI и PostgreSQL/PostGIS.
- Настроить миграции, health checks и базовые тесты.

Результат: проект запускается локально одной командой.

### Недели 2–3 — сбор данных и карта

Этап 2

- Реализовать FIRMS ingestion worker.
- Нормализовать и сохранять обнаружения.
- Добавить обработку дубликатов, таймаутов и повторных запросов.
- Сделать API карты, фильтры, кластеризацию и карточку обнаружения.
- Показать время последнего успешного обновления.

Результат: карта отображает настоящие спутниковые обнаружения.

### Недели 4–5 — аналитика

Этап 3

- Подключить EONET и NASA POWER.
- Реализовать временные ряды и сравнение периодов.
- Добавить географические агрегаты.
- Реализовать baseline и детектор аномалий.
- Добавить выгрузку CSV и GeoJSON.

Результат: система не только показывает точки, но и анализирует их.

### Недели 6–7 — оценка риска

Этап 4

- Подготовить обучающие признаки и временные метки.
- Определить целевое событие и горизонт прогноза.
- Сравнить простой baseline с ML-моделью, если данные позволяют.
- Провести временную валидацию.
- Создать Risk Explorer с объяснениями факторов.

Результат: воспроизводимая модель или документированный индекс риска.

### Недели 8–9 — ИИ и уведомления

Этап 5

- Реализовать регистрацию и авторизацию.
- Добавить пользовательские зоны наблюдения.
- Реализовать правила уведомлений и журнал отправки.
- Подключить ИИ-ассистента к ограниченному набору инструментов.
- Добавить ссылки на данные, ограничения и контекст ответов.

Результат: персонализированная платформа для исследования региона.

### Недели 10–11 — качество и развёртывание

Этап 6

- Интеграционные и end-to-end тесты.
- Проверка нагрузки на карту и запросы к БД.
- Обработка недоступных внешних API.
- Проверка авторизации, секретов и пользовательских данных.
- Развёртывание на доступном хостинге, HTTPS и резервное копирование.

Результат: доступная демонстрационная версия с понятной процедурой запуска.

### Неделя 12 — защита

Этап 7

- Подготовить презентацию архитектуры и ER-диаграмму.
- Сформировать отчёт о качестве модели.
- Подготовить демонстрацию с заранее проверенным регионом и периодом.
- Описать ограничения, источники и направления развития.
- Проверить установку проекта на чистом окружении.

Результат: воспроизводимый проект, научное обоснование и готовая демонстрация.

### Что обязательно должно попасть в MVP

Даже если времени окажется меньше 12 недель, необходимо сохранить работающие:

- карту с реальными данными NASA;
- фильтры по времени и области;
- страницу аналитики;
- один объяснимый алгоритм обнаружения аномалий;
- статус источников данных;
- тесты и документацию запуска.

ML-прогноз, сложный ИИ-ассистент и дополнительные источники можно реализовывать после этого. Не жертвуй рабочей базовой версией ради большого числа недоделанных функций.

## 9. Тестирование и критерии готовности

| Тип проверки | Что проверять | Критерий |
| --- | --- | --- |
| Unit-тесты | Нормализация и расчёты | Все ключевые граничные случаи проверены |
| API-тесты | Фильтры, пагинация, ошибки | Корректные ответы и коды ошибок |
| Интеграция | NASA API → worker → БД | Данные проходят весь путь без потерь |
| Геотесты | Поиск в радиусе и bbox | Проверенные координаты и границы |
| Дедупликация | Повторный импорт | Нет повторного создания той же записи |
| ML-тесты | Временная валидация | Нет утечки будущих данных |
| E2E | Основной пользовательский сценарий | Все критические шаги выполняются |
| Безопасность | Авторизация и секреты | Нет доступа к чужим зонам и ключам |
| Отказоустойчивость | Недоступность NASA API | Ошибка видна, приложение не падает |
| Производительность | Карта и фильтры | Время ответа измерено и задокументировано |

Для защиты полезно поставить измеримые цели, например: успешный импорт тестового набора без дубликатов, покрытие критической бизнес-логики тестами не менее 80%, корректная работа основных пользовательских сценариев и отчёт о качестве модели на отложенном периоде.

Это целевые критерии, а не уже достигнутые результаты. После разработки их необходимо проверить и зафиксировать фактические значения.

## 10. Единый подробный промпт для ИИ-программиста

Этот промпт можно передать ИИ, работающему с репозиторием: например, coding agent в IDE. Лучше попросить его сначала исследовать проект и создать план, а затем реализовывать этапы последовательно. Попытка сгенерировать всю платформу за один проход часто приводит к неработающим интеграциям и заглушкам вместо реальных функций.

Написание текста

# FIREWATCH AI — MASTER ENGINEERING SPECIFICATION

## 1\. Role and objective

Act as a senior full-stack engineer, geospatial software engineer, data engineer, applied machine-learning engineer, QA engineer, and technical writer.

Build a production-quality university research platform named **FireWatch AI** for wildfire activity monitoring, spatiotemporal analytics, anomaly detection, risk assessment, and scientific reporting using real NASA data.

The project must be runnable, testable, documented, and demonstrable. Do not create only a static landing page, mock dashboard, UI prototype, or collection of disconnected screens.

Work directly in the existing repository. Inspect the repository before making changes. Preserve working functionality and report any existing limitations.

The expected development window is 8–12 weeks for a solo university developer assisted by AI coding tools. Prioritize a reliable end-to-end core before adding advanced features.

## 2\. Non-negotiable requirements

1. Use real NASA data in the operational application.
2. Never fabricate observations, API responses, model metrics, sources, or successful imports.
3. Never present mock data as live NASA data.
4. Clearly distinguish observed satellite detections, derived statistics, anomaly scores, heuristic risk indices, and calibrated predictive probabilities.
5. Display the observation timestamp, data source, freshness, and relevant limitations.
6. Keep secrets and provider credentials on the server.
7. Provide graceful degradation when external APIs are unavailable.
8. Every primary UI control must perform its advertised action.
9. Provide migrations, automated tests, seed/demo instructions, and reproducible setup.
10. Do not claim a model is scientifically validated until evaluation has actually been performed.
11. Do not promise operational fire warnings or emergency response accuracy.
12. Use accessible, responsive UI design and clear loading, empty, and error states.

## 3\. Technology stack

Frontend:

- Next.js with App Router
- React and TypeScript in strict mode
- Tailwind CSS
- shadcn/ui or equivalent accessible components
- MapLibre GL JS for interactive geospatial maps
- Apache ECharts for charts
- TanStack Query for API data fetching and caching
- Zod for client-side validation

Backend:

- Python 3.12 or another supported stable Python version
- FastAPI
- Pydantic
- SQLAlchemy 2.x
- Alembic
- PostgreSQL with PostGIS
- Redis and Celery for scheduled/background jobs
- Pandas, NumPy, scikit-learn
- GeoJSON for geospatial interchange
- pytest, httpx and relevant test tooling

Operations:

- Docker Compose
- Separate frontend, API, worker, PostgreSQL/PostGIS and Redis services
- Environment-based configuration
- Structured logs and health checks
- GitHub Actions or an equivalent CI pipeline
- OpenAPI documentation

Pin compatible dependency versions and document them. Avoid adding libraries that are not needed.

## 4\. Official data sources

### NASA FIRMS

Official documentation: https://firms.modaps.eosdis.nasa.gov/api/

API key registration: https://firms.modaps.eosdis.nasa.gov/api/map\_key/

Implement a backend-only FIRMS connector. The API key must be supplied through FIRMS\_MAP\_KEY and must never be exposed to the browser.

Requirements:

- Support the selected MODIS/VIIRS products documented by FIRMS.
- Support area, time range and sensor/product filters where the endpoint allows them.
- Normalize source records into a canonical internal detection model.
- Preserve source identifiers, sensor, acquisition timestamp, confidence fields, FRP where provided, coordinates and original attributes.
- Validate geographic coordinates and timestamp formats.
- Handle rate limits, timeouts, retries with backoff, and provider errors.
- Make ingestion idempotent.
- Track import runs, source freshness, record counts and errors.
- Respect endpoint-specific limits and use bounded queries.
- Never infer missing confidence or FRP values.
- Preserve the distinction between observation time and ingestion time.

Read the actual official documentation before implementing endpoint paths and query parameters. Do not guess API response fields.

### NASA EONET

Official documentation: https://eonet.gsfc.nasa.gov/docs/v3

Implement a connector for natural-event metadata, including wildfire-related events where available.

Requirements:

- Fetch event metadata and associated dates and geometries.
- Store the source event ID, title, categories, source URL, event status and coordinates.
- Allow event filtering by category and time.
- Provide provenance for each event.
- Do not assume that an EONET event and a nearby FIRMS detection represent the same physical incident without a documented matching procedure.

### NASA POWER

Official documentation: https://power.larc.nasa.gov/docs/services/api/

Implement a configurable meteorological data connector.

Requirements:

- Request supported meteorological variables at the correct spatial and temporal resolution.
- Store units, coordinates, observation period, source and retrieval time.
- Cache repeated requests.
- Avoid excessive parallel requests.
- Handle missing values and distinguish unavailable data from measured zero.
- Use meteorological variables as contextual features, not proof of causation.
- Document the limitations of gridded weather data.

### NASA GIBS / Worldview

GIBS: https://www.earthdata.nasa.gov/data/tools/gibs

Worldview: https://worldview.earthdata.nasa.gov/

Add optional satellite imagery layers using supported service endpoints and layer definitions.

Requirements:

- Verify the selected layer and imagery date.
- Keep imagery dates distinct from fire detection timestamps.
- Provide attribution and a layer legend.
- Avoid assuming that every image layer uses the same projection, time availability or resolution.
- If imagery configuration is not yet validated, disable the layer with an explicit explanation instead of displaying a broken map.

## 5\. System architecture

Implement a modular monolith with separate background worker processes.

Core components:

1. Next.js frontend.
2. FastAPI REST backend under /api/v1.
3. PostgreSQL/PostGIS database.
4. Redis/Celery worker for ingestion and scheduled analysis.
5. Analytics and anomaly-detection module.
6. Optional predictive-risk module.
7. Report-generation module.
8. AI assistant service with controlled tool access.
9. Authentication and user-specific watch zones.
10. Logging, health checks and ingestion status.

Avoid unnecessary microservices and infrastructure.

The backend must remain the authoritative source for analytical calculations and access control.

## 6\. Database schema

Create migrations and SQLAlchemy models for at least:

- users
- fire\_detections
- regions
- weather\_observations
- natural\_events
- risk\_assessments
- anomalies
- watch\_zones
- alert\_rules
- notifications
- data\_ingestion\_runs
- audit\_logs

Important fields:

fire\_detections:

- internal UUID
- source
- source\_record\_id where available
- satellite and instrument
- observed\_at in UTC
- ingested\_at in UTC
- latitude and longitude
- PostGIS geometry
- confidence and confidence category where supplied
- brightness temperature where supplied
- FRP where supplied
- source metadata
- raw payload or a controlled raw-data reference

weather\_observations:

- coordinates or spatial cell
- observed\_at
- variable values
- units
- source
- retrieved\_at
- data quality metadata

risk\_assessments:

- region or spatial cell
- assessed\_at
- prediction/assessment horizon
- score
- score type
- risk class
- model version
- feature snapshot
- explanation
- evaluation metadata where applicable

anomalies:

- region or spatial cell
- detection timestamp
- anomaly method
- score
- baseline value
- observed value
- severity
- explanation
- status

Add:

- Foreign keys and check constraints.
- Unique constraints for idempotent ingestion.
- GiST spatial indexes.
- B-tree indexes for common timestamp and filter queries.
- Explicit nullability and units.
- UTC timestamp handling.
- Safe handling of raw source data.
- A documented deduplication strategy.
- Database migrations and rollback guidance.

Do not partition tables prematurely unless justified by measured data volume.

## 7\. REST API

Implement and document:

GET /api/v1/health GET /api/v1/system/data-status GET /api/v1/fires GET /api/v1/fires/{id} GET /api/v1/events GET /api/v1/weather GET /api/v1/analytics/timeseries GET /api/v1/analytics/regions GET /api/v1/anomalies GET /api/v1/risk/map GET /api/v1/risk/regions/{id} GET /api/v1/watch-zones POST /api/v1/watch-zones PATCH /api/v1/watch-zones/{id} DELETE /api/v1/watch-zones/{id} GET /api/v1/alerts POST /api/v1/alert-rules POST /api/v1/reports POST /api/v1/assistant/query

Use appropriate HTTP methods, validation, pagination, bounded time ranges, consistent error schemas, and authentication where needed.

The fire endpoint must support geographic bounding boxes, time ranges, sensor filters and reasonable result limits. Use GeoJSON for spatial outputs where appropriate.

Never accept arbitrary SQL from clients.

## 8\. Frontend pages

Create the following functional pages:

### Dashboard

- Current imported detection count for a clearly defined period.
- Data freshness and provider health.
- Activity time series.
- Recent anomalies.
- Regional activity summaries.
- Links to detailed views.

### Live Fire Map

- Interactive map.
- Fire markers and clustering.
- Time range, source and sensor filters.
- Geographic bounding box queries.
- Detection details.
- Layer legend and source attribution.
- Loading, empty, error and stale-data states.

### Analytics Lab

- Daily and weekly time series.
- Regional comparison.
- Seasonal and historical analysis.
- Change relative to a defined baseline.
- Export CSV and GeoJSON.

### Risk Explorer

- Separate layer for risk assessments.
- Selectable assessment horizon.
- Explanation of contributing features.
- Model version and data timestamp.
- Legend and limitations.
- Do not label a heuristic score as probability.

### Anomaly Explorer

- Filterable anomaly table.
- Anomaly score and baseline comparison.
- Links to relevant map areas.
- A clear distinction between unusual activity and confirmed incidents.

### Events

- EONET natural-event catalog.
- Source links and event metadata.
- Filters by category, status and dates.

### AI Research Assistant

- Natural-language queries.
- Structured results and citations to source data.
- Relevant charts or tables when useful.
- Clear handling of unsupported questions.
- No invented measurement