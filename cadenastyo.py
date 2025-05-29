#!/usr/bin/env python
# read xyz coordinate file
# -*- coding: utf-8 -*-

import visual as vs
import numpy as np


filenamet1 = "datos1t.dat"
filenameo1 = "datos1o.dat"

filenamet2 = "datos2t.dat"
filenameo2 = "datos2o.dat"

filenamet3 = "datos3t.dat"
filenameo3 = "datos3o.dat"

filenamet4 = "datos4t.dat"
filenameo4 = "datos4o.dat"

filenamet5 = "datos5t.dat"
filenameo5 = "datos5o.dat"

filenamet6 = "datos6t.dat"
filenameo6 = "datos6o.dat"

filenamet7 = "datos7t.dat"
filenameo7 = "datos7o.dat"

filenamet8 = "datos8t.dat"
filenameo8 = "datos8o.dat"

filenamet9 = "datos9t.dat"
filenameo9 = "datos9o.dat"

filenamet10 = "datos10t.dat"
filenameo10 = "datos10o.dat"

filenamet11 = "datos11t.dat"
filenameo11 = "datos11o.dat"

filenamet12 = "datos12t.dat"
filenameo12 = "datos12o.dat"

filenamet13 = "datos13t.dat"
filenameo13 = "datos13o.dat"

filenamet14 = "datos14t.dat"
filenameo14 = "datos14o.dat"

filenamet15 = "datos15t.dat"
filenameo15 = "datos15o.dat"

filenamet16 = "datos16t.dat"
filenameo16 = "datos16o.dat"

filenamet17 = "datos17t.dat"
filenameo17 = "datos17o.dat"

filenamet18 = "datos18t.dat"
filenameo18 = "datos18o.dat"

filenamet19 = "datos19t.dat"
filenameo19 = "datos19o.dat"

filenamet20 = "datos20t.dat"
filenameo20 = "datos20o.dat"

filenamet21 = "datos21t.dat"
filenameo21 = "datos21o.dat"

filenamet22 = "datos22t.dat"
filenameo22 = "datos22o.dat"

filenamet23 = "datos23t.dat"
filenameo23 = "datos23o.dat"

filenamet24 = "datos24t.dat"
filenameo24 = "datos24o.dat"

filenamet25 = "datos25t.dat"
filenameo25 = "datos25o.dat"

filenamet26 = "datos26t.dat"
filenameo26 = "datos26o.dat"

filenamet27 = "datos27t.dat"
filenameo27 = "datos27o.dat"

filenamet28 = "datos28t.dat"
filenameo28 = "datos28o.dat"

filenamet29 = "datos29t.dat"
filenameo29 = "datos29o.dat"

filenamet30 = "datos30t.dat"
filenameo30 = "datos30o.dat"

filenamet31 = "datos31t.dat"
filenameo31 = "datos31o.dat"

filenamet32 = "datos32t.dat"
filenameo32 = "datos32o.dat"

filenamet33 = "datos33t.dat"
filenameo33 = "datos33o.dat"

filenamet34 = "datos34t.dat"
filenameo34 = "datos34o.dat"

filenamet35 = "datos35t.dat"
filenameo35 = "datos35o.dat"

filenamet36 = "datos36t.dat"
filenameo36 = "datos36o.dat"

filenamet37 = "datos37t.dat"
filenameo37 = "datos37o.dat"

filenamet38 = "datos38t.dat"
filenameo38 = "datos38o.dat"

filenamet39 = "datos39t.dat"
filenameo39 = "datos39o.dat"

filenamet40 = "datos40t.dat"
filenameo40 = "datos40o.dat"

filenamet41 = "datos41t.dat"
filenameo41 = "datos41o.dat"

filenamet42 = "datos42t.dat"
filenameo42 = "datos42o.dat"

filenamet43 = "datos43t.dat"
filenameo43 = "datos43o.dat"

filenamet44 = "datos44t.dat"
filenameo44 = "datos44o.dat"

filenamet45 = "datos45t.dat"
filenameo45 = "datos45o.dat"

filenamet46 = "datos46t.dat"
filenameo46 = "datos46o.dat"

filenamet47 = "datos47t.dat"
filenameo47 = "datos47o.dat"

filenamet48 = "datos48t.dat"
filenameo48 = "datos48o.dat"

filenamet49 = "datos49t.dat"
filenameo49 = "datos49o.dat"

filenamet50 = "datos50t.dat"
filenameo50 = "datos50o.dat"

filenamet51 = "datos51t.dat"
filenameo51 = "datos51o.dat"

filenamet52 = "datos52t.dat"
filenameo52 = "datos52o.dat"

filenamet53 = "datos53t.dat"
filenameo53 = "datos53o.dat"

filenamet54 = "datos54t.dat"
filenameo54 = "datos54o.dat"

filenamet55 = "datos55t.dat"
filenameo55 = "datos55o.dat"

filenamet56 = "datos56t.dat"
filenameo56 = "datos56o.dat"

filenamet57 = "datos57t.dat"
filenameo57 = "datos57o.dat"

filenamet58 = "datos58t.dat"
filenameo58 = "datos58o.dat"

filenamet59 = "datos59t.dat"
filenameo59 = "datos59o.dat"

filenamet60 = "datos60t.dat"
filenameo60 = "datos60o.dat"

filenamet61 = "datos61t.dat"
filenameo61 = "datos61o.dat"

filenamet62 = "datos62t.dat"
filenameo62 = "datos62o.dat"

filenamet63 = "datos63t.dat"
filenameo63 = "datos63o.dat"

filenamet64 = "datos64t.dat"
filenameo64 = "datos64o.dat"



#Pide pasos en dinamica

##nparti= raw_input("numero de particulas en paramTyR.dat:")
##Fparti= int(nparti)

lectura = raw_input("pasos en dinamica db.dat:")
pasos= int(lectura)

#############VELOCIDAD DE LECTURA DE DATOS##############
vel_fotogramas=100

#############VECTOR DE CAMPO ELECTRICO##########
campo = vs.arrow(pos = (3, 3,3),axis = (0,0, 1), color = vs.color.blue)
campo = vs.arrow(pos = (3, 3,3),axis = (0,1, 0), color = vs.color.green)
campo = vs.arrow(pos = (3, 3,3),axis = (1,0, 0), color = vs.color.red)

mybox = vs.box(pos=(10, 14,10), length=23.392141905702925, height=23.392141905702925, width=23.392141905702925,color=vs.color.blue, opacity=0.25)

############################PARTICULA1########################

coordinatest1 = []
rx1=[]
ry1=[]
rz1=[]
xyz = open(filenamet1)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest1.append([float(x), float(y), float(z)])
    rx1.append(x)
    ry1.append(y)
    rz1.append(z)
xyz.close()

coordinateso1 = []
ox1=[]
oy1=[]
oz1=[]
xyz = open(filenameo1)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso1.append([float(x), float(y), float(z)])
    ox1.append(x)
    oy1.append(y)
    oz1.append(z)
xyz.close()

############################PARTICULA2########################

coordinatest2 = []
rx2=[]
ry2=[]
rz2=[]
xyz = open(filenamet2)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest2.append([float(x), float(y), float(z)])
    rx2.append(x)
    ry2.append(y)
    rz2.append(z)
xyz.close()

coordinateso2 = []
ox2=[]
oy2=[]
oz2=[]
xyz = open(filenameo2)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso2.append([float(x), float(y), float(z)])
    ox2.append(x)
    oy2.append(y)
    oz2.append(z)
xyz.close()

############################PARTICULA3########################

coordinatest3 = []
rx3=[]
ry3=[]
rz3=[]
xyz = open(filenamet3)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest3.append([float(x), float(y), float(z)])
    rx3.append(x)
    ry3.append(y)
    rz3.append(z)
xyz.close()

coordinateso3 = []
ox3=[]
oy3=[]
oz3=[]
xyz = open(filenameo3)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso3.append([float(x), float(y), float(z)])
    ox3.append(x)
    oy3.append(y)
    oz3.append(z)
xyz.close()


############################PARTICULA4########################

coordinatest4 = []
rx4=[]
ry4=[]
rz4=[]
xyz = open(filenamet4)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest4.append([float(x), float(y), float(z)])
    rx4.append(x)
    ry4.append(y)
    rz4.append(z)
xyz.close()

coordinateso4 = []
ox4=[]
oy4=[]
oz4=[]
xyz = open(filenameo4)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso4.append([float(x), float(y), float(z)])
    ox4.append(x)
    oy4.append(y)
    oz4.append(z)
xyz.close()
############################PARTICULA5########################

coordinatest5 = []
rx5=[]
ry5=[]
rz5=[]
xyz = open(filenamet5)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest5.append([float(x), float(y), float(z)])
    rx5.append(x)
    ry5.append(y)
    rz5.append(z)
xyz.close()

coordinateso5 = []
ox5=[]
oy5=[]
oz5=[]
xyz = open(filenameo5)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso5.append([float(x), float(y), float(z)])
    ox5.append(x)
    oy5.append(y)
    oz5.append(z)
xyz.close()
############################PARTICULA6########################

coordinatest6 = []
rx6=[]
ry6=[]
rz6=[]
xyz = open(filenamet6)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest6.append([float(x), float(y), float(z)])
    rx6.append(x)
    ry6.append(y)
    rz6.append(z)
xyz.close()

