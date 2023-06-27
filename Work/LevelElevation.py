# -*- coding: utf-8 -*-
__title__ = "Level Elevation"
__author__ = "Onur Korkmaz"
__doc__ = """Version = 1.0
Date    = 27.06.2023
_____________________________________________________________________
Description:

Rename selected sheet with Find/Replace/Prefix/Suffix options.
_____________________________________________________________________
How-to:

-> Click the button
-> Select TitleBlock
-> Set parameters
-> Create Sheets
_____________________________________________________________________
"""
# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ==================================================
# Regular + Autodesk
import os, sys, math, datetime, time                                    # Regular Imports
from Autodesk.Revit.DB import *                                         # Import everything from DB (Very good for beginners)
from Autodesk.Revit.DB import Transaction, FilteredElementCollector     # or Import only classes that are used.

# pyRevit
from pyrevit import revit, forms                                        # import pyRevit modules. (Lots of useful features)

# Custom Imports
from Snippets._selection import get_selected_elements                   # lib import
from Snippets._convert import convert_internal_to_m                     # lib import

# .NET Imports
import clr                                  # Common Language Runtime. Makes .NET libraries accessinble
clr.AddReference("System")                  # Refference System.dll for import.
from System.Collections.Generic import List # List<ElementType>() <- it's special type of list from .NET framework that RevitAPI requires
# List_example = List[ElementId]()          # use .Add() instead of append or put python list of ElementIds in parentesis.

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ==================================================
doc   = __revit__.ActiveUIDocument.Document   # Document   class from RevitAPI that represents project. Used to Create, Delete, Modify and Query elements from the project.
uidoc = __revit__.ActiveUIDocument          # UIDocument class from RevitAPI that represents Revit project opened in the Revit UI.
app   = __revit__.Application                 # Represents the Autodesk Revit Application, providing access to documents, options and other application wide data and settings.
#PATH_SCRIPT = os.path.dirname(__file__)     # Absolute path to the folder where script is placed.

# GLOBAL VARIABLES

# - Place global variables here.

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ==================================================

def convert_internal_to_m(Length):

    rvt_year = int(app.VersionNumber)

    if rvt_year < 2022
        return UnitUtils.Convert(Length,
                                 DisplayUnitType.DUT_DECIMAL_FEET,
                                 DisplayUnitType.DUT_METERS)
    else:
        return UnitUtils.ConvertFromInternalUnits(Length, UnitTypeId.Meters)



# - Place local functions here. If you might use any functions in other scripts, consider placing it in the lib folder.

# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
# ==================================================

# - Place local classes here. If you might use any classes in other scripts, consider placing it in the lib folder.

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================


# Get all levels
all_levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()

for lvl in all_levels:
    lvl_elevation = lvl.Elevation
    lvl_elevation_m = lvl_elevation / 0.3048
    lvl_elevation_m = round(convert_internal_to_m(lvl_elevation),2)

# List Comprehension
    lvl_elevation_m_str = "*" + str(lvl_elevation_m) if lvl.Elevation>0 else str(lvl_elevation_m)

    if lvl_elevation > 0:
        var = "*" + str(lvl_elevation_m)
    else:
        var = str(lvl_elevation_m)