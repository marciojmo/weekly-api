import models
import decorators

class CrudDAO:
    """
    Defines CRUD operations over mongoengine models.
    """
    meta = {
        "abstract": True
    }

    def __init__(self, model):
        """
        Creates an instance of a CrudDAO by 
        settings its model reference.

        Args:
            model (mongoengine.Document): The model handled by this dao.
        """
        self.model = model

    def list_all(self, page, size, order, filters):
        """
        Lists all model objects on the database.

        Returns:
            A list of all model objects on the database.
        """
        queryset = self.model.object.filter(**filters) if filters else self.model.objects()
        offset = page * size
        queryset = queryset.skip(offset).limit(size)
        return list(queryset.order_by(*order) if order else queryset)

    def create(self, data):
        """
        Creates a new model object on the database.

        Returns:
            The recently created model on the database.
        """
        return self.model(**data).save()

    def get_by_id(self, id):
        """
        Gets a model by id.

        Args:
            The id of the model.
        
        Returns:
            The model whose id is equal to the id informed.
        """
        return self.model.objects(id=id).get()
    
    def update_by_id(self, id, data):
        """
        Updates a model by id.

        Args:
            id (string): The id of object.
            data (dict): The object's new data.

        Returns:
            The updated object data.
        """
        entity = self.get_by_id(id)
        entity.update(**data)
        return entity.reload()

    def delete_by_id(self, id):
        """
        Deletes a model by id.

        Args:
            id (string): The id of object.
        """
        self.get_by_id(id).delete()

@decorators.singleton
class TaskDAO(CrudDAO):
    """
    Handles database operations for 
    the Task model.
    """
    def __init__(self):
        super().__init__(models.Task)