coordinateso6 = []
ox6=[]
oy6=[]
oz6=[]
xyz = open(filenameo6)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso6.append([float(x), float(y), float(z)])
    ox6.append(x)
    oy6.append(y)
    oz6.append(z)
xyz.close()
############################PARTICULA7########################

coordinatest7 = []
rx7=[]
ry7=[]
rz7=[]
xyz = open(filenamet7)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest7.append([float(x), float(y), float(z)])
    rx7.append(x)
    ry7.append(y)
    rz7.append(z)
xyz.close()

coordinateso7 = []
ox7=[]
oy7=[]
oz7=[]
xyz = open(filenameo7)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso7.append([float(x), float(y), float(z)])
    ox7.append(x)
    oy7.append(y)
    oz7.append(z)
xyz.close()
############################PARTICULA8########################


coordinatest8 = []
rx8=[]
ry8=[]
rz8=[]
xyz = open(filenamet8)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest8.append([float(x), float(y), float(z)])
    rx8.append(x)
    ry8.append(y)
    rz8.append(z)
xyz.close()

coordinateso8 = []
ox8=[]
oy8=[]
oz8=[]
xyz = open(filenameo8)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso8.append([float(x), float(y), float(z)])
    ox8.append(x)
    oy8.append(y)
    oz8.append(z)
xyz.close()
##################################PARTICULA9#########################

coordinatest9 = []
rx9=[]
ry9=[]
rz9=[]
xyz = open(filenamet9)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest9.append([float(x), float(y), float(z)])
    rx9.append(x)
    ry9.append(y)
    rz9.append(z)
xyz.close()

coordinateso9 = []
ox9=[]
oy9=[]
oz9=[]
xyz = open(filenameo9)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso9.append([float(x), float(y), float(z)])
    ox9.append(x)
    oy9.append(y)
    oz9.append(z)
xyz.close()


##################################PARTICULA10#########################

coordinatest10 = []
rx10=[]
ry10=[]
rz10=[]
xyz = open(filenamet10)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest10.append([float(x), float(y), float(z)])
    rx10.append(x)
    ry10.append(y)
    rz10.append(z)
xyz.close()

coordinateso10 = []
ox10=[]
oy10=[]
oz10=[]
xyz = open(filenameo10)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso10.append([float(x), float(y), float(z)])
    ox10.append(x)
    oy10.append(y)
    oz10.append(z)
xyz.close()

##################################PARTICULA11#########################

coordinatest11 = []
rx11=[]
ry11=[]
rz11=[]
xyz = open(filenamet11)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest11.append([float(x), float(y), float(z)])
    rx11.append(x)
    ry11.append(y)
    rz11.append(z)
xyz.close()

coordinateso11 = []
ox11=[]
oy11=[]
oz11=[]
xyz = open(filenameo11)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso11.append([float(x), float(y), float(z)])
    ox11.append(x)
    oy11.append(y)
    oz11.append(z)
xyz.close()

##################################PARTICULA12#########################

coordinatest12 = []
rx12=[]
ry12=[]
rz12=[]
xyz = open(filenamet12)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest12.append([float(x), float(y), float(z)])
    rx12.append(x)
    ry12.append(y)
    rz12.append(z)
xyz.close()

coordinateso12 = []
ox12=[]
oy12=[]
oz12=[]
xyz = open(filenameo12)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso12.append([float(x), float(y), float(z)])
    ox12.append(x)
    oy12.append(y)
    oz12.append(z)
xyz.close()

##################################PARTICULA13#########################

coordinatest13 = []
rx13=[]
ry13=[]
rz13=[]
xyz = open(filenamet13)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest13.append([float(x), float(y), float(z)])
    rx13.append(x)
    ry13.append(y)
    rz13.append(z)
xyz.close()

coordinateso13 = []
ox13=[]
oy13=[]
oz13=[]
xyz = open(filenameo13)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso13.append([float(x), float(y), float(z)])
    ox13.append(x)
    oy13.append(y)
    oz13.append(z)
xyz.close()

##################################PARTICULA14#########################

coordinatest14 = []
rx14=[]
ry14=[]
rz14=[]
xyz = open(filenamet14)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest14.append([float(x), float(y), float(z)])
    rx14.append(x)
    ry14.append(y)
    rz14.append(z)
xyz.close()

coordinateso14 = []
ox14=[]
oy14=[]
oz14=[]
xyz = open(filenameo14)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso14.append([float(x), float(y), float(z)])
    ox14.append(x)
    oy14.append(y)
    oz14.append(z)
xyz.close()
##################################PARTICULA15#########################

coordinatest15 = []
rx15=[]
ry15=[]
rz15=[]
xyz = open(filenamet15)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest15.append([float(x), float(y), float(z)])
    rx15.append(x)
    ry15.append(y)
    rz15.append(z)
xyz.close()

coordinateso15 = []
ox15=[]
oy15=[]
oz15=[]
xyz = open(filenameo15)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso15.append([float(x), float(y), float(z)])
    ox15.append(x)
    oy15.append(y)
    oz15.append(z)
xyz.close()

##################################PARTICULA16#########################

coordinatest16 = []
rx16=[]
ry16=[]
rz16=[]
xyz = open(filenamet16)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest16.append([float(x), float(y), float(z)])
    rx16.append(x)
    ry16.append(y)
    rz16.append(z)
xyz.close()

coordinateso16 = []
ox16=[]
oy16=[]
oz16=[]
xyz = open(filenameo16)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso16.append([float(x), float(y), float(z)])
    ox16.append(x)
    oy16.append(y)
    oz16.append(z)
xyz.close()


##################################PARTICULA17#########################

coordinatest17 = []
rx17=[]
ry17=[]
rz17=[]
xyz = open(filenamet17)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest17.append([float(x), float(y), float(z)])
    rx17.append(x)
    ry17.append(y)
    rz17.append(z)
xyz.close()

coordinateso17 = []
ox17=[]
oy17=[]
oz17=[]
xyz = open(filenameo17)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso17.append([float(x), float(y), float(z)])
    ox17.append(x)
    oy17.append(y)
    oz17.append(z)
xyz.close()


##################################PARTICULA18#########################

coordinatest18 = []
rx18=[]
ry18=[]
rz18=[]
xyz = open(filenamet18)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest18.append([float(x), float(y), float(z)])
    rx18.append(x)
    ry18.append(y)
    rz18.append(z)
xyz.close()

coordinateso18 = []
ox18=[]
oy18=[]
oz18=[]
xyz = open(filenameo18)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso18.append([float(x), float(y), float(z)])
    ox18.append(x)
    oy18.append(y)
    oz18.append(z)
xyz.close()

##################################PARTICULA19#########################

coordinatest19 = []
rx19=[]
ry19=[]
rz19=[]
xyz = open(filenamet19)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest19.append([float(x), float(y), float(z)])
    rx19.append(x)
    ry19.append(y)
    rz19.append(z)
xyz.close()

coordinateso19 = []
ox19=[]
oy19=[]
oz19=[]
xyz = open(filenameo19)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso19.append([float(x), float(y), float(z)])
    ox19.append(x)
    oy19.append(y)
    oz19.append(z)
xyz.close()

##################################PARTICULA20#########################

coordinatest20 = []
rx20=[]
ry20=[]
rz20=[]
xyz = open(filenamet20)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest20.append([float(x), float(y), float(z)])
    rx20.append(x)
    ry20.append(y)
    rz20.append(z)
xyz.close()

coordinateso20 = []
ox20=[]
oy20=[]
oz20=[]
xyz = open(filenameo20)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso20.append([float(x), float(y), float(z)])
    ox20.append(x)
    oy20.append(y)
    oz20.append(z)
xyz.close()

##################################PARTICULA21#########################

coordinatest21 = []
rx21=[]
ry21=[]
rz21=[]
xyz = open(filenamet21)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest21.append([float(x), float(y), float(z)])
    rx21.append(x)
    ry21.append(y)
    rz21.append(z)
xyz.close()

coordinateso21 = []
ox21=[]
oy21=[]
oz21=[]
xyz = open(filenameo21)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso21.append([float(x), float(y), float(z)])
    ox21.append(x)
    oy21.append(y)
    oz21.append(z)
xyz.close()

##################################PARTICULA22#########################

coordinatest22 = []
rx22=[]
ry22=[]
rz2=[]
xyz = open(filenamet22)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest22.append([float(x), float(y), float(z)])
    rx22.append(x)
    ry22.append(y)
    rz2.append(z)
xyz.close()

coordinateso22 = []
ox22=[]
oy22=[]
oz22=[]
xyz = open(filenameo22)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso22.append([float(x), float(y), float(z)])
    ox22.append(x)
    oy22.append(y)
    oz22.append(z)
xyz.close()


##################################PARTICULA23#########################

coordinatest23 = []
rx23=[]
ry23=[]
rz23=[]
xyz = open(filenamet23)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest23.append([float(x), float(y), float(z)])
    rx23.append(x)
    ry23.append(y)
    rz23.append(z)
xyz.close()

coordinateso23 = []
ox23=[]
oy23=[]
oz23=[]
xyz = open(filenameo23)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso23.append([float(x), float(y), float(z)])
    ox23.append(x)
    oy23.append(y)
    oz23.append(z)
xyz.close()



##################################PARTICULA24#########################

coordinatest24 = []
rx24=[]
ry24=[]
rz24=[]
xyz = open(filenamet24)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest24.append([float(x), float(y), float(z)])
    rx24.append(x)
    ry24.append(y)
    rz24.append(z)
