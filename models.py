import mongoengine
import datetime

class BaseModel(mongoengine.Document):
    """
    Defines attributes and methods that are 
    common to all models.
    """

    meta = {
        "abstract": True
    }

    created = mongoengine.DateTimeField()
    modified = mongoengine.DateTimeField(default=datetime.datetime.utcnow)

    def save(self,*args,**kwargs):
        """
        Updates created timestamp if needed.
        """
        if not self.created:
            self.created = datetime.datetime.utcnow()

        return super(BaseModel, self).save(*args, **kwargs)


class Task(BaseModel):
    """
    Task model.
    """
    description = mongoengine.StringField(max_length=100, required=True)
    completed = mongoengine.BooleanField(required=True, default=False)
    schedule = mongoengine.DateField(required=False)
    order = mongoengine.IntField(min_value=0,required=False)