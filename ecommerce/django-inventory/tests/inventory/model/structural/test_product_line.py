import pytest
from django.db import models

from inventory.models import *
import uuid



"""
## Table and Column Validation
"""

@pytest.mark.parametrize("model, expected_field_count",
                         [
                             (ProductLine,8,),
                             
                          
                          ]
                         )

def test_model_structure_field_count(model, expected_field_count):
    assert (
        
        len(model._meta.fields) == expected_field_count
        ), f"{model.__name__} model has {len(model._meta.fields)} fields, expected {expected_field_count}"

"""
- [ ] Confirm the presence of all required tables within the database schema.
"""

def test_model_structure_table_exists():
    
    try:
        from inventory.models import ProductLine
    except ImportError:
        assert False
    else:
        assert True
        


"""
- [ ] Validate the existence of expected columns in each table, ensuring correct data types.
"""

@pytest.mark.parametrize("model,field_name, expected_type",
                         [
                             (ProductLine, "price", models.DecimalField),
        (ProductLine, "sku", models.UUIDField),
        (ProductLine, "stock_qty", models.IntegerField),
        (ProductLine, "is_active", models.BooleanField),
        (ProductLine, "order", models.IntegerField),
        (ProductLine, "weight", models.FloatField),
        (ProductLine, "product", models.ForeignKey),
        (ProductLine, "attribute_values", models.ManyToManyField),
                          ]
                         )

def test_model_structure_column_data_types(model, field_name, expected_type):
    assert hasattr(
        model, field_name ), f"{model.__name__} model does not have '{field_name}' field"
    
    field = model._meta.get_field(field_name)
    
    assert isinstance(field, expected_type), f"Field is not type '{expected_type}'"




"""
- [ ] Ensure that column relationships are correctly defined.
"""

# @pytest.mark.parametrize(
#     "model,field_name, expected_type, related_model, on_delete_behavior,allow_null, allow_blank",
#                           [
#         (ProductLine, "price", models.DecimalField, None, None, False, False),
#         (ProductLine, "sku", models.UUIDField, None, None, False, False),
#         (ProductLine, "stock_qty", models.IntegerField, None, None, False, False),
#         (ProductLine, "is_active", models.BooleanField, None, None, False, False),
#         (ProductLine, "order", models.IntegerField, None, None, False, False),
#         (ProductLine, "weight", models.FloatField, None, None, False, False),
#         (ProductLine, "product", models.ForeignKey, Product, models.PROTECT, False, False),
#         (ProductLine, "attribute_values", models.ManyToManyField, AttributeValue, None, False, False),
#     ]
#                          )
# def test_model_structure_relationship(model,field_name, expected_type, related_model, on_delete_behavior,allow_null, allow_blank):
#     # model = Category
#     # field_name = "parent"
#     # related_model = Category
#     # on_delete_behavior = models.PROTECT
#     assert hasattr(
#         model, field_name ), f"{model.__name__} model does not have '{field_name}' field"
    
#     field = model._meta.get_field(field_name)
    
#     assert isinstance(field, expected_type), f"Field is not type '{expected_type}'" 
    
#     assert (
#         field.related_model == related_model
#     ), f"'{field_name}' field does not related to '{related_model.__name__}' model"
    
#     assert (
#         field.remote_field.on_delete == on_delete_behavior
#     ), f"'{field_name}' field does not related to '{on_delete_behavior}' model"
    
#     assert (
#         field.null == allow_null
#     ), f"'{field_name}' field does not allow null values as expected"
    
#     assert (
#         field.blank == allow_blank
#     ), f"'{field_name}' field does not allow blank values as expected"
    
    

# @pytest.mark.parametrize("model,field_name, expected_nullable",
#                          [
#                              (Product,"description", True),
#                              (Product,"category", True),
#                              (Product,"seasonal_event", True),
                             
#                             #  (Category,"parent",models.ForeignKey),
                          
#                           ]
#                          )
# def test_model_structure_nullable_contraints(model,field_name, expected_nullable):
#     # Get the field name from the model
#     field = model._meta.get_field(field_name)
#     # Check if the nullable constraint matches the expected value
#     assert (
#         field.null is expected_nullable
#     ), f"Field '{field_name}' has unexpected nullable constraint"
    


@pytest.mark.parametrize("model,field_name, expected_default",
                         [
                             (ProductLine,"is_active", False),
                             (ProductLine,"stock_qty", 0),
                             (ProductLine,"sku", uuid.uuid4),
                             
                         ]
)    

def test_model_structure_default_values(model,field_name, expected_default):
    field = model._meta.get_field(field_name)
    
    
    assert (
        field.default == expected_default
    ), f"Field '{field_name}' has unexpected default value"
    
    
    assert (
        field.default == expected_default    )
    


# @pytest.mark.parametrize("model,field_name, expected_length",
#                          [
#                              (Product,"name", 100),
#                              (Product,"pid", 255),
                             
                             
#                          ]
# )   
# def test_model_structure_column_length(model,field_name, expected_length):
#     field = model._meta.get_field(field_name)
#     assert (
#         field.max_length == expected_length
#     ), f"Field '{field_name}' has unexpected max length"    
    
    
    

# @pytest.mark.parametrize("model,field_name, expected_unique",
#                          [
#                              (Product,"slug", True),
#                              (Product,"name", True),
#                          ]
# )   
# def test_model_structure_unique_value(model,field_name, expected_unique):
#     field = model._meta.get_field(field_name)
#     assert (
#         field.unique == expected_unique
#     ), f"Field '{field_name}' uniqueness mismatch"  
    

"""
- [ ] Verify nullable or not nullable fields
"""

"""
- [ ] Verify the correctness of default values for relevant columns.
"""

"""
- [ ] Ensure that column lengths align with defined requirements.
"""

"""
- [ ]  Validate the enforcement of unique constraints for columns requiring unique values.
"""