xyz.close()

coordinateso24 = []
ox24=[]
oy24=[]
oz24=[]
xyz = open(filenameo24)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso24.append([float(x), float(y), float(z)])
    ox24.append(x)
    oy24.append(y)
    oz24.append(z)
xyz.close()

##################################PARTICULA25#########################

coordinatest25 = []
rx25=[]
ry25=[]
rz25=[]
xyz = open(filenamet25)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest25.append([float(x), float(y), float(z)])
    rx25.append(x)
    ry25.append(y)
    rz25.append(z)
xyz.close()

coordinateso25 = []
ox25=[]
oy25=[]
oz25=[]
xyz = open(filenameo25)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso25.append([float(x), float(y), float(z)])
    ox25.append(x)
    oy25.append(y)
    oz25.append(z)
xyz.close()

##################################PARTICULA26#########################

coordinatest26 = []
rx26=[]
ry26=[]
rz26=[]
xyz = open(filenamet26)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest26.append([float(x), float(y), float(z)])
    rx26.append(x)
    ry26.append(y)
    rz26.append(z)
xyz.close()

coordinateso26 = []
ox26=[]
oy26=[]
oz26=[]
xyz = open(filenameo26)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso26.append([float(x), float(y), float(z)])
    ox26.append(x)
    oy26.append(y)
    oz26.append(z)
xyz.close()


##################################PARTICULA27#########################

coordinatest27 = []
rx27=[]
ry27=[]
rz27=[]
xyz = open(filenamet27)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest27.append([float(x), float(y), float(z)])
    rx27.append(x)
    ry27.append(y)
    rz27.append(z)
xyz.close()

coordinateso27 = []
ox27=[]
oy27=[]
oz27=[]
xyz = open(filenameo27)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso27.append([float(x), float(y), float(z)])
    ox27.append(x)
    oy27.append(y)
    oz27.append(z)
xyz.close()


##################################PARTICULA28#########################

coordinatest28 = []
rx28=[]
ry28=[]
rz28=[]
xyz = open(filenamet28)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest28.append([float(x), float(y), float(z)])
    rx28.append(x)
    ry28.append(y)
    rz28.append(z)
xyz.close()

coordinateso28 = []
ox28=[]
oy28=[]
oz28=[]
xyz = open(filenameo28)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso28.append([float(x), float(y), float(z)])
    ox28.append(x)
    oy28.append(y)
    oz28.append(z)
xyz.close()



##################################PARTICULA29#########################

coordinatest29 = []
rx29=[]
ry29=[]
rz29=[]
xyz = open(filenamet29)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest29.append([float(x), float(y), float(z)])
    rx29.append(x)
    ry29.append(y)
    rz29.append(z)
xyz.close()

coordinateso29 = []
ox29=[]
oy29=[]
oz29=[]
xyz = open(filenameo29)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso29.append([float(x), float(y), float(z)])
    ox29.append(x)
    oy29.append(y)
    oz29.append(z)
xyz.closz = line.split()


##################################PARTICULA30#########################

coordinatest27 = []
rx30=[]
ry30=[]
rz30=[]
xyz = open(filenamet30)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest30.append([float(x), float(y), float(z)])
    rx30.append(x)
    ry30.append(y)
    rz30.append(z)
xyz.close()

coordinateso30 = []
ox30=[]
oy30=[]
oz30=[]
xyz = open(filenameo30)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso30.append([float(x), float(y), float(z)])
    ox30.append(x)
    oy30.append(y)
    oz30.append(z)
xyz.close()



##################################PARTICULA31#########################

coordinatest31 = []
rx31=[]
ry31=[]
rz31=[]
xyz = open(filenamet31)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest31.append([float(x), float(y), float(z)])
    rx31.append(x)
    ry31.append(y)
    rz31.append(z)
xyz.close()

coordinateso31 = []
ox31=[]
oy31=[]
oz31=[]
xyz = open(filenameo31)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso31.append([float(x), float(y), float(z)])
    ox31.append(x)
    oy31.append(y)
    oz31.append(z)
xyz.close()

##################################PARTICULA32#########################

coordinatest32 = []
rx32=[]
ry32=[]
rz32=[]
xyz = open(filenamet32)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest32.append([float(x), float(y), float(z)])
    rx32.append(x)
    ry32.append(y)
    rz32.append(z)
xyz.close()

coordinateso32 = []
ox32=[]
oy32=[]
oz32=[]
xyz = open(filenameo32)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso32.append([float(x), float(y), float(z)])
    ox32.append(x)
    oy32.append(y)
    oz32.append(z)
xyz.close()


##################################PARTICULA33#########################

coordinatest33 = []
rx33=[]
ry33=[]
rz33=[]
xyz = open(filenamet33)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest33.append([float(x), float(y), float(z)])
    rx33.append(x)
    ry33.append(y)
    rz33.append(z)
xyz.close()

coordinateso33 = []
ox33=[]
oy33=[]
oz3=[]
xyz = open(filenameo33)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso33.append([float(x), float(y), float(z)])
    ox33.append(x)
    oy33.append(y)
    oz33.append(z)
xyz.close()

##################################PARTICULA34#########################

coordinatest34 = []
rx34=[]
ry34=[]
rz34=[]
xyz = open(filenamet34)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest34.append([float(x), float(y), float(z)])
    rx34.append(x)
    ry34.append(y)
    rz34.append(z)
xyz.close()

coordinateso34 = []
ox34=[]
oy34=[]
oz34=[]
xyz = open(filenameo34)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso34.append([float(x), float(y), float(z)])
    ox34.append(x)
    oy34.append(y)
    oz34.append(z)
xyz.close()


##################################PARTICULA35#########################

coordinatest35 = []
rx35=[]
ry35=[]
rz35=[]
xyz = open(filenamet35)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest35.append([float(x), float(y), float(z)])
    rx35.append(x)
    ry35.append(y)
    rz35.append(z)
xyz.close()

coordinateso35 = []
ox35=[]
oy35=[]
oz35=[]
xyz = open(filenameo35)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso35.append([float(x), float(y), float(z)])
    ox35.append(x)
    oy35.append(y)
    oz35.append(z)
xyz.close()


##################################PARTICULA36#########################

coordinatest36 = []
rx36=[]
ry36=[]
rz36=[]
xyz = open(filenamet36)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest36.append([float(x), float(y), float(z)])
    rx36.append(x)
    ry36.append(y)
    rz36.append(z)
xyz.close()

coordinateso36 = []
ox36=[]
oy36=[]
oz36=[]
xyz = open(filenameo36)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso36.append([float(x), float(y), float(z)])
    ox36.append(x)
    oy36.append(y)
    oz36.append(z)
xyz.close()

##################################PARTICULA37#########################

coordinatest37 = []
rx37=[]
ry37=[]
rz37=[]
xyz = open(filenamet37)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest37.append([float(x), float(y), float(z)])
    rx37.append(x)
    ry37.append(y)
    rz37.append(z)
xyz.close()

coordinateso37 = []
ox37=[]
oy37=[]
oz37=[]
xyz = open(filenameo37)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso37.append([float(x), float(y), float(z)])
    ox37.append(x)
    oy37.append(y)
    oz37.append(z)
xyz.close()

##################################PARTICULA16#########################

coordinatest38 = []
rx38=[]
ry38=[]
rz38=[]
xyz = open(filenamet38)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest38.append([float(x), float(y), float(z)])
    rx38.append(x)
    ry38.append(y)
    rz38.append(z)
xyz.close()

coordinateso38 = []
ox38=[]
oy38=[]
oz38=[]
xyz = open(filenameo38)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso38.append([float(x), float(y), float(z)])
    ox38.append(x)
    oy38.append(y)
    oz38.append(z)
xyz.close()


##################################PARTICULA39#########################

coordinatest39 = []
rx39=[]
ry39=[]
rz39=[]
xyz = open(filenamet39)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest39.append([float(x), float(y), float(z)])
    rx39.append(x)
    ry39.append(y)
    rz39.append(z)
xyz.close()

coordinateso39 = []
ox39=[]
oy39=[]
oz39=[]
xyz = open(filenameo39)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso39.append([float(x), float(y), float(z)])
    ox39.append(x)
    oy39.append(y)
    oz39.append(z)
xyz.close()

##################################PARTICULA40#########################

coordinatest40 = []
rx40=[]
ry40=[]
rz40=[]
xyz = open(filenamet40)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest40.append([float(x), float(y), float(z)])
    rx40.append(x)
    ry40.append(y)
    rz40.append(z)
xyz.close()

coordinateso40 = []
ox40=[]
oy40=[]
oz40=[]
xyz = open(filenameo40)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso40.append([float(x), float(y), float(z)])
    ox40.append(x)
    oy40.append(y)
    oz40.append(z)
xyz.close()

##################################PARTICULA41#########################

coordinatest41 = []
rx41=[]
ry41=[]
rz41=[]
xyz = open(filenamet41)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest41.append([float(x), float(y), float(z)])
    rx41.append(x)
    ry41.append(y)
    rz41.append(z)
xyz.close()


coordinateso41 = []
ox41=[]
oy41=[]
oz41=[]
xyz = open(filenameo41)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso41.append([float(x), float(y), float(z)])
    ox41.append(x)
    oy41.append(y)
    oz41.append(z)
xyz.close()

##################################PARTICULA42#########################

