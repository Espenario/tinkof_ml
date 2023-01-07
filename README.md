# tinkoff_ml
## Запуск программы
Пример запуска: `python3 compare.py input.txt scores.txt`

По умолчанию получает данные из файла `input.txt`, а результат выводит в файл `scores.txt`
## Работа программы
1. Проверка данных
    1. Проверка количества введенных файлов (если их меньше 2, программа завершается с указанием строки в файле с входными данными, где не хватает данных).
    2. Проверка типа файла. Так как во время предобработки будет использоваться библиотека ast, то при обнаружении не `python` файла во входных данных будет выведено диалоговое окно, где можно будет остановить выполнение программы.
2. Предобработка данных.
  Сравнение на антиплагиат будет производиться с помощью расстояния Левенштейна, поэтому были сделаны следующие изменения в исходных данных.
    1. Унифицированны имена переменных, аргументов функций, функций и классов. Так как расстояния Левенштейна смотрит только на символы, то абсолютно одинаковые по смыслу программы с разными именами переменных могут иметь высокий коэффициент оригинальности.
    2. Удалены комментарии. 
3. Вычисление расстояние Левенштейна. 
  С помощью алгоритма [Вагнера-Фишера](https://en.wikipedia.org/wiki/Wagner–Fischer_algorithm) заполняем матрицу D. Итовым расстоянием будет являться нижняя правая ячейка получившейся матрицы. Для нормировки значения полученное расстояние делится на среднее значение длинны текста.
