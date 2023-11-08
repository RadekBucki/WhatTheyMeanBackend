from enum import Enum


def dataclass_to_dict(instance):
# Convert a data class instance to a dictionary with enum values as strings.

    data_dict = {}
    for field in instance.__dataclass_fields__:
        value = getattr(instance, field)
        if isinstance(value, Enum):
            data_dict[field] = value.value
        else:
            data_dict[field] = value
    return data_dict

def dataclass_to_dict_without_id(instance):
# Convert a data class instance to a dictionary without id and with enum values as strings.

    data_dict = {}
    for field in instance.__dataclass_fields__:
        value = getattr(instance, field)
        if isinstance(value, Enum):
            data_dict[field] = value.value
        else:
            data_dict[field] = value
    data_dict.pop('_id')
    return data_dict

def dict_to_dataclass(data_dict, data_class):
# Convert a dictionary to a data class instance with enum values.

    enum_fields = [field for field in data_class.__dataclass_fields__ if isinstance(getattr(data_class, field), Enum)]
    for field in enum_fields:
        enum_type = data_class.__annotations__[field]
        enum_value = data_dict.get(field)
        if enum_value is not None:
            data_dict[field] = enum_type(enum_value)
    return data_class(**data_dict)