coordinatest42 = []
rx42=[]
ry42=[]
rz42=[]
xyz = open(filenamet42)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest42.append([float(x), float(y), float(z)])
    rx42.append(x)
    ry42.append(y)
    rz42.append(z)
xyz.close()

coordinateso42 = []
ox42=[]
oy42=[]
oz42=[]
xyz = open(filenameo42)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso42.append([float(x), float(y), float(z)])
    ox42.append(x)
    oy42.append(y)
    oz42.append(z)
xyz.close()

##################################PARTICULA43#########################

coordinatest43 = []
rx43=[]
ry43=[]
rz43=[]
xyz = open(filenamet43)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest43.append([float(x), float(y), float(z)])
    rx43.append(x)
    ry43.append(y)
    rz43.append(z)
xyz.close()

coordinateso43 = []
ox43=[]
oy43=[]
oz43=[]
xyz = open(filenameo43)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso43.append([float(x), float(y), float(z)])
    ox43.append(x)
    oy43.append(y)
    oz43.append(z)
xyz.close()

##################################PARTICULA44#########################

coordinatest44 = []
rx44=[]
ry44=[]
rz44=[]
xyz = open(filenamet44)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest44.append([float(x), float(y), float(z)])
    rx44.append(x)
    ry44.append(y)
    rz44.append(z)
xyz.close()

coordinateso44 = []
ox44=[]
oy44=[]
oz44=[]
xyz = open(filenameo44)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso44.append([float(x), float(y), float(z)])
    ox44.append(x)
    oy44.append(y)
    oz44.append(z)
xyz.close()


##################################PARTICULA45#########################

coordinatest45 = []
rx45=[]
ry45=[]
rz45=[]
xyz = open(filenamet45)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest45.append([float(x), float(y), float(z)])
    rx45.append(x)
    ry45.append(y)
    rz45.append(z)
xyz.close()

coordinateso45 = []
ox45=[]
oy45=[]
oz45=[]
xyz = open(filenameo45)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso45.append([float(x), float(y), float(z)])
    ox45.append(x)
    oy45.append(y)
    oz45.append(z)
xyz.close()


##################################PARTICULA46#########################

coordinatest46 = []
rx46=[]
ry46=[]
rz46=[]
xyz = open(filenamet46)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest46.append([float(x), float(y), float(z)])
    rx46.append(x)
    ry46.append(y)
    rz46.append(z)
xyz.close()

coordinateso46 = []
ox46=[]
oy46=[]
oz46=[]
xyz = open(filenameo46)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso46.append([float(x), float(y), float(z)])
    ox46.append(x)
    oy46.append(y)
    oz46.append(z)
xyz.close()

##################################PARTICULA47#########################

coordinatest47 = []
rx47=[]
ry47=[]
rz47=[]
xyz = open(filenamet47)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest47.append([float(x), float(y), float(z)])
    rx47.append(x)
    ry47.append(y)
    rz47.append(z)
xyz.close()

coordinateso47 = []
ox47=[]
oy47=[]
oz47=[]
xyz = open(filenameo47)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso47.append([float(x), float(y), float(z)])
    ox47.append(x)
    oy47.append(y)
    oz47.append(z)
xyz.close()


##################################PARTICULA48#########################

coordinatest48 = []
rx48=[]
ry48=[]
rz48=[]
xyz = open(filenamet48)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest48.append([float(x), float(y), float(z)])
    rx48.append(x)
    ry48.append(y)
    rz48.append(z)
xyz.close()

coordinateso48 = []
ox48=[]
oy48=[]
oz48=[]
xyz = open(filenameo48)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso48.append([float(x), float(y), float(z)])
    ox48.append(x)
    oy48.append(y)
    oz48.append(z)
xyz.close()


##################################PARTICULA49#########################

coordinatest49 = []
rx49=[]
ry49=[]
rz49=[]
xyz = open(filenamet49)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest49.append([float(x), float(y), float(z)])
    rx49.append(x)
    ry49.append(y)
    rz49.append(z)
xyz.close()

coordinateso49 = []
ox49=[]
oy49=[]
oz49=[]
xyz = open(filenameo49)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso49.append([float(x), float(y), float(z)])
    ox49.append(x)
    oy49.append(y)
    oz49.append(z)
xyz.close()



##################################PARTICULA50#########################

coordinatest50 = []
rx50=[]
ry50=[]
rz50=[]
xyz = open(filenamet50)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest50.append([float(x), float(y), float(z)])
    rx50.append(x)
    ry50.append(y)
    rz50.append(z)
xyz.close()

coordinateso50 = []

ox50=[]
oy50=[]
oz50=[]
xyz = open(filenameo50)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso50.append([float(x), float(y), float(z)])
    ox50.append(x)
    oy50.append(y)
    oz50.append(z)
xyz.close()



##################################PARTICULA51#########################

coordinatest27 = []
rx51=[]
ry51=[]
rz51=[]
xyz = open(filenamet51)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest51.append([float(x), float(y), float(z)])
    rx51.append(x)
    ry51.append(y)
    rz51.append(z)
xyz.close()

coordinateso51 = []
ox51=[]
oy51=[]
oz51=[]
xyz = open(filenameo51)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso51.append([float(x), float(y), float(z)])
    ox51.append(x)
    oy51.append(y)
    oz51.append(z)
xyz.close()


##################################PARTICUL52#########################

coordinatest52 = []
rx52=[]
ry52=[]
rz52=[]
xyz = open(filenamet52)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest52.append([float(x), float(y), float(z)])
    rx52.append(x)
    ry52.append(y)
    rz52.append(z)
xyz.close()

coordinateso52 = []
ox52=[]
oy52=[]
oz52=[]
xyz = open(filenameo52)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso52.append([float(x), float(y), float(z)])
    ox52.append(x)
    oy52.append(y)
    oz52.append(z)
xyz.close()

##################################PARTICULA53#########################

coordinatest53 = []
rx53=[]
ry53=[]
rz53=[]
xyz = open(filenamet53)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest53.append([float(x), float(y), float(z)])
    rx53.append(x)
    ry53.append(y)
    rz53.append(z)
xyz.close()

coordinateso53 = []
ox53=[]
oy53=[]
oz53=[]
xyz = open(filenameo53)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso53.append([float(x), float(y), float(z)])
    ox53.append(x)
    oy53.append(y)
    oz53.append(z)
xyz.close()


##################################PARTICULA54#########################

coordinatest54 = []
rx54=[]
ry54=[]
rz54=[]
xyz = open(filenamet54)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest54.append([float(x), float(y), float(z)])
    rx54.append(x)
    ry54.append(y)
    rz54.append(z)
xyz.close()

coordinateso54 = []
ox54=[]
oy54=[]
oz54=[]
xyz = open(filenameo54)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso54.append([float(x), float(y), float(z)])
    ox54.append(x)
    oy54.append(y)
    oz54.append(z)
xyz.close()

##################################PARTICULA55#########################

coordinatest55 = []
rx55=[]
ry55=[]
rz55=[]
xyz = open(filenamet55)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest55.append([float(x), float(y), float(z)])
    rx55.append(x)
    ry55.append(y)
    rz55.append(z)
xyz.close()

coordinateso55 = []
ox55=[]
oy55=[]
oz55=[]
xyz = open(filenameo55)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso55.append([float(x), float(y), float(z)])
    ox55.append(x)
    oy55.append(y)
    oz55.append(z)
xyz.close()

##################################PARTICULA56#########################

coordinatest56 = []
rx56=[]
ry56=[]
rz56=[]
xyz = open(filenamet56)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest56.append([float(x), float(y), float(z)])
    rx56.append(x)
    ry56.append(y)
    rz56.append(z)
xyz.close()


coordinateso56 = []
ox56=[]
oy56=[]
oz56=[]
xyz = open(filenameo56)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso56.append([float(x), float(y), float(z)])
    ox56.append(x)
    oy56.append(y)
    oz56.append(z)
xyz.close()

##################################PARTICULA57#########################

coordinatest57 = []
rx57=[]
ry57=[]
rz57=[]
xyz = open(filenamet57)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest57.append([float(x), float(y), float(z)])
    rx57.append(x)
    ry57.append(y)
    rz57.append(z)
xyz.close()

coordinateso57 = []
ox57=[]
oy57=[]
oz57=[]
xyz = open(filenameo57)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso57.append([float(x), float(y), float(z)])
    ox57.append(x)
    oy57.append(y)
    oz57.append(z)
xyz.close()

##################################PARTICULA58#########################

coordinatest58 = []
rx58=[]
ry58=[]
rz58=[]
xyz = open(filenamet58)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest58.append([float(x), float(y), float(z)])
    rx58.append(x)
    ry58.append(y)
    rz58.append(z)
xyz.close()

coordinateso58 = []
ox58=[]
oy58=[]
oz58=[]
xyz = open(filenameo58)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso58.append([float(x), float(y), float(z)])
    ox58.append(x)
    oy58.append(y)
    oz58.append(z)
xyz.close()

##################################PARTICULA59#########################

coordinatest59 = []
rx59=[]
ry59=[]
rz59=[]
xyz = open(filenamet59)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest59.append([float(x), float(y), float(z)])
    rx59.append(x)
    ry59.append(y)
    rz59.append(z)
xyz.close()

coordinateso59 = []
ox59=[]
oy59=[]
oz59=[]
xyz = open(filenameo59)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso59.append([float(x), float(y), float(z)])
    ox59.append(x)
    oy59.append(y)
    oz59.append(z)
