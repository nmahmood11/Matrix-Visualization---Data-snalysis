#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import numpy
import numpy as np

#Seasons / year
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
Sdict = {"2005":0,"2006":1,"2007":2,"2008":3,"2009":4,"2010":5,"2011":6,"2012":7,"2013":8,"2014":9}

#Players
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]
Pdict = {"KobeBryant":0,"JoeJohnson":1,"LeBronJames":2,"CarmeloAnthony":3,"DwightHoward":4,"ChrisBosh":5,"ChrisPaul":6,"KevinDurant":7,"DerrickRose":8,"DwayneWade":9}

#Salaries
KobeBryant_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
JoeJohnson_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
LeBronJames_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
CarmeloAnthony_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
DwightHoward_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
ChrisBosh_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
ChrisPaul_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
KevinDurant_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
DerrickRose_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
DwayneWade_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]
#Matrix
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])

#Games 
KobeBryant_G = [80,77,82,82,73,82,58,78,6,35]
JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80]
LeBronJames_G = [79,78,75,81,76,79,62,76,77,69]
CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40]
DwightHoward_G = [82,82,82,79,82,78,54,76,71,41]
ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44]
ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82]
KevinDurant_G = [35,35,80,74,82,78,66,81,81,27]
DerrickRose_G = [40,40,40,81,78,81,39,0,10,51]
DwayneWade_G = [75,51,51,79,77,76,49,69,54,62]
#Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])

#Minutes Played
KobeBryant_MP = [3277,3140,3192,2960,2835,2779,2232,3013,177,1207]
JoeJohnson_MP = [3340,2359,3343,3124,2886,2554,2127,2642,2575,2791]
LeBronJames_MP = [3361,3190,3027,3054,2966,3063,2326,2877,2902,2493]
CarmeloAnthony_MP = [2941,2486,2806,2277,2634,2751,1876,2482,2982,1428]
DwightHoward_MP = [3021,3023,3088,2821,2843,2935,2070,2722,2396,1223]
ChrisBosh_MP = [2751,2658,2425,2928,2526,2795,2007,2454,2531,1556]
ChrisPaul_MP = [2808,2353,3006,3002,1712,2880,2181,2335,2171,2857]
KevinDurant_MP = [1255,1255,2768,2885,3239,3038,2546,3119,3122,913]
DerrickRose_MP = [1168,1168,1168,3000,2871,3026,1375,0,311,1530]
DwayneWade_MP = [2892,1931,1954,3048,2792,2823,1625,2391,1775,1971]
#Matrix
MinutesPlayed = np.array([KobeBryant_MP, JoeJohnson_MP, LeBronJames_MP, CarmeloAnthony_MP, DwightHoward_MP, ChrisBosh_MP, ChrisPaul_MP, KevinDurant_MP, DerrickRose_MP, DwayneWade_MP])

#Field Goals
KobeBryant_FG = [978,813,775,800,716,740,574,738,31,266]
JoeJohnson_FG = [632,536,647,620,635,514,423,445,462,446]
LeBronJames_FG = [875,772,794,789,768,758,621,765,767,624]
CarmeloAnthony_FG = [756,691,728,535,688,684,441,669,743,358]
DwightHoward_FG = [468,526,583,560,510,619,416,470,473,251]
ChrisBosh_FG = [549,543,507,615,600,524,393,485,492,343]
ChrisPaul_FG = [407,381,630,631,314,430,425,412,406,568]
KevinDurant_FG = [306,306,587,661,794,711,643,731,849,238]
DerrickRose_FG = [208,208,208,574,672,711,302,0,58,338]
DwayneWade_FG = [699,472,439,854,719,692,416,569,415,509]
#Matrix
FieldGoals  = np.array([KobeBryant_FG, JoeJohnson_FG, LeBronJames_FG, CarmeloAnthony_FG, DwightHoward_FG, ChrisBosh_FG, ChrisPaul_FG, KevinDurant_FG, DerrickRose_FG, DwayneWade_FG])

