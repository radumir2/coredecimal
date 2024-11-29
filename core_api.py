import datetime
from typing import List

from file_system_api import FileSystemApi


class RefeshIndexEvent:
    def __init__(self, tag):
        self.tag = tag


class IndexObserver:
    def refresh(self, event: RefeshIndexEvent):
        pass


class CoreApi:
    def __init__(self, f_api: FileSystemApi):
        self.f_api = f_api
        self.index_observer: IndexObserver

    def register_index_observer(self, observer: IndexObserver):
        self.index_observer = observer

    def _area_folder(self, cd_id):
        self.f_api.find([cd_id[:1], cd_id[:2]])

    def _refresh(self, r_id):
        if self.index_observer is not None:
            self.index_observer.refresh(RefeshIndexEvent(r_id))

    def sanitize(self, tag):
        # TO DO: base64?!
        return tag

    def index(self, cd_id, tags: List[str]):
        category_index = self.f_api.find([cd_id[:1], cd_id[:2], "00"])
        crr_min = datetime.datetime.now().isoformat()[:16]
        for tag in tags:
            self.f_api.append(category_index, f"{cd_id} {tag} {crr_min}")
        self._refresh(cd_id)

        main_index = self.f_api.find(["0", "00"])
        for tag in tags:
            f_tag = self.sanitize(tag)
            self.f_api.append(f"{main_index}/{f_tag}", cd_id)
            self._refresh(f"{main_index}/{f_tag}")

    def add_item_to_standard_folder(self, category, message):
        pass