xyz.close()


##################################PARTICULA60#########################

coordinatest60 = []
rx60=[]
ry60=[]
rz60=[]
xyz = open(filenamet60)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest60.append([float(x), float(y), float(z)])
    rx60.append(x)
    ry60.append(y)
    rz60.append(z)
xyz.close()

coordinateso60 = []
ox60=[]
oy60=[]
oz60=[]
xyz = open(filenameo60)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso60.append([float(x), float(y), float(z)])
    ox60.append(x)
    oy60.append(y)
    oz60.append(z)
xyz.close()


##################################PARTICULA61#########################

coordinatest61 = []
rx61=[]
ry61=[]
rz61=[]
xyz = open(filenamet61)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest61.append([float(x), float(y), float(z)])
    rx61.append(x)
    ry61.append(y)
    rz61.append(z)
xyz.close()

coordinateso61 = []
ox61=[]
oy61=[]
oz61=[]
xyz = open(filenameo61)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso61.append([float(x), float(y), float(z)])
    ox61.append(x)
    oy61.append(y)
    oz61.append(z)
xyz.close()

##################################PARTICULA62#########################

coordinatest62 = []
rx62=[]
ry62=[]
rz62=[]
xyz = open(filenamet62)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest62.append([float(x), float(y), float(z)])
    rx62.append(x)
    ry62.append(y)
    rz62.append(z)
xyz.close()

coordinateso62 = []
ox62=[]
oy62=[]
oz62=[]
xyz = open(filenameo62)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso62.append([float(x), float(y), float(z)])
    ox62.append(x)
    oy62.append(y)
    oz62.append(z)
xyz.close()


##################################PARTICULA63#########################

coordinatest63 = []
rx63=[]
ry63=[]
rz63=[]
xyz = open(filenamet63)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest63.append([float(x), float(y), float(z)])
    rx63.append(x)
    ry63.append(y)
    rz63.append(z)
xyz.close()

coordinateso63 = []
ox63=[]
oy63=[]
oz63=[]
xyz = open(filenameo63)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso63.append([float(x), float(y), float(z)])
    ox63.append(x)
    oy63.append(y)
    oz63.append(z)
xyz.close()


##################################PARTICULA64#########################

coordinatest64 = []
rx64=[]
ry64=[]
rz64=[]
xyz = open(filenamet64)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinatest64.append([float(x), float(y), float(z)])
    rx64.append(x)
    ry64.append(y)
    rz64.append(z)
xyz.close()

coordinateso64 = []
ox64=[]
oy64=[]
oz64=[]
xyz = open(filenameo64)
title = xyz.readline()
for line in xyz:
    x,y,z = line.split()
    coordinateso64.append([float(x), float(y), float(z)])
    ox64.append(x)
    oy64.append(y)
    oz64.append(z)
xyz.close()







###############################################################################

