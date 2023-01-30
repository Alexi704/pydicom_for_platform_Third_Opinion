[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=4000&width=440&lines=%D0%92%D1%85%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5+%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5++%D0%B2+%D0%B4%D0%B8%D1%80%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%B8+%60src%60.)](https://git.io/typing-svg)

Скрипт выполняет преобразования входных данных, используя модуль pydicom
([документация pydicom](https://pydicom.github.io/pydicom/stable)).

При запуске программы:</br>
:one: удаляется информация, хранящаяся в ключе `PatientName` (аномизируется файл)</br>
:two: используя информацию в ключах `StudyInstanceUID`, `SeriesInstanceUID`, `SOPInstanceUID` создается новая структура хранения файлов:</br>
* на первом уровне `StudyInstanceUID`</br>
* на втором уровне `SeriesInstanceUID`</br>
* имя файла задается значением `SOPInstanceUID` с расширением `.dcm`</br>
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&pause=4000&center=true&vCenter=true&width=480&lines=%D0%A2.%D0%BE.+%D0%BF%D1%83%D1%82%D1%8C+%D0%BA+%D0%BA%D0%B0%D0%B6%D0%B4%D0%BE%D0%BC%D1%83+%D1%84%D0%B0%D0%B9%D0%BB%D1%83+%D0%B2%D1%8B%D0%B3%D0%BB%D1%8F%D0%B4%D0%B8%D1%82+%D1%82%D0%B0%D0%BA%3A)](https://git.io/typing-svg)</br>
:point_right:`$StudyInstanceUID/$SeriesInstanceUID/$SOPInstanceUID.dcm`:point_left:</br>

:three: Создается файл `list_of_matching_paths.txt`, в котором имена файлов исходной структуры сопоставлены к путям (именам) файлов в конечной структуре.</br>

:heavy_exclamation_mark: В случае отсутствия ключей `StudyInstanceUID` и `SeriesInstanceUID`,</br>
будут созданы следующие пути для хранения файлов: `no_StudyInstance` и `no_SeriesInstance` соответственно.</br>

:heavy_exclamation_mark: В случае отсутствия ключа `SOPInstanceUID`, файлу будет присвоено имя `no_SOPInstance_i`, где `i` - это порядковый номер файла.