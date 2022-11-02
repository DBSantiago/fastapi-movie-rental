from api.db.base_class import Base

from api.apps.cast.models import (
    MemberModel, GenderModel, RoleModel,
)
from api.apps.films.models import (
    FilmModel, FilmTypeModel, FilmCategoryModel,
)
from api.apps.customers.models import CustomerModel
from api.apps.orders.models import OrderModel
from api.apps.seasons.models import (
    EpisodeModel, SeasonModel
)
from api.apps.users.models import (
    UserModel, UserRoleModel,
)
from api.db.session import engine
from api.utils.commands.faker_gen import (
    FakerUser, FakerCast, FakerCustomer, FakerFilm,
    FakerSeason, FakerEpisode, FakerOrder,
)

from api.utils.logger import Logger

logger = Logger.get_logger_console(__name__)


class Commands:
    @staticmethod
    def clean_database():
        """Remove all records from database."""
        logger.info("Wiping database clean of records...")
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        logger.info("Records erased!")

    @staticmethod
    def faker_populate():
        models = (FakerUser, FakerCast, FakerCustomer, FakerFilm,
                  FakerSeason, FakerEpisode, FakerOrder)
        logger.info("Generating records...")
        for model in models:
            model.generate_records()
        logger.info("Records added!")
