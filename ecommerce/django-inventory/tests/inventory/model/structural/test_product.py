import pytest
from django.db import models

from inventory.models import *


"""
## Table and Column Validation
"""

@pytest.mark.parametrize("model, expected_field_count",
                         [
                             (Product,12,),
                             
                          
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
        from inventory.models import Product
    except ImportError:
        assert False
    else:
        assert True
        


"""
- [ ] Validate the existence of expected columns in each table, ensuring correct data types.
"""

@pytest.mark.parametrize("model,field_name, expected_type",
                         [
                             (Product,"id", models.BigAutoField),
                             (Product,"name", models.CharField),
                             (Product,"slug", models.SlugField),
                             (Product,"is_active", models.BooleanField),
                             
                             (Product,"seasonal_event",models.ForeignKey),
                          
                          (Product,"description", models.TextField),
                             (Product,"is_digtial", models.BooleanField),
                             (Product,"created_at", models.DateTimeField),
                             (Product,"updated_at", models.DateTimeField),
                             (Product,"stock_status", models.CharField),
                             (Product,"category",models.ForeignKey),
                             (Product,"product_type",models.ManyToManyField),
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

@pytest.mark.parametrize(
    "model,field_name, expected_type, related_model, on_delete_behavior,allow_null, allow_blank",
                         [
                             (Product,"category",models.ForeignKey, Category,models.SET_NULL, True, False),
                             (Product,"seasonal_event",models.ForeignKey, SeasonalEvent,models.SET_NULL, True, True),
                             (Product,"product_type",models.ManyToManyField, ProductType,None, False, False),
                          ]
                         )
def test_model_structure_relationship(model,field_name, expected_type, related_model, on_delete_behavior,allow_null, allow_blank):
    # model = Category
    # field_name = "parent"
    # related_model = Category
    # on_delete_behavior = models.PROTECT
    assert hasattr(
        model, field_name ), f"{model.__name__} model does not have '{field_name}' field"
    
    field = model._meta.get_field(field_name)
    
    assert isinstance(field, expected_type), f"Field is not type '{expected_type}'" 
    
    assert (
        field.related_model == related_model
    ), f"'{field_name}' field does not related to '{related_model.__name__}' model"
    
    assert (
        field.remote_field.on_delete == on_delete_behavior
    ), f"'{field_name}' field does not related to '{on_delete_behavior}' model"
    
    assert (
        field.null == allow_null
    ), f"'{field_name}' field does not allow null values as expected"
    
    assert (
        field.blank == allow_blank
    ), f"'{field_name}' field does not allow blank values as expected"
    
    

@pytest.mark.parametrize("model,field_name, expected_nullable",
                         [
                             (Product,"description", True),
                             (Product,"category", True),
                             (Product,"seasonal_event", True),
                             
                            #  (Category,"parent",models.ForeignKey),
                          
                          ]
                         )
def test_model_structure_nullable_contraints(model,field_name, expected_nullable):
    # Get the field name from the model
    field = model._meta.get_field(field_name)
    # Check if the nullable constraint matches the expected value
    assert (
        field.null is expected_nullable
    ), f"Field '{field_name}' has unexpected nullable constraint"
    


@pytest.mark.parametrize("model,field_name, expected_default",
                         [
                             (Product,"is_active", False),
                             (Product,"is_digtial", False),
                             
                         ]
)    

def test_model_structure_default_values(model,field_name, expected_default):
    field = model._meta.get_field(field_name)
    
    
    assert (
        field.default == expected_default
    ), f"Field '{field_name}' has unexpected default value"
    
    
    assert (
        field.default == expected_default    )
    


@pytest.mark.parametrize("model,field_name, expected_length",
                         [
                             (Product,"name", 100),
                             (Product,"pid", 255),
                         ]
)   
def test_model_structure_column_length(model,field_name, expected_length):
    field = model._meta.get_field(field_name)
    assert (
        field.max_length == expected_length
    ), f"Field '{field_name}' has unexpected max length"    
    
    
    

@pytest.mark.parametrize("model,field_name, expected_unique",
                         [
                             (Product,"slug", True),
                             (Product,"name", True),
                         ]
)   
def test_model_structure_unique_value(model,field_name, expected_unique):
    field = model._meta.get_field(field_name)
    assert (
        field.unique == expected_unique
    ), f"Field '{field_name}' uniqueness mismatch"  
    

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