bola1 = vs.sphere(pos = (float(rx1[0]),float(ry1[0]),float(rz1[0])),radius=0.35, color=vs.color.cyan)
flecha1 = vs.arrow(pos = (float(rx1[0]),float(ry1[0]),float(rz1[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola2 = vs.sphere(pos = (float(rx2[0]),float(ry2[0]),float(rz2[0])),radius=0.35, color=vs.color.cyan)
flecha2 = vs.arrow(pos = (float(rx2[0]),float(ry2[0]),float(rz2[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola3 = vs.sphere(pos = (float(rx3[0]),float(ry3[0]),float(rz3[0])),radius=0.35, color=vs.color.cyan)
flecha3 = vs.arrow(pos = (float(rx3[0]),float(ry3[0]),float(rz3[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola4 = vs.sphere(pos = (float(rx4[0]),float(ry4[0]),float(rz4[0])),radius=0.35, color=vs.color.cyan)
flecha4 = vs.arrow(pos = (float(rx4[0]),float(ry4[0]),float(rz4[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola5 = vs.sphere(pos = (float(rx5[0]),float(ry5[0]),float(rz5[0])),radius=0.35, color=vs.color.cyan)
flecha5 = vs.arrow(pos = (float(rx5[0]),float(ry5[0]),float(rz5[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola6 = vs.sphere(pos = (float(rx6[0]),float(ry6[0]),float(rz6[0])),radius=0.35, color=vs.color.cyan)
flecha6 = vs.arrow(pos = (float(rx6[0]),float(ry6[0]),float(rz6[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola7 = vs.sphere(pos = (float(rx7[0]),float(ry7[0]),float(rz7[0])),radius=0.35, color=vs.color.cyan)
flecha7 = vs.arrow(pos = (float(rx7[0]),float(ry7[0]),float(rz7[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola8 = vs.sphere(pos = (float(rx8[0]),float(ry8[0]),float(rz8[0])),radius=0.35, color=vs.color.cyan)
flecha8 = vs.arrow(pos = (float(rx8[0]),float(ry8[0]),float(rz8[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola9 = vs.sphere(pos = (float(rx9[0]),float(ry9[0]),float(rz9[0])),radius=0.35, color=vs.color.cyan)
flecha9 = vs.arrow(pos = (float(rx9[0]),float(ry9[0]),float(rz9[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola10 = vs.sphere(pos = (float(rx10[0]),float(ry10[0]),float(rz10[0])),radius=0.35, color=vs.color.cyan)
flecha10 = vs.arrow(pos = (float(rx10[0]),float(ry10[0]),float(rz10[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola11 = vs.sphere(pos = (float(rx11[0]),float(ry11[0]),float(rz11[0])),radius=0.35, color=vs.color.cyan)
flecha11 = vs.arrow(pos = (float(rx11[0]),float(ry11[0]),float(rz11[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola12 = vs.sphere(pos = (float(rx12[0]),float(ry12[0]),float(rz12[0])),radius=0.35, color=vs.color.cyan)
flecha12 = vs.arrow(pos = (float(rx12[0]),float(ry12[0]),float(rz12[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola13 = vs.sphere(pos = (float(rx13[0]),float(ry13[0]),float(rz13[0])),radius=0.35, color=vs.color.cyan)
flecha13 = vs.arrow(pos = (float(rx13[0]),float(ry13[0]),float(rz13[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola14 = vs.sphere(pos = (float(rx14[0]),float(ry14[0]),float(rz14[0])),radius=0.35, color=vs.color.cyan)
flecha14 = vs.arrow(pos = (float(rx14[0]),float(ry14[0]),float(rz14[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola15 = vs.sphere(pos = (float(rx15[0]),float(ry15[0]),float(rz15[0])),radius=0.35, color=vs.color.cyan)
flecha15 = vs.arrow(pos = (float(rx15[0]),float(ry15[0]),float(rz15[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola16 = vs.sphere(pos = (float(rx16[0]),float(ry16[0]),float(rz16[0])),radius=0.35, color=vs.color.cyan)
flecha16 = vs.arrow(pos = (float(rx16[0]),float(ry16[0]),float(rz16[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola17 = vs.sphere(pos = (float(rx17[0]),float(ry17[0]),float(rz17[0])),radius=0.35, color=vs.color.cyan)
flecha17 = vs.arrow(pos = (float(rx17[0]),float(ry17[0]),float(rz17[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola18 = vs.sphere(pos = (float(rx18[0]),float(ry18[0]),float(rz18[0])),radius=0.35, color=vs.color.cyan)
flecha18 = vs.arrow(pos = (float(rx18[0]),float(ry18[0]),float(rz18[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola19 = vs.sphere(pos = (float(rx19[0]),float(ry19[0]),float(rz19[0])),radius=0.35, color=vs.color.cyan)
flecha19 = vs.arrow(pos = (float(rx19[0]),float(ry19[0]),float(rz19[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola20 = vs.sphere(pos = (float(rx20[0]),float(ry20[0]),float(rz20[0])),radius=0.35, color=vs.color.cyan)
flecha20 = vs.arrow(pos = (float(rx20[0]),float(ry20[0]),float(rz20[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola21 = vs.sphere(pos = (float(rx21[0]),float(ry21[0]),float(rz21[0])),radius=0.35, color=vs.color.cyan)
flecha21 = vs.arrow(pos = (float(rx21[0]),float(ry21[0]),float(rz21[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola22 = vs.sphere(pos = (float(rx22[0]),float(ry22[0]),float(rz22[0])),radius=0.35, color=vs.color.cyan)
flecha22 = vs.arrow(pos = (float(rx22[0]),float(ry22[0]),float(rz22[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola23 = vs.sphere(pos = (float(rx23[0]),float(ry23[0]),float(rz23[0])),radius=0.35, color=vs.color.cyan)
flecha23 = vs.arrow(pos = (float(rx23[0]),float(ry23[0]),float(rz23[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola24 = vs.sphere(pos = (float(rx24[0]),float(ry24[0]),float(rz24[0])),radius=0.35, color=vs.color.cyan)
flecha24 = vs.arrow(pos = (float(rx24[0]),float(ry24[0]),float(rz24[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola25 = vs.sphere(pos = (float(rx25[0]),float(ry25[0]),float(rz25[0])),radius=0.35, color=vs.color.cyan)
flecha25 = vs.arrow(pos = (float(rx25[0]),float(ry25[0]),float(rz25[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola26 = vs.sphere(pos = (float(rx26[0]),float(ry26[0]),float(rz26[0])),radius=0.35, color=vs.color.cyan)
flecha26 = vs.arrow(pos = (float(rx26[0]),float(ry26[0]),float(rz26[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola27 = vs.sphere(pos = (float(rx27[0]),float(ry27[0]),float(rz27[0])),radius=0.35, color=vs.color.cyan)
flecha27 = vs.arrow(pos = (float(rx27[0]),float(ry27[0]),float(rz27[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola28 = vs.sphere(pos = (float(rx28[0]),float(ry28[0]),float(rz28[0])),radius=0.35, color=vs.color.cyan)
flecha28 = vs.arrow(pos = (float(rx28[0]),float(ry28[0]),float(rz28[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola29 = vs.sphere(pos = (float(rx29[0]),float(ry29[0]),float(rz29[0])),radius=0.35, color=vs.color.cyan)
flecha29 = vs.arrow(pos = (float(rx29[0]),float(ry29[0]),float(rz29[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola30 = vs.sphere(pos = (float(rx30[0]),float(ry30[0]),float(rz30[0])),radius=0.35, color=vs.color.cyan)
flecha30 = vs.arrow(pos = (float(rx30[0]),float(ry30[0]),float(rz30[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola31 = vs.sphere(pos = (float(rx31[0]),float(ry31[0]),float(rz31[0])),radius=0.35, color=vs.color.cyan)
flecha31 = vs.arrow(pos = (float(rx31[0]),float(ry31[0]),float(rz31[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola32 = vs.sphere(pos = (float(rx32[0]),float(ry32[0]),float(rz32[0])),radius=0.35, color=vs.color.cyan)
flecha32 = vs.arrow(pos = (float(rx32[0]),float(ry32[0]),float(rz32[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola33 = vs.sphere(pos = (float(rx33[0]),float(ry33[0]),float(rz33[0])),radius=0.35, color=vs.color.cyan)
flecha33 = vs.arrow(pos = (float(rx33[0]),float(ry33[0]),float(rz33[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola34 = vs.sphere(pos = (float(rx34[0]),float(ry34[0]),float(rz34[0])),radius=0.35, color=vs.color.cyan)
flecha34 = vs.arrow(pos = (float(rx34[0]),float(ry34[0]),float(rz34[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola35 = vs.sphere(pos = (float(rx35[0]),float(ry35[0]),float(rz35[0])),radius=0.35, color=vs.color.cyan)
flecha35 = vs.arrow(pos = (float(rx35[0]),float(ry35[0]),float(rz35[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola36 = vs.sphere(pos = (float(rx36[0]),float(ry36[0]),float(rz36[0])),radius=0.35, color=vs.color.cyan)
flecha36 = vs.arrow(pos = (float(rx36[0]),float(ry36[0]),float(rz36[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola37 = vs.sphere(pos = (float(rx37[0]),float(ry37[0]),float(rz37[0])),radius=0.35, color=vs.color.cyan)
flecha37 = vs.arrow(pos = (float(rx37[0]),float(ry37[0]),float(rz37[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola38 = vs.sphere(pos = (float(rx38[0]),float(ry38[0]),float(rz38[0])),radius=0.35, color=vs.color.cyan)
flecha38 = vs.arrow(pos = (float(rx38[0]),float(ry38[0]),float(rz38[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola39 = vs.sphere(pos = (float(rx39[0]),float(ry39[0]),float(rz39[0])),radius=0.35, color=vs.color.cyan)
flecha39 = vs.arrow(pos = (float(rx39[0]),float(ry39[0]),float(rz39[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola40 = vs.sphere(pos = (float(rx40[0]),float(ry40[0]),float(rz40[0])),radius=0.35, color=vs.color.cyan)
flecha40 = vs.arrow(pos = (float(rx40[0]),float(ry40[0]),float(rz40[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola41 = vs.sphere(pos = (float(rx41[0]),float(ry41[0]),float(rz41[0])),radius=0.35, color=vs.color.cyan)
flecha41 = vs.arrow(pos = (float(rx41[0]),float(ry41[0]),float(rz41[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola42 = vs.sphere(pos = (float(rx42[0]),float(ry42[0]),float(rz42[0])),radius=0.35, color=vs.color.cyan)
flecha42 = vs.arrow(pos = (float(rx42[0]),float(ry42[0]),float(rz42[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola43 = vs.sphere(pos = (float(rx43[0]),float(ry43[0]),float(rz43[0])),radius=0.35, color=vs.color.cyan)
flecha43 = vs.arrow(pos = (float(rx43[0]),float(ry43[0]),float(rz43[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola44 = vs.sphere(pos = (float(rx44[0]),float(ry44[0]),float(rz44[0])),radius=0.35, color=vs.color.cyan)
flecha44 = vs.arrow(pos = (float(rx44[0]),float(ry44[0]),float(rz44[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola45 = vs.sphere(pos = (float(rx45[0]),float(ry45[0]),float(rz45[0])),radius=0.35, color=vs.color.cyan)
flecha45 = vs.arrow(pos = (float(rx45[0]),float(ry45[0]),float(rz45[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola46 = vs.sphere(pos = (float(rx46[0]),float(ry46[0]),float(rz46[0])),radius=0.35, color=vs.color.cyan)
flecha46 = vs.arrow(pos = (float(rx46[0]),float(ry46[0]),float(rz46[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola47 = vs.sphere(pos = (float(rx47[0]),float(ry47[0]),float(rz47[0])),radius=0.35, color=vs.color.cyan)
flecha47 = vs.arrow(pos = (float(rx47[0]),float(ry47[0]),float(rz47[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola48 = vs.sphere(pos = (float(rx48[0]),float(ry48[0]),float(rz48[0])),radius=0.35, color=vs.color.cyan)
flecha48 = vs.arrow(pos = (float(rx48[0]),float(ry48[0]),float(rz48[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola49 = vs.sphere(pos = (float(rx49[0]),float(ry49[0]),float(rz49[0])),radius=0.35, color=vs.color.cyan)
flecha49 = vs.arrow(pos = (float(rx49[0]),float(ry49[0]),float(rz49[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola50 = vs.sphere(pos = (float(rx50[0]),float(ry50[0]),float(rz50[0])),radius=0.35, color=vs.color.cyan)
flecha50 = vs.arrow(pos = (float(rx50[0]),float(ry50[0]),float(rz50[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola51 = vs.sphere(pos = (float(rx51[0]),float(ry51[0]),float(rz51[0])),radius=0.35, color=vs.color.cyan)
flecha51 = vs.arrow(pos = (float(rx51[0]),float(ry51[0]),float(rz51[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola52 = vs.sphere(pos = (float(rx52[0]),float(ry52[0]),float(rz52[0])),radius=0.35, color=vs.color.cyan)
flecha52 = vs.arrow(pos = (float(rx52[0]),float(ry52[0]),float(rz52[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola53 = vs.sphere(pos = (float(rx53[0]),float(ry53[0]),float(rz53[0])),radius=0.35, color=vs.color.cyan)
flecha53 = vs.arrow(pos = (float(rx53[0]),float(ry53[0]),float(rz53[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola54 = vs.sphere(pos = (float(rx54[0]),float(ry54[0]),float(rz54[0])),radius=0.35, color=vs.color.cyan)
flecha54 = vs.arrow(pos = (float(rx54[0]),float(ry54[0]),float(rz54[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola55 = vs.sphere(pos = (float(rx55[0]),float(ry55[0]),float(rz55[0])),radius=0.35, color=vs.color.cyan)
flecha55 = vs.arrow(pos = (float(rx55[0]),float(ry55[0]),float(rz55[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola56 = vs.sphere(pos = (float(rx56[0]),float(ry56[0]),float(rz56[0])),radius=0.35, color=vs.color.cyan)
flecha56 = vs.arrow(pos = (float(rx56[0]),float(ry56[0]),float(rz56[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola57 = vs.sphere(pos = (float(rx57[0]),float(ry57[0]),float(rz57[0])),radius=0.35, color=vs.color.cyan)
flecha57 = vs.arrow(pos = (float(rx57[0]),float(ry57[0]),float(rz57[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola58 = vs.sphere(pos = (float(rx58[0]),float(ry58[0]),float(rz58[0])),radius=0.35, color=vs.color.cyan)
flecha58 = vs.arrow(pos = (float(rx58[0]),float(ry58[0]),float(rz58[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola59 = vs.sphere(pos = (float(rx59[0]),float(ry59[0]),float(rz59[0])),radius=0.35, color=vs.color.cyan)
flecha59 = vs.arrow(pos = (float(rx59[0]),float(ry59[0]),float(rz59[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola60 = vs.sphere(pos = (float(rx60[0]),float(ry60[0]),float(rz60[0])),radius=0.35, color=vs.color.cyan)
flecha60 = vs.arrow(pos = (float(rx60[0]),float(ry60[0]),float(rz60[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola61 = vs.sphere(pos = (float(rx61[0]),float(ry61[0]),float(rz61[0])),radius=0.35, color=vs.color.cyan)
flecha61 = vs.arrow(pos = (float(rx61[0]),float(ry61[0]),float(rz61[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola62 = vs.sphere(pos = (float(rx62[0]),float(ry62[0]),float(rz62[0])),radius=0.35, color=vs.color.cyan)
flecha62 = vs.arrow(pos = (float(rx62[0]),float(ry62[0]),float(rz62[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola63 = vs.sphere(pos = (float(rx63[0]),float(ry63[0]),float(rz63[0])),radius=0.35, color=vs.color.cyan)
flecha63 = vs.arrow(pos = (float(rx63[0]),float(ry63[0]),float(rz63[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)

bola64 = vs.sphere(pos = (float(rx64[0]),float(ry64[0]),float(rz64[0])),radius=0.35, color=vs.color.cyan)
flecha64 = vs.arrow(pos = (float(rx64[0]),float(ry64[0]),float(rz64[0])),axis =(0.25,0.25,0.25), color = vs.color.yellow)


for i in range(0,pasos,1):
    bola1.pos = (float(rx1[i]), float(ry1[i]), float(rz1[i]))
    flecha1.pos = (float(rx1[i]), float(ry1[i]), float(rz1[i]))
    flecha1.axis = (float(ox1[i]), float(oy1[i]), float(oz1[i]))
    bola2.pos = (float(rx2[i]), float(ry2[i]), float(rz2[i]))
    flecha2.pos = (float(rx2[i]), float(ry2[i]), float(rz2[i]))
    flecha2.axis = (float(ox2[i]), float(oy2[i]), float(oz2[i]))
    bola3.pos = (float(rx3[i]), float(ry3[i]), float(rz3[i]))
    flecha3.pos = (float(rx3[i]), float(ry3[i]), float(rz3[i]))
    flecha3.axis = (float(ox3[i]), float(oy3[i]), float(oz3[i]))
    bola4.pos = (float(rx4[i]), float(ry4[i]), float(rz4[i]))
    flecha4.pos = (float(rx4[i]), float(ry4[i]), float(rz4[i]))
    flecha4.axis = (float(ox4[i]), float(oy4[i]), float(oz4[i]))
    bola5.pos = (float(rx5[i]), float(ry5[i]), float(rz5[i]))
    flecha5.pos = (float(rx5[i]), float(ry5[i]), float(rz5[i]))
    flecha5.axis = (float(ox5[i]), float(oy5[i]), float(oz5[i]))
    bola6.pos = (float(rx6[i]), float(ry6[i]), float(rz6[i]))
    flecha6.pos = (float(rx6[i]), float(ry6[i]), float(rz6[i]))
    flecha6.axis = (float(ox6[i]), float(oy6[i]), float(oz6[i]))
    bola7.pos = (float(rx7[i]), float(ry7[i]), float(rz7[i]))
    flecha7.pos = (float(rx7[i]), float(ry7[i]), float(rz7[i]))
    flecha7.axis = (float(ox7[i]), float(oy7[i]), float(oz7[i]))
    bola8.pos = (float(rx8[i]), float(ry8[i]), float(rz8[i]))
    flecha8.pos = (float(rx8[i]), float(ry8[i]), float(rz8[i]))
    flecha8.axis = (float(ox8[i]), float(oy8[i]), float(oz8[i]))
    bola9.pos = (float(rx9[i]), float(ry9[i]), float(rz9[i]))
    flecha9.pos = (float(rx9[i]), float(ry9[i]), float(rz9[i]))
    flecha9.axis = (float(ox9[i]), float(oy9[i]), float(oz9[i]))
    bola10.pos = (float(rx10[i]), float(ry10[i]), float(rz10[i]))
    flecha10.pos = (float(rx10[i]), float(ry10[i]), float(rz10[i]))
    flecha10.axis = (float(ox10[i]), float(oy10[i]), float(oz10[i]))
    bola11.pos = (float(rx11[i]), float(ry11[i]), float(rz11[i]))
    flecha11.pos = (float(rx11[i]), float(ry11[i]), float(rz11[i]))
    flecha11.axis = (float(ox11[i]), float(oy11[i]), float(oz11[i]))
    bola12.pos = (float(rx12[i]), float(ry12[i]), float(rz12[i]))
    flecha12.pos = (float(rx12[i]), float(ry12[i]), float(rz12[i]))
    flecha12.axis = (float(ox12[i]), float(oy12[i]), float(oz12[i]))
    bola13.pos = (float(rx13[i]), float(ry13[i]), float(rz13[i]))
    flecha13.pos = (float(rx13[i]), float(ry13[i]), float(rz13[i]))
    flecha13.axis = (float(ox13[i]), float(oy13[i]), float(oz13[i]))
    bola14.pos = (float(rx14[i]), float(ry14[i]), float(rz14[i]))
    flecha14.pos = (float(rx14[i]), float(ry14[i]), float(rz14[i]))
    flecha14.axis = (float(ox14[i]), float(oy14[i]), float(oz14[i]))
    bola15.pos = (float(rx15[i]), float(ry15[i]), float(rz15[i]))
    flecha15.pos = (float(rx15[i]), float(ry15[i]), float(rz15[i]))
    flecha15.axis = (float(ox15[i]), float(oy15[i]), float(oz15[i]))
    bola16.pos = (float(rx16[i]), float(ry16[i]), float(rz16[i]))
    flecha16.pos = (float(rx16[i]), float(ry16[i]), float(rz16[i]))
    flecha16.axis = (float(ox16[i]), float(oy16[i]), float(oz16[i]))
    bola17.pos = (float(rx17[i]), float(ry17[i]), float(rz17[i]))
    flecha17.pos = (float(rx17[i]), float(ry17[i]), float(rz17[i]))
    flecha17.axis = (float(ox17[i]), float(oy17[i]), float(oz17[i]))
    bola18.pos = (float(rx18[i]), float(ry18[i]), float(rz18[i]))
    flecha18.pos = (float(rx18[i]), float(ry18[i]), float(rz18[i]))
    flecha18.axis = (float(ox18[i]), float(oy18[i]), float(oz18[i]))
    bola19.pos = (float(rx19[i]), float(ry19[i]), float(rz18[i]))
    flecha19.pos = (float(rx19[i]), float(ry19[i]), float(rz19[i]))
    flecha19.axis = (float(ox19[i]), float(oy19[i]), float(oz19[i]))
    bola20.pos = (float(rx20[i]), float(ry20[i]), float(rz20[i]))
    flecha20.pos = (float(rx20[i]), float(ry20[i]), float(rz20[i]))
    flecha20.axis = (float(ox20[i]), float(oy20[i]), float(oz20[i]))
    bola21.pos = (float(rx21[i]), float(ry21[i]), float(rz21[i]))
    flecha21.pos = (float(rx21[i]), float(ry21[i]), float(rz21[i]))
    flecha21.axis = (float(ox21[i]), float(oy21[i]), float(oz21[i]))
    bola22.pos = (float(rx22[i]), float(ry22[i]), float(rz22[i]))
    flecha22.pos = (float(rx22[i]), float(ry22[i]), float(rz22[i]))
    flecha22.axis = (float(ox22[i]), float(oy22[i]), float(oz22[i]))
    bola23.pos = (float(rx23[i]), float(ry23[i]), float(rz23[i]))
    flecha23.pos = (float(rx23[i]), float(ry23[i]), float(rz23[i]))
    flecha23.axis = (float(ox23[i]), float(oy23[i]), float(oz23[i]))
    bola24.pos = (float(rx24[i]), float(ry24[i]), float(rz24[i]))
    flecha24.pos = (float(rx24[i]), float(ry24[i]), float(rz24[i]))
    flecha24.axis = (float(ox24[i]), float(oy24[i]), float(oz24[i]))
    bola25.pos = (float(rx25[i]), float(ry25[i]), float(rz25[i]))
    flecha25.pos = (float(rx25[i]), float(ry25[i]), float(rz25[i]))
    flecha25.axis = (float(ox25[i]), float(oy25[i]), float(oz25[i]))
    bola26.pos = (float(rx26[i]), float(ry26[i]), float(rz26[i]))
    flecha26.pos = (float(rx26[i]), float(ry26[i]), float(rz26[i]))
    flecha26.axis = (float(ox26[i]), float(oy26[i]), float(oz26[i]))
    bola27.pos = (float(rx27[i]), float(ry27[i]), float(rz27[i]))
    flecha27.pos = (float(rx27[i]), float(ry27[i]), float(rz27[i]))
    flecha27.axis = (float(ox27[i]), float(oy27[i]), float(oz27[i]))
    bola28.pos = (float(rx28[i]), float(ry28[i]), float(rz28[i]))
    flecha28.pos = (float(rx28[i]), float(ry28[i]), float(rz28[i]))
    flecha28.axis = (float(ox28[i]), float(oy28[i]), float(oz28[i]))
    bola29.pos = (float(rx29[i]), float(ry29[i]), float(rz29[i]))
    flecha29.pos = (float(rx29[i]), float(ry29[i]), float(rz29[i]))
    flecha29.axis = (float(ox29[i]), float(oy29[i]), float(oz29[i]))
    bola30.pos = (float(rx30[i]), float(ry30[i]), float(rz30[i]))
    flecha30.pos = (float(rx30[i]), float(ry30[i]), float(rz30[i]))
    flecha30.axis = (float(ox30[i]), float(oy30[i]), float(oz30[i]))
    bola31.pos = (float(rx31[i]), float(ry31[i]), float(rz31[i]))
    flecha31.pos = (float(rx31[i]), float(ry31[i]), float(rz31[i]))
    flecha31.axis = (float(ox31[i]), float(oy31[i]), float(oz31[i]))
    bola32.pos = (float(rx32[i]), float(ry32[i]), float(rz32[i]))
    flecha32.pos = (float(rx32[i]), float(ry32[i]), float(rz32[i]))
    flecha32.axis = (float(ox32[i]), float(oy32[i]), float(oz32[i]))
    bola33.pos = (float(rx33[i]), float(ry33[i]), float(rz33[i]))
    flecha33.pos = (float(rx33[i]), float(ry33[i]), float(rz33[i]))
    flecha33.axis = (float(ox33[i]), float(oy33[i]), float(oz33[i]))
    bola34.pos = (float(rx34[i]), float(ry34[i]), float(rz34[i]))
    flecha34.pos = (float(rx34[i]), float(ry34[i]), float(rz34[i]))
    flecha34.axis = (float(ox34[i]), float(oy34[i]), float(oz34[i]))
    bola35.pos = (float(rx35[i]), float(ry35[i]), float(rz35[i]))
    flecha35.pos = (float(rx35[i]), float(ry35[i]), float(rz35[i]))
    flecha35.axis = (float(ox35[i]), float(oy35[i]), float(oz35[i]))
    bola36.pos = (float(rx36[i]), float(ry36[i]), float(rz36[i]))
    flecha36.pos = (float(rx36[i]), float(ry36[i]), float(rz36[i]))
    flecha36.axis = (float(ox36[i]), float(oy36[i]), float(oz36[i]))
    bola37.pos = (float(rx37[i]), float(ry37[i]), float(rz37[i]))
    flecha37.pos = (float(rx37[i]), float(ry37[i]), float(rz37[i]))
    flecha37.axis = (float(ox37[i]), float(oy37[i]), float(oz37[i]))
    bola38.pos = (float(rx38[i]), float(ry38[i]), float(rz38[i]))
    flecha38.pos = (float(rx38[i]), float(ry38[i]), float(rz38[i]))
    flecha38.axis = (float(ox38[i]), float(oy38[i]), float(oz38[i]))
    bola39.pos = (float(rx39[i]), float(ry39[i]), float(rz39[i]))
    flecha39.pos = (float(rx39[i]), float(ry39[i]), float(rz39[i]))
    flecha39.axis = (float(ox39[i]), float(oy39[i]), float(oz39[i]))
    bola40.pos = (float(rx40[i]), float(ry40[i]), float(rz40[i]))
    flecha40.pos = (float(rx40[i]), float(ry40[i]), float(rz40[i]))
    flecha40.axis = (float(ox40[i]), float(oy40[i]), float(oz40[i]))
    bola41.pos = (float(rx41[i]), float(ry41[i]), float(rz41[i]))
    flecha41.pos = (float(rx41[i]), float(ry41[i]), float(rz41[i]))
    flecha41.axis = (float(ox41[i]), float(oy41[i]), float(oz41[i]))
    bola42.pos = (float(rx42[i]), float(ry42[i]), float(rz42[i]))
    flecha42.pos = (float(rx42[i]), float(ry42[i]), float(rz42[i]))
    flecha42.axis = (float(ox42[i]), float(oy42[i]), float(oz42[i]))
    bola43.pos = (float(rx43[i]), float(ry43[i]), float(rz43[i]))
    flecha43.pos = (float(rx43[i]), float(ry43[i]), float(rz43[i]))
    flecha43.axis = (float(ox43[i]), float(oy43[i]), float(oz43[i]))
    bola44.pos = (float(rx44[i]), float(ry44[i]), float(rz44[i]))
    flecha44.pos = (float(rx44[i]), float(ry44[i]), float(rz44[i]))
    flecha44.axis = (float(ox44[i]), float(oy44[i]), float(oz44[i]))
    bola45.pos = (float(rx45[i]), float(ry45[i]), float(rz45[i]))
    flecha45.pos = (float(rx45[i]), float(ry45[i]), float(rz45[i]))
    flecha45.axis = (float(ox45[i]), float(oy45[i]), float(oz45[i]))
    bola46.pos = (float(rx46[i]), float(ry46[i]), float(rz46[i]))
    flecha46.pos = (float(rx46[i]), float(ry46[i]), float(rz46[i]))
    flecha46.axis = (float(ox46[i]), float(oy46[i]), float(oz46[i]))
    bola47.pos = (float(rx47[i]), float(ry47[i]), float(rz47[i]))
    flecha47.pos = (float(rx47[i]), float(ry47[i]), float(rz47[i]))
    flecha47.axis = (float(ox47[i]), float(oy47[i]), float(oz47[i]))
    bola48.pos = (float(rx48[i]), float(ry48[i]), float(rz48[i]))
    flecha48.pos = (float(rx48[i]), float(ry48[i]), float(rz48[i]))
    flecha48.axis = (float(ox48[i]), float(oy48[i]), float(oz48[i]))
    bola49.pos = (float(rx49[i]), float(ry49[i]), float(rz49[i]))
    flecha49.pos = (float(rx49[i]), float(ry49[i]), float(rz49[i]))
    flecha49.axis = (float(ox49[i]), float(oy49[i]), float(oz49[i]))
    bola50.pos = (float(rx50[i]), float(ry50[i]), float(rz50[i]))
    flecha50.pos = (float(rx50[i]), float(ry50[i]), float(rz50[i]))
    flecha50.axis = (float(ox50[i]), float(oy50[i]), float(oz50[i]))
    bola51.pos = (float(rx51[i]), float(ry51[i]), float(rz51[i]))
    flecha51.pos = (float(rx51[i]), float(ry51[i]), float(rz51[i]))
    flecha51.axis = (float(ox51[i]), float(oy51[i]), float(oz51[i]))
    bola52.pos = (float(rx52[i]), float(ry52[i]), float(rz52[i]))
    flecha52.pos = (float(rx52[i]), float(ry52[i]), float(rz52[i]))
    flecha52.axis = (float(ox52[i]), float(oy52[i]), float(oz52[i]))
    bola53.pos = (float(rx53[i]), float(ry53[i]), float(rz53[i]))
    flecha53.pos = (float(rx53[i]), float(ry53[i]), float(rz53[i]))
    flecha53.axis = (float(ox53[i]), float(oy53[i]), float(oz53[i]))
    bola54.pos = (float(rx54[i]), float(ry54[i]), float(rz54[i]))
    flecha54.pos = (float(rx54[i]), float(ry54[i]), float(rz54[i]))
    flecha54.axis = (float(ox54[i]), float(oy54[i]), float(oz54[i]))
    bola55.pos = (float(rx55[i]), float(ry55[i]), float(rz55[i]))
    flecha55.pos = (float(rx55[i]), float(ry55[i]), float(rz55[i]))
    flecha55.axis = (float(ox55[i]), float(oy55[i]), float(oz55[i]))
    bola56.pos = (float(rx56[i]), float(ry56[i]), float(rz56[i]))
    flecha56.pos = (float(rx56[i]), float(ry56[i]), float(rz56[i]))
    flecha56.axis = (float(ox56[i]), float(oy56[i]), float(oz56[i]))
    bola57.pos = (float(rx57[i]), float(ry57[i]), float(rz57[i]))
    flecha57.pos = (float(rx57[i]), float(ry57[i]), float(rz57[i]))
    flecha57.axis = (float(ox57[i]), float(oy57[i]), float(oz57[i]))
    bola58.pos = (float(rx58[i]), float(ry58[i]), float(rz58[i]))
    flecha58.pos = (float(rx58[i]), float(ry58[i]), float(rz58[i]))
    flecha58.axis = (float(ox58[i]), float(oy58[i]), float(oz58[i]))
    bola59.pos = (float(rx59[i]), float(ry59[i]), float(rz59[i]))
    flecha59.pos = (float(rx59[i]), float(ry59[i]), float(rz59[i]))
    flecha59.axis = (float(ox59[i]), float(oy59[i]), float(oz59[i]))
    bola60.pos = (float(rx60[i]), float(ry60[i]), float(rz60[i]))
    flecha60.pos = (float(rx60[i]), float(ry60[i]), float(rz60[i]))
    flecha60.axis = (float(ox60[i]), float(oy60[i]), float(oz60[i]))
    bola61.pos = (float(rx61[i]), float(ry61[i]), float(rz61[i]))
    flecha61.pos = (float(rx61[i]), float(ry61[i]), float(rz61[i]))
    flecha61.axis = (float(ox61[i]), float(oy61[i]), float(oz61[i]))
    bola62.pos = (float(rx62[i]), float(ry62[i]), float(rz62[i]))
    flecha62.pos = (float(rx62[i]), float(ry62[i]), float(rz62[i]))
    flecha62.axis = (float(ox62[i]), float(oy62[i]), float(oz62[i]))
    bola63.pos = (float(rx63[i]), float(ry63[i]), float(rz63[i]))
    flecha63.pos = (float(rx63[i]), float(ry63[i]), float(rz63[i]))
    flecha63.axis = (float(ox63[i]), float(oy63[i]), float(oz63[i]))
    bola64.pos = (float(rx64[i]), float(ry64[i]), float(rz64[i]))
    flecha64.pos = (float(rx64[i]), float(ry64[i]), float(rz64[i]))
    flecha64.axis = (float(ox64[i]), float(oy64[i]), float(oz64[i]))


    print(i)
#    print(float(rx5[i]), float(ry5[i]), float(rz5[i]))
    vs.rate(vel_fotogramas)



scene.autoscale = True
userzoom = True
userspin = True

