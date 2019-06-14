from django.contrib.staticfiles.finders import AppDirectoriesFinder

from einkaufsliste.einkaufsliste.settings import BASE_DIR


class AppDirFinder(AppDirectoriesFinder):
    print(BASE_DIR)
    source_dir = '/static'