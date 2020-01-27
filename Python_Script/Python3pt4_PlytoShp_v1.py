# Written by: Michael Mechenich, email: mike.mechenich@gmail.com
# Modified by: Hari Adhikari, Department of Geosciences and Geography, University of Helsinki, email: hari.adhikari@helsinki.fi
# Cited from: Spatial and Statistical Analysis in Ecological and Paleontological Research
# Michael Mechenich, Master’s Examination, University of Helsinki, Department of Geosciences and Geography, April 2017

# SINGLE CONDITION
# If you want to run the script just for one file, use inputfile and output file and continue from line # Script 1: PLY-SHP Converter
# ------------------------------------------------------------------------------
#inputfile = "C:/HY-Data/ADHIKARI/OneDrive/OneDrive - University of Helsinki/Turkana/3D scans/PLY/" + \
#           "KNMER61454NoteuiM3.ply"
#outputfile = "C:/HY-Data/ADHIKARI/OneDrive/OneDrive - University of Helsinki/Turkana/3D scans/PLY/Shapefiles/" + \
#            "KNMER61454NoteuiM3.shp"

# ------------------------------------------------------------------------------

# MULTIPLE CONDITION
# If you want to run the script for many files (batch mode), continue from line "import sys"
# In this case, you have to give name for input and output file through loop.
# for example, in R you can run this python scrip whose name is "Python3pt4_PlytoShp.py" as follows
# PLYFOLDER<- "C:/HY-Data/ADHIHARI/PhD_Articles/6th_Paper/Data/Test_cut_scans"
# ShapefileDir<- "C:/HY-Data/ADHIHARI/PhD_Articles/6th_Paper/Data/Test_cut_scans/ShapeFile"
# setwd(PLYFOLDER)
# ply_inputfiles <- list.files(, full.names = FALSE, pattern=".ply") # If you make true, you get the whole link to folder and file
# ply_outputShapefiles<- gsub(".ply", ".shp", ply_inputfiles)
# inputfile = file.path(PLYFOLDER, ply_inputfiles)
# outputfile = file.path(PLYFOLDER, ShapefileDir, ply_outputShapefiles)
# write.table(inputfile, "ListofPLYFiles.txt", row.names=FALSE, col.names=FALSE, quote=F) # Just in case you want to save the list
# write.table(outputfile, "ListofShapeFiles.txt", row.names=FALSE, col.names=FALSE, quote=F) # Just in case you want to save the list
# command <- c("C:\\Python34\\python.exe","C:/HY-Data/ADHIHARI/PhD_Articles/6th_Paper/Data/Test_cut_scans/Python3pt4_PlytoShp.py" ) # 64 byte computer 
# for (r in 1:length(inputfile)) { 
# args = c(inputfile[r], outputfile[r]) # Build up args in a vector
# system2(command, args=args, stdout=TRUE)# Run python command
# rm(args,allArgs)
# }
# ------------------------------------------------------------------------------

import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]

# Script 1: PLY-SHP Converter
import shapefile

inputfile = open(inputfile, "r")

record = inputfile.readline().strip("\n")
while record != "end_header":
    record = inputfile.readline().strip("\n")

print ("Reading vertex vectors...")
vertex = [[], [], []]
record = inputfile.readline().strip(" \n").split(" ")
while len(record) == 3:
    vertex[0].append(float(record[0]))
    vertex[1].append(float(record[1]))
    vertex[2].append(float(record[2]))
 
    if len(vertex[0]) % 100000 == 0:
       print ("\t%i vertex vectors read..." % len(vertex[0]))
   
    record = inputfile.readline().strip(" \n").split(" ")
print ("Done. %i vertex vector(s) read." % len(vertex[0]))
# ------------------------------------------------------------------------------
print ("\nScaling vertex vectors...")
minx = min(vertex[0])
miny = min(vertex[1])
minz = min(vertex[2])
rangey = max(vertex[1]) - miny

scaledvertex = []
for index in range(len(vertex[0])):
    x = ((vertex[0][index] - minx) / rangey) * 100.0
    y = ((vertex[1][index] - miny) / rangey) * 100.0
    z = ((vertex[2][index] - minz) / rangey) * 100.0
    scaledvertex.append([x, y, z])

print ("Done. %i vertex vector(s) scaled." % len(scaledvertex))
# ------------------------------------------------------------------------------
print ("\nReading triangles...")

triangle = []
while len(record) == 4:
    index1 = int(record[1])
    index2 = int(record[2])
    index3 = int(record[3])
    z = (scaledvertex[index1][2] +
        scaledvertex[index2][2] +
        scaledvertex[index3][2]) / 3.0
    triangle.append([z, index1, index2, index3])
    if len(triangle) % 100000 == 0:
        print ("\t%i triangles read..." % len(triangle))
        
    record = inputfile.readline().strip(" \n").split(" ")
    
inputfile.close()
print ("Done. %i triangle(s) read." % len(triangle))
# ------------------------------------------------------------------------------
print ("\nWriting shapefile...")

triangle.sort()
writer = shapefile.Writer(shapefile.POLYGON)
writer.field("ID", "N", 10, 0)
writer.field("Z", "N", 18, 10)

index = 0
for feature in triangle:
    writer.poly([[scaledvertex[feature[1]],
                  scaledvertex[feature[2]],
                  scaledvertex[feature[3]]]])
    writer.record(index, feature[0])
    
    index += 1
    if index % 100000 == 0:
        print ("\t%i features prepared..." % index)
writer.save(outputfile)
print ("Done. %i feature(s) written." % index)
