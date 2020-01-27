# Author: HARI ADHIKARI
# UNIVERSITY OF HELSINKI
# PhD student (Researcher)
# Department of Geosciences and Geography
# EARTH CHANGE OBSERVATION LABORATORY
# P.O. Box 68 (Gustaf Hällströmin katu 2b)
# FI-00014 University of Helsinki, Finland
# Office +358294151204
#        +358504487028
# Home   +358449899584
# Email: hari.adhikari@helsinki.fi; harisubash2002@yahoo.com

# Affiliated with 
# Helsinki Institute of Sustainability Science (HELSUS)
# Institute for Atmospheric and Earth System Research (INAR)


# BASIC DESCRIPTION
# This script will reclassify (slice) raster file, and save results as tiff file. We will read this result in R studio 
# and calculate the percentage of each class, with na.rm = TRUE

# INSTALL AND IMPORT SYSTEM MODULES
import arcpy, os
from arcpy import env
from arcpy.sa import *

# SET ENVIRONMENT SETTINGS
#arcpy.env.workspace = "C:/HY-Data/ADHIHARI/PhD_Articles/6th_Paper/Data/FinalScans3D/Shapefiles/Rasterfiles/Slopefiles"
#outptConFol = r"C:\HY-Data\ADHIHARI\PhD_Articles\6th_Paper\Data\FinalScans3D\Shapefiles\Rasterfiles\Slopefiles\NaturalBreak\0pt05_natbrk"

arcpy.env.workspace = "C:/HY-Data/ADHIHARI/PhD_Articles/6th_Paper/Data/temp/FinalScans2andhalfD/PLYfolder/Shapefiles/Rasterfiles/Slopefiles"
outptConFol = r"C:\HY-Data\ADHIHARI\PhD_Articles\6th_Paper\Data\temp\FinalScans2andhalfD\PLYfolder\Shapefiles\Rasterfiles\Slopefiles\NaturalBreak\0pt05_natbrk"

# use r when you use \ symbol

# CHECK OUT THE ARCGIS SPATIAL ANALYST EXTENSION LICENSE
arcpy.CheckOutExtension("Spatial")
arcpy.CheckOutExtension("3D")

# FIND NECESSARY RASTER FILE
# In a loop we will find all those raster files who ends with _0pt05.tif, as we are only intersted in those raster with original resolution
# Make changes if you need different Contour Interval and Base Contour
for tiff in arcpy.ListRasters("*_0pt05_slope.tif"): 
   in_surface = tiff
   out_tif_file = os.path.join(outptConFol,os.path.splitext(os.path.basename(tiff))[0]+"_natbrk.tif") # Although the original resoultion is 0.05, it will be really messy
   outslice = Slice(in_surface, 3, "NATURAL_BREAKS") 
   outslice.save(out_tif_file)