#Field Goal Attempts
KobeBryant_FGA = [2173,1757,1690,1712,1569,1639,1336,1595,73,713]
JoeJohnson_FGA = [1395,1139,1497,1420,1386,1161,931,1052,1018,1025]
LeBronJames_FGA = [1823,1621,1642,1613,1528,1485,1169,1354,1353,1279]
CarmeloAnthony_FGA = [1572,1453,1481,1207,1502,1503,1025,1489,1643,806]
DwightHoward_FGA = [881,873,974,979,834,1044,726,813,800,423]
ChrisBosh_FGA = [1087,1094,1027,1263,1158,1056,807,907,953,745]
ChrisPaul_FGA = [947,871,1291,1255,637,928,890,856,870,1170]
KevinDurant_FGA = [647,647,1366,1390,1668,1538,1297,1433,1688,467]
DerrickRose_FGA = [436,436,436,1208,1373,1597,695,0,164,835]
DwayneWade_FGA = [1413,962,937,1739,1511,1384,837,1093,761,1084]
#Matrix
FieldGoalAttempts = np.array([KobeBryant_FGA, JoeJohnson_FGA, LeBronJames_FGA, CarmeloAnthony_FGA, DwightHoward_FGA, ChrisBosh_FGA, ChrisPaul_FGA, KevinDurant_FGA, DerrickRose_FGA, DwayneWade_FGA])

#Points
KobeBryant_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
JoeJohnson_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
LeBronJames_PTS = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
CarmeloAnthony_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
DwightHoward_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
ChrisBosh_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
ChrisPaul_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
KevinDurant_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
DerrickRose_PTS = [597,597,597,1361,1619,2026,852,0,159,904]
DwayneWade_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]
#Matrix
Points = np.array([KobeBryant_PTS, JoeJohnson_PTS, LeBronJames_PTS, CarmeloAnthony_PTS, DwightHoward_PTS, ChrisBosh_PTS, ChrisPaul_PTS, KevinDurant_PTS, DerrickRose_PTS, DwayneWade_PTS])             
                  


# In[2]:


Salary


# In[3]:


# Building your first matrix - 

Games


# In[4]:


Points


# In[5]:


import numpy as np # numpy is used for array imputation


# In[6]:


mydata = np.arange(0,20) 
print(mydata) 


# In[7]:


np.reshape(mydata,(5,4)) # 5 rows & 4 columns 


# In[8]:


np.reshape(mydata,(4,5)) 


# In[9]:


np.reshape(mydata,(5,4), order = 'c') #'C' means to read / write the elements using C-like index order
MATR1 = np.reshape(mydata, (5,4), order = 'c')
MATR1  


# In[10]:


# If i want to get only no.3 
MATR1[4,3]  


# In[11]:


MATR1[4,-1] 


# In[12]:


MATR1 


# In[13]:


MATR1[0,0] 


# In[14]:


np.reshape(mydata,(5,4), order = 'c') #'C' means to read / write the elements using C-like index order
MATR1 = np.reshape(mydata, (5,4), order = 'c')
MATR1 


# In[15]:


MATR2 = np.reshape(mydata, (5,4), order = 'F') # reshape behaviour are  - 'C','F','A'
MATR2


# In[16]:


MATR2


# In[17]:


MATR2[2,-1]  


# In[18]:


MATR3 = np.reshape(mydata, (5,4), order = 'A')
MATR3


# In[19]:


MATR1


# In[20]:


a1 = ['welcome', 'to','datascience']
a2 = ['required','hard','work' ]
a3 = [1,2,3] 


# In[21]:


[a1,a2,a3] 


# In[22]:


np.array([a1,a2,a3])  # u11 - unicode 11 characer : 3*3 matrix


# In[23]:


Games


# In[24]:


Games[0] 


# In[25]:


Games[2] 


# In[26]:


Games


# In[27]:


Games[2,9] 


# In[28]:


Games


# In[29]:


Games[-2,-2] 


# In[30]:


Games[-7,-7] 


# In[31]:


Points


# In[32]:


Points[6] 


# In[33]:


Points[6,1] 


# In[34]:


