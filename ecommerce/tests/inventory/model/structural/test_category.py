import pytest
from django.db import models

from inventory.models import Category


"""
## Table and Column Validation
"""

"""
- [ ] Confirm the presence of all required tables within the database schema.
"""

def test_model_structure_table_exists():
    
    try:
        from inventory.models import Category
    except ImportError:
        assert False
    else:
        assert True
        

def test_model_1():
    assert True
    
def test_structure_2():
    assert True
        


"""
- [ ] Validate the existence of expected columns in each table, ensuring correct data types.
"""

@pytest.mark.parametrize("model,field_name, expected_type",
                         [
                             (Category,"id", models.BigAutoField),
                             (Category,"name", models.CharField),
                             (Category,"slug", models.SlugField),
                             (Category,"is_active", models.BooleanField),
                             (Category,"level", models.IntegerField),
                            #  (Category,"parent",models.ForeignKey),
                          
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
                             (Category,"parent",models.ForeignKey, Category,models.PROTECT, True, True),
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
                             (Category,"id", False),
                             (Category,"name", False),
                             (Category,"slug", False),
                             (Category,"is_active", False),
                             (Category,"level", False),
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
                             (Category,"is_active", False),
                             (Category,"level", 100),
                         ]
)    

def test_model_structure_default_values(model,field_name, expected_default):
    field = model._meta.get_field(field_name)
    
    
    assert (
        field.default == expected_default
    ), f"Field '{field_name}' has unexpected default value"
    
    level_field = model._meta.get_field("level")
    
    assert (
        
    )
    


@pytest.mark.parametrize("model,field_name, expected_length",
                         [
                             (Category,"name", 100),
                         ]
)   
def test_model_structure_expected_length(model,field_name, expected_length):
    field = model._meta.get_field(field_name)
    assert (
        field.max_length == expected_length
    ), f"Field '{field_name}' has unexpected length"    
    

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
