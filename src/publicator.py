import shutil
import os
from src import common_utils


def public_local(package_name):
    """
    Опубликовать пакет локально
    :(package_name:
    :return:
    """
    common_utils.ensure_directory("/nginx-builder/rpms/")
    shutil.move(package_name, "/nginx-builder/rpms/")
