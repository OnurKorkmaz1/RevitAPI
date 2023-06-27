# -*- coding: utf-8 -*-
__title__ = "Create Sheets"
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
Last update:
- [11.07.2021] GUI created
- [11.07.2021] Refactored
_____________________________________________________________________
To-do:
- GUI for TitleBlock Selection
- Restrict textfield to integers only
_____________________________________________________________________
"""

#______________________________ IMPORTS
import sys
from Autodesk.Revit.DB import (FilteredElementCollector,
                               BuiltInParameter,
                               BuiltInCategory,
                               ViewSheet,
                               Transaction)
from pyrevit.forms import SelectFromList
from pyrevit import forms

# .NET IMPORTS
import clr
from clr import AddReference
AddReference("System")
from System.Diagnostics.Process import Start
from System.Windows.Window import DragMove
from System.Windows.Input import MouseButtonState

# VARIABLES
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application