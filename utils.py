
def parse_request_params(params, meta_filters = {}):
    """
    Parses request params.

    Args:
        params (flask.request.args): The request params.
        meta_filters (dict): Mappings between filter names and lambda functions 
        that converts the field to its respective value. Default is string.

    Returns:
        A tuple: page, size, order, filters.
        page (int): The pagination number.
        size (int): The pagination size.
        order (list): The sorting orders.
        filters (dict): A dict mapping a field to the value it should have.
    """

    page = params.get("__page", None, int)
    size = params.get("__size", None, int)
    order = params.get("__order", None, str)
    filters = None

    if order:
        order.split(',')

    extra_params = [x for x in params if x not in ["__page","__size","__order"]]
    if extra_params:
        filters = {f: meta_filters[f](params.get(f)) if f in meta_filters else params.get(f) for f in extra_params}
    
    return page, size, order, filters