#====== DICTIONARY =======#

# dict does not maintain the order

dict1 = {'key1':'val1', 'key2':'val2', 'key3':'val3'} 


# In[35]:


dict1


# In[36]:


dict1['key2'] 


# In[37]:


dict2 = {'bang':2,'hyd':'we are hear', 'pune':True}


# In[38]:


dict2


# In[39]:


dict3 = {'Germany':'I have been here', 'France':2, 'Spain': True}


# In[40]:


dict3


# In[41]:


dict3['Germany'] 


# In[42]:


# if you check theat dataset seasons & players are dictionary type of data
# if you look at the pdict players names are key part:nos are the values
# dictionary can guide us which player at which level and which row
# main advantage of the dictionary is we dont required to count which no row which players are sitting


# In[43]:


Games


# In[44]:


# how do i know player kobebryant is at

Pdict['KobeBryant'] 


# In[45]:


Games[0] 


# In[46]:


Pdict['DerrickRose'] 


# In[47]:


Games[8] 


# In[48]:


Games[Pdict['DerrickRose']] 


# In[49]:


Games


# In[50]:


Games[Pdict['DerrickRose']][7] 


# In[51]:


Points[Pdict['DerrickRose']][Sdict['2011']] 


# In[52]:


Points


# In[53]:


Points[Pdict['JoeJohnson']] 


# In[54]:


#Salary[][]  & if you want to know which row & column this player belong to 

print(Pdict['LeBronJames'])  # what row he is into
print(Sdict['2009']) # which column he is into


# In[55]:


Salary


# In[56]:


Salary[2,4] 


# In[57]:


Salary[Pdict['LeBronJames']][Sdict['2009']] 


# In[58]:


# Matrix operations - 
Games


# In[59]:


978/80


# In[60]:


FieldGoals #which season how many goal player had make the goals


# In[61]:


Games


# In[62]:


# how to find goals per each player ans - 978/80, 813/77 for this kind of problems matrix operation is very helpfull
FieldGoals / Games


# In[63]:


#import warnings
#warnings.filterwarnings('ignore') 

FieldGoals/Games  # this matrix is lot of decimal points yo can not round
#round()


# In[64]:


np.matrix.round(FieldGoals/Games) 


# In[65]:


FieldGoalPerGame = np.matrix.round(FieldGoals/Games)


# In[66]:


FieldGoalPerGame 


# In[67]:


FieldGoalPerGame[Pdict['DerrickRose']][Sdict['2011']] # DERRICKROSE IS 8TH ROW & COLUMN STARTS FROM 2005


# In[68]:


FieldGoalPerGame[Pdict['DerrickRose']][Sdict['2009']]


# In[69]:


FieldGoalPerGame[Pdict['KobeBryant']][Sdict['2009']]


# In[70]:


np.matrix.round(MinutesPlayed / Games)


# In[71]:


MinutesPlayed # if you look at the 311 & 177 might these playes are injured 


# In[72]:


Games


# In[73]:


FieldGoalAttempts


# In[74]:


FieldGoals


# In[75]:


FieldGoalAttempts/FieldGoals


# In[76]:


FieldGoalsPerPlay = FieldGoalAttempts/FieldGoals
FieldGoalsPerPlay
np.matrix.round(FieldGoalsPerPlay)


# In[77]:


import numpy as np # n-dimension array
import matplotlib.pyplot as plt # visualization and plotting library
# seeborn is used for advanced visualization


# In[78]:


get_ipython().run_line_magic('matplotlib', 'inline # keep the plot inside jupyter nots insted of getting in other screen')


# In[79]:


Salary[0] 


# In[80]:


Games[0]


# In[81]:


Salary[0]


# In[82]:


plt.plot(Salary[0])  


# In[83]:


plt.plot(Salary[0], c='Red') 


# In[84]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = 8,6


# In[85]:


plt.plot(Salary[0], c='Blue', ls = '--') 


# In[86]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's') # s - squares 


# In[87]:


#%matplotlib inline
#plt.rcParams['figure.figsize'] = 9,6 #runtime configuration parameter


