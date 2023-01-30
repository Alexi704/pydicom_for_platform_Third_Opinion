[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=4000&width=440&lines=%D0%92%D1%85%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5+%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5++%D0%B2+%D0%B4%D0%B8%D1%80%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%B8+%60src%60.)](https://git.io/typing-svg)

Скрипт выполняет преобразования входных данных, используя модуль pydicom
([документация pydicom](https://pydicom.github.io/pydicom/stable)).

При запуске программы:

:one: удаляется информация, хранящаяся в ключе `PatientName` (аномизируется файл)</br>
:two: используя информацию в ключах `StudyInstanceUID`, `SeriesInstanceUID`, `SOPInstanceUID` создается новая структура хранения файлов:
* на первом уровне `StudyInstanceUID`
* на втором уровне `SeriesInstanceUID`
* имя файла задается значением `SOPInstanceUID` с расширением `.dcm`

:point_right: Таким образом, путь к каждому файлу выглядит так: `$StudyInstanceUID/$SeriesInstanceUID/$SOPInstanceUID.dcm`


:three: Создается файл `list_of_matching_paths.txt`, в котором имена файлов исходной структуры сопоставлены к путям (именам) файлов в конечной структуре.

В случае отсутствия ключей `StudyInstanceUID` и `SeriesInstanceUID`, будут созданы следующие пути для хранения файлов: 
`no_StudyInstance` и `no_SeriesInstance` соответственно.

В случае отсутствия ключа `SOPInstanceUID`, файлу будет присвоено имя `no_SOPInstance_i`, где `i` - это порядковый номер файла.