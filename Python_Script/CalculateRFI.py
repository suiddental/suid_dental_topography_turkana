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
# This script will calculate the 2 D and 3 D area from raster with resolution of 0.05
# RFI is calculated as 3D area /2D area (which means the value is always greater that 1) 

# INSTALL AND IMPORT SYSTEM MODULES
import arcpy, os
from arcpy import env
from arcpy.sa import *

# SET ENVIRONMENT SETTINGS
#arcpy.env.workspace = "C:/HY-Data/ADHIHARI/PhD_Articles/6th_Paper/Data/FinalScans3D/Shapefiles/Rasterfiles"
#outptConFol = r"C:\HY-Data\ADHIHARI\PhD_Articles\6th_Paper\Data\FinalScans3D\Shapefiles\Rasterfiles\RFI"

arcpy.env.workspace = "C:/HY-Data/ADHIHARI/PhD_Articles/6th_Paper/Data/temp/FinalScans2andhalfD/PLYfolder/Shapefiles/Rasterfiles"
outptConFol = r"C:\HY-Data\ADHIHARI\PhD_Articles\6th_Paper\Data\temp\FinalScans2andhalfD\PLYfolder\Shapefiles\Rasterfiles\RFI"

# use r when you use \ symbol

# CHECK OUT THE ARCGIS SPATIAL ANALYST EXTENSION LICENSE
arcpy.CheckOutExtension("Spatial")
arcpy.CheckOutExtension("3D")

# FIND NECESSARY RASTER FILE
# In a loop we will find all those raster files who ends with _0pt05.tif, as we are only intersted in those raster with original resolution
# Make changes if you need different Contour Interval and Base Contour
for tiff in arcpy.ListRasters("*_0pt05.tif"): 
   in_surface = tiff
   out_text_file = os.path.join(outptConFol,os.path.splitext(os.path.basename(tiff))[0]+"_SV3D.txt") # Although the original resoultion is 0.05, it will be really messy
   reference_plane = ""
   base_z=""
   z_factor=""
   pyramid_level_resolution=""
   arcpy.SurfaceVolume_3d(in_surface, out_text_file, reference_plane, base_z, z_factor,pyramid_level_resolution) # Execute Contour

# arcpy.SurfaceVolume_3d (in_surface, {out_text_file}, {reference_plane}, {base_z}, {z_factor}, {pyramid_level_resolution})