# In[88]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 10) 
plt.show() 


# In[89]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7)
plt.xticks(list(range(0,10)), Seasons) 
plt.show() 


# In[90]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')
plt.show() 


# In[91]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.xticks(list(range(0,10)), Seasons,rotation='horizontal')
plt.show()


# In[92]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 's', ms = 5, label = Players[1])

plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[93]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 5, label = Players[1])
plt.plot(Salary[2], c='red', ls = '--', marker = '^', ms = 8, label = Players[2])


plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[94]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 5, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 8, label = Players[2])
plt.plot(Salary[3], c='Red', ls = '--', marker = 'd', ms = 8, label = Players[3])

plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[95]:


# how to add legned in visualisation

plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 4, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 2, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 5, label = Players[2])
plt.plot(Salary[3], c='Red', ls = '--', marker = 'd', ms = 6, label = Players[3])
plt.legend() # 
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[96]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 5, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 8, label = Players[2])
plt.plot(Salary[3], c='Red', ls = '--', marker = 'd', ms = 8, label = Players[3])
plt.legend(loc = 'upper left' )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[97]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 5, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 8, label = Players[2])
plt.plot(Salary[3], c='Red', ls = '--', marker = 'd', ms = 8, label = Players[3])
plt.legend(loc = 'upper left',bbox_to_anchor=(1,0) ) 
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[98]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = 10,7 #runtime configuration parameter


# In[99]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 5, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 8, label = Players[2])
plt.plot(Salary[3], c='Red', ls = '--', marker = 'd', ms = 8, label = Players[3])
plt.legend(loc = 'right',bbox_to_anchor=(1,1) ) 
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[100]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 5, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 8, label = Players[2])
plt.plot(Salary[3], c='Red', ls = '--', marker = 'd', ms = 8, label = Players[3])
plt.legend(loc = 'lower right',bbox_to_anchor=(0.5,1) )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show() 


# In[101]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 7, label = Players[2])
plt.plot(Salary[3], c='Red', ls = '--', marker = 'D', ms = 7, label = Players[3])
plt.plot(Salary[4], c='Red', ls = '--', marker = 's', ms = 7, label = Players[4])
plt.plot(Salary[5], c='Red', ls = '--', marker = 'o', ms = 7, label = Players[5])
plt.plot(Salary[6], c='Red', ls = '--', marker = '^', ms = 7, label = Players[6])
#plt.plot(Salary[7], c='Red', ls = '--', marker = 'd', ms = 7, label = Players[7])
#plt.plot(Salary[8], c='Red', ls = '--', marker = 's', ms = 7, label = Players[8])
#plt.plot(Salary[9], c='Red', ls = '--', marker = 'o', ms = 7, label = Players[9])

plt.rcParams['figure.figsize'] = 10,9

plt.legend(loc = 'lover right',bbox_to_anchor=(0.5,1) )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[102]:


# we can visualize the how many games played by a player 

plt.plot(Games[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0]) 
plt.plot(Games[1], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[1])
plt.plot(Games[2], c='Green', ls = '--', marker = '^', ms = 7, label = Players[2])
plt.plot(Games[3], c='Red', ls = '--', marker = 'D', ms = 7, label = Players[3])
plt.plot(Games[4], c='Black', ls = '--', marker = 's', ms = 7, label = Players[4])
plt.plot(Games[5], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[5])
plt.plot(Games[6], c='red', ls = '--', marker = '^', ms = 7, label = Players[6])
plt.plot(Games[7], c='Green', ls = '--', marker = 'd', ms = 7, label = Players[7])
plt.plot(Games[8], c='Red', ls = '--', marker = 's', ms = 7, label = Players[8])
plt.plot(Games[9], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[9])

plt.legend(loc = 'lover right',bbox_to_anchor=(1,1) )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# Conclusion data analysis- 1>Matrices 2>Building matrices - np.reshape 3>Dictionaried in python (order doesnot mater) (keys & values) 4>visualizaing using pyplot 5>Basket ball analysis
