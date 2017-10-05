
from json import dumps

from .base import Base

from podcast_manager.datastore import DataStore


class List(Base):

    def run(self):
        dataStore = DataStore()
        podcasts = dataStore.get_podcasts()
        for podcast in podcasts:
            print(podcast)