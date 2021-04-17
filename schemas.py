from marshmallow import schema, fields, validate

class BaseSchema(schema.Schema):
    """
    Defines attributes that are common to all schemas.
    """

    id = fields.Str()
    created = fields.DateTime()
    modified = fields.DateTime()

class TaskSchema(BaseSchema):
    """
    Task Schema
    """
    description = fields.Str(required=True,validate=validate.Length(min=0,max=100))
    completed = fields.Boolean(required=False)
    schedule = fields.Date(required=False)
    order = fields.Integer(validate=validate.Range(min=0,max=12),required=False)