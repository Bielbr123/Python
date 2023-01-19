# Lembrar que eu retirei os espaços dos elementos que só possuem uma letra
# Isso pode dar problema, depois eu devo voltar esses espaços, e retirar pelo python!

ELEM=("H","He",                                                                       
"Li","Be","B ","C","N","O","F ","Ne",                                         
"Na","Mg","Al","Si","P","S ","Cl","Ar",                                         
"K ","Ca","Sc","Ti","V ","Cr","Mn","Fe","Co","Ni","Cu","Zn",                     
"Ga","Ge","As","Se","Br","Kr",                                                  
"Rb","Sr","Y ","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd",                     
"In","Sn","Sb","Te","I","Xe",                                                   
"Cs","Ba",                                                                       
"La","Ce","Pr","Nd","Pm","Sm","Eu",                                              
"Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu",                                         
"Hf","Ta","W ","Re","Os","Ir","Pt","Au","Hg",                                     
"Tl","Pb","Bi","Po","At","Rn",                                                   
"Fr","Ra","Ac","Th","Pa","U ","Np","Pu","Am",                                    
"Cm")

RAIOCOV=(0.310,0.280,                                                                     
1.280,0.960,0.840,0.760,0.710,0.660,0.570,0.580,                                 
1.660,1.410,1.210,1.110,1.070,1.050,1.020,1.060,                                 
2.030,1.760,1.700,1.600,1.530,1.390,1.500,1.420,1.380,1.240,1.320,1.220,         
1.220,1.200,1.190,1.200,1.200,1.160,                                             
2.200,1.950,1.900,1.750,1.640,1.540,1.470,1.460,1.420,1.390,1.450,1.440,         
1.420,1.390,1.390,1.380,1.390,1.400,                                             
2.440,2.150,                                                                     
2.070,2.040,2.030,2.010,1.990,1.980,1.980,                                       
1.960,1.940,1.920,1.920,1.890,1.900,1.870,1.870,                                 
1.750,1.700,1.620,1.510,1.440,1.410,1.360,1.360,1.320,                           
1.450,1.460,1.480,1.400,1.500,1.500,                                             
2.600,2.210,2.150,2.060,2.000,1.960,1.900,1.870,1.800,                           
1.690)

elem_one = [] 
for elemento in ELEM:
    a = elemento.replace(" ", "")
    elem_one.append(a)
#print(elem_one)
elem_raio_dict=dict(zip(elem_one, RAIOCOV))

if __name__ == "__main__":
    pass
