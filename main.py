# task: https://github.com/batuser/recruit

import os
import pydicom
from pydicom.tag import Tag

# получаем список всех исходных файлов
files_names = os.listdir('src')


def file_processing():
    for single_file in files_names:
        file_path = f'src/{single_file}'
        ds = pydicom.dcmread(file_path, force=True)

        # удаляем имя пациента
        if 'PatientName' in ds:
            patient_name = ds[0x0010, 0x0010]
            patient_name.value = None

        # получаем нужные переменные
        study_instance_UID = ds.StudyInstanceUID if 'StudyInstanceUID' in ds else 'no_StudyInstance'
        series_instance_UID = ds.SeriesInstanceUID if 'SeriesInstanceUID' in ds else 'no_SeriesInstance'
        sop_instance_UID = ds.SOPInstanceUID if 'SOPInstanceUID' in ds else 'no_SOPInstance'

        # сохраняем файл согласно следующей структуры:
        # $StudyInstanceUID/$SeriesInstanceUID/$SOPInstanceUID.dcm
        path_folder_safe = os.path.join('out', os.path.join(study_instance_UID, series_instance_UID))
        path_file_safe = os.path.join(path_folder_safe, sop_instance_UID + '.dcm')

        # проверка наличия папки для сохранения файла
        if not os.path.exists(path_folder_safe):
            os.makedirs(path_folder_safe)

        # сохраняем файл
        with open(path_file_safe, 'wb') as outfile:
            ds.save_as(outfile)

        # создаем файл со списком соответствия путей
        with open('list_of_matching_paths.txt', 'a', encoding='utf-8') as file:
            file.write(f'{single_file} > {study_instance_UID}/{series_instance_UID}/{sop_instance_UID}.dcm\n')


if __name__ == '__main__':
    file_processing()
