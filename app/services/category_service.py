from app.data_access.product_supabase import *
from app.models.category import Category
import json

# get list of products from data
def getAllCategories() :
    categories = dataGetCategories()
    return categories

def getCategory(id) :
    return dataGetCategory(id)