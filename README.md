### Входные данные расположены в директории `src`.

Скрипт выполняет преобразования входных данных, используя модуль pydicom.
([документация pydicom](https://pydicom.github.io/pydicom/stable))

При запуске программы:
1. удаляется информация, хранящаяся в ключе `PatientName` (аномизируется файл)
2. используя информацию в ключах StudyInstanceUID, SeriesInstanceUID, SOPInstanceUID создается новая структура хранения файлов:
* на первом уровне `StudyInstanceUID`
* на втором уровне `SeriesInstanceUID`
* имя файла задается значением `SOPInstanceUID` с расширением `.dcm`

2. [x] Таким образом, путь к каждому файлу выглядит так: `$StudyInstanceUID/$SeriesInstanceUID/$SOPInstanceUID.dcm`


3. Создается файл `list_of_matching_paths.txt`, в котором имена файлов исходной структуры сопоставлены к путям (именам) файлов в конечной структуре.

В случае отсутствия ключей `StudyInstanceUID` и `SeriesInstanceUID`, будут созданы следующие пути для хранения файлов: 
`no_StudyInstance` и `no_SeriesInstance` соответственно.

В случае отсутствия ключа `SOPInstanceUID`, имени файла будет присвоено имя `no_SOPInstance_i`, где `i` - это порядковый номер файла.