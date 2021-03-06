import os

from pasteme import config
from playhouse.db_url import connect


MYSQL_DB = connect(config.MYSQL_URL, timeout=1800)


def create_tables():
    from pasteme.models.UserFileModel import UserFileModel
    from pasteme.models.UserModel import UserModel

    MYSQL_DB.create_tables([UserFileModel, UserModel], safe=True)

    # if not os.path.exists(os.path.join(config.BASE_DIR, 'media')):
    #     os.mkdir(os.path.join(config.BASE_DIR, 'media'))
