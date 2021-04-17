import daos
import schemas
import decorators
import config


class CrudService:
    """
    Defines CRUD operations.
    """
    meta = {
        "abstract": True
    }

    def __init__(self, dao, schema):
        self.dao = dao
        self.schema = schema

    def list_all(self, page=None, size=None, order=None, filters=None):
        """
        Lists all Models.
        
        Returns:
            The list of Models on the database.
        """
        # Validating pagination params
        page = 0 if not page or page < 0 else page
        size = min((size,config.MAX_PAGINATION_SIZE)) if size else config.DEFAULT_PAGINATION_SIZE
        entities = self.dao.list_all(page, size, order, filters)
        return self.schema.dump(entities, many=True)

    def create(self, body):
        """
        Creates a Model.

        Args:
            body (dict): The request body.
        
        Returns:
            The Model object created.
        """
        # Validates the request body and save
        validated_data = self.schema.load(body, partial=("id","created","modified"))
        entity = self.dao.create(validated_data)
        return self.schema.dump(entity)

    def get_by_id(self, id):
        """
        Gets a Model by id.

        Args:
            id (string): The id of the Model.
        
        Returns:
            The Model whose id is equal to the id informed.
        """
        entity = self.dao.get_by_id(id)
        return self.schema.dump(entity)
    
    def update_by_id(self, id, body):
        """
        Updates a Model by id.

        Args:
            id (string): The id of the Model.
            body (dict): The request body.
        
        Returns:
            The Model whose id is equal to the id informed.
        """
        # Validates the request body and save
        validated_data = self.schema.load(body, partial=True)
        entity = self.dao.update_by_id(id, validated_data)
        return self.schema.dump(entity)

    def delete_by_id(self, id):
        """
        Deletes a Model by id.

        Args:
            id (string): The id of the Model.
        """
        self.dao.delete_by_id(id)

@decorators.singleton
class TaskService(CrudService):
    """
    Defines business rules for Tasks.
    """
    def __init__(self):
        super(TaskService,self).__init__(daos.TaskDAO.get_instance(),schemas.TaskSchema())