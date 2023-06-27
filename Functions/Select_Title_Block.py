# -*- coding: utf-8 -*-
# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
#==================================================
import sys, clr
import traceback

from Autodesk.Revit.UI.Selection    import ISelectionFilter, ObjectType, Selection
from Autodesk.Revit.DB.Architecture import Room
from Autodesk.Revit.DB import *

# pyRevit IMPORTS
from pyrevit.forms import SelectFromList
from pyrevit import forms

#.NET
clr.AddReference('System')
from System.Collections.Generic import List

# CUSTOM IMPORTS
from Snippets._variables import ALL_VIEW_TYPES
from GUI.forms           import select_from_dict

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
#==================================================
uidoc     = __revit__.ActiveUIDocument
doc       = __revit__.ActiveUIDocument.Document
selection = uidoc.Selection                          # type: Selection

# ╔═╗╔═╗╦  ╔═╗╔═╗╔╦╗
# ╚═╗║╣ ║  ║╣ ║   ║
# ╚═╝╚═╝╩═╝╚═╝╚═╝ ╩
#==================================================
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SELECT TITLEBLOCK
def select_title_block(given_uidoc = uidoc, exitscript = True):
    """Function to let user select a title block.
    SelectFromList -> select_from_dict()"""

    doc = given_uidoc.Document
    #>>>>>>>>>> SELECT TITLE BLOCK
    all_title_blocks = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TitleBlocks).WhereElementIsElementType().ToElements()
    
    unique_title_blocks = {}
    for tb in all_title_blocks:
        family_name = tb.FamilyName
        type_name = tb.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString()
        unique_title_blocks["{} - {}".format(family_name, type_name)] = tb.Id


    #>>>>>>>>>> MAKE SURE IT'S SELECTED
    selected_title_block = select_from_dict(unique_title_blocks, SelectMultiple=False)

    # VERIFY SOMETHING IS SELECTED
    if not selected_title_block and exitscript:
        forms.alert("No TitleBlock was selected. Please try again.", exitscript = exitscript)

    return selected_title_block[0]