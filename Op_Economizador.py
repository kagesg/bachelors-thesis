##------------------------------Importando bibliotecas------------------------------##
from math import log, pow, pi
import pandas as pd
import numpy as np
import timeit

#Vaiável para cálculo do tempo de processamento
inicio = timeit.default_timer()

##------------------------------Tabelas------------------------------##
    #Propriedades termofísicas água
agua_array = [["Temperatura","Pressão","Volume específico"," ","Calor de Vaporização","Calor específico"," ","Viscosidade dinâmica"," ","Condutividade térmica"," ","Numero de Prandtl"," ","Tensão superficial","Coeficiente de expansão"],
	["T","p","vf*10^3","vg","hfg","cpf","cpg","uf*10^6","ug*10^6","kf*10^3","kg*10^3","Prf","Prg","Sigmaf*10^3","Betaf*10^6"],
	["[K]","[bars]","[m³/kg]","[m³/kg]","[kJ/kg]","[kJ/(kg*K)]","[kJ/(kg*K)]","[N*s/m²]","[N*s/m²]","[W/(m*K)]","[W/(m*K)]"," "," ","[N/m]","[K^-1]"],
	[273.15,0.00611,1.000,206.3,2502,4.217,1.854,1750,8.02,569,18.20,12.99,0.815,75.5,-68.05],
	[275,0.00697,1.000,181.7,2497,4.211,1.855,1652,8.09,574,18.30,12.22,0.817,75.3,-32.74],
	[280,0.00990,1.000,130.4,2485,4.198,1.858,1422,8.29,582,18.60,10.26,0.825,74.8,46.04],
	[285,0.01387,1.000,99.4,2473,4.189,1.861,1225,8.49,590,18.90,8.81,0.833,74.3,114.1],
	[290,0.01917,1.001,69.7,2461,4.184,1.864,1080,8.69,598,19.30,7.56,0.841,73.7,174.0],
	[295,0.02617,1.002,51.94,2449,4.181,1.868,959,8.89,606,19.50,6.62,0.849,72.7,227.5],
	[300,0.03531,1.003,39.13,2438,4.179,1.872,855,9.09,613,19.60,5.83,0.857,71.7,276.1],
	[305,0.04712,1.005,29.74,2426,4.178,1.877,769,9.29,620,20.10,5.20,0.865,70.9,320.6],
	[310,0.06221,1.007,22.93,2414,4.178,1.882,695,9.49,628,20.40,4.62,0.873,70.00,361.9],
	[315,0.08132,1.009,17.82,2402,4.179,1.888,631,9.69,634,20.70,4.16,0.883,69.2,400.4],
	[320,0.10530,1.011,13.98,2390,4.180,1.895,577,9.89,640,21.00,3.77,0.894,68.3,436.7],
	[325,0.13510,1.013,11.06,2378,4.182,1.903,528,10.09,645,21.30,3.42,0.901,67.5,471.2],
	[330,0.17190,1.016,8.82,2366,4.184,1.911,489,10.29,650,21.70,3.15,0.908,66.6,504.0],
	[335,0.21670,1.018,7.09,2354,4.186,1.920,453,10.49,656,22.00,2.88,0.916,65.8,535.5],
	[340,0.27130,1.021,5.74,2342,4.188,1.930,420,10.69,660,22.30,2.66,0.925,64.9,566.0],
	[345,0.33720,1.024,4.683,2329,4.191,1.941,389,10.89,664,22.60,2.45,0.933,64.1,595.4],
	[350,0.41630,1.027,3.846,2317,4.195,1.954,365,11.09,668,23.00,2.29,0.942,63.2,624.2],
	[355,0.51000,1.03,3.180,2304,4.199,1.968,343,11.29,671,23.30,2.14,0.951,62.3,652.3],
	[360,0.62090,1.034,2.645,2291,4.203,1.983,324,11.49,674,23.70,2.02,0.960,61.4,697.9],
	[365,0.75140,1.038,2.212,2278,4.209,1.999,306,11.69,677,24.10,1.91,0.969,60.5,707.1],
	[370,0.90400,1.041,1.861,2265,4.214,2.017,289,11.89,679,24.50,1.80,0.978,59.5,728.7],
	[373.15,1.01330,1.044,1.679,2257,4.217,2.029,279,12.02,680,24.80,1.76,0.984,58.9,750.1],
	[375,1.08150,1.045,1.574,2252,4.220,2.036,274,12.09,681,24.90,1.70,0.987,58.6,761],
	[380,1.28690,1.049,1.337,2239,4.226,2.057,260,12.29,683,25.40,1.61,0.999,57.6,788],
	[385,1.52330,1.053,1.142,2225,4.232,2.080,248,12.49,685,25.80,1.53,1.004,56.6,814],
	[390,1.79400,1.058,0.980,2212,4.239,2.104,237,12.69,686,26.30,1.47,1.013,55.6,841],
	[400,2.45500,1.067,0.731,2183,4.256,2.158,217,13.05,688,27.20,1.34,1.033,53.6,896],
	[410,0.33020,1.077,0.553,2153,4.278,2.221,200,13.42,688,28.20,1.24,1.054,51.5,952],
	[420,0.43700,1.088,0.425,2123,4.302,2.291,185,13.79,688,29.80,1.12,1.075,49.4,1010],
	[430,0.56990,1.099,0.331,2001,4.331,2.369,173,14.14,685,30.40,1.09,1.100,47.2," "],
	[440,7.33300,1.11,0.261,2059,4.36,2.46,162,14.5,682,31.70,1.04,1.12,45.1," "],
	[450,9.31900,1.123,0.208,2024,4.4,2.56,152,14.85,678,33.10,0.99,1.14,42.9," "],
	[460,11.71000,1.137,0.167,1989,4.44,2.68,143,15.19,673,34.60,0.95,1.17,40.7," "],
	[470,14.55000,1.152,0.136,1951,4.48,2.79,136,15.54,667,36.30,0.92,1.20,38.5," "],
	[480,17.90000,1.167,0.111,1912,4.53,2.94,129,15.88,660,38.10,0.89,1.23,36.2," "],
	[490,21.83000,1.184,0.0922,1870,4.59,3.1,124,16.23,651,40.10,0.87,1.25,33.9," "],
	[500,26.40000,1.203,0.0766,1825,4.66,3.27,118,16.59,642,42.30,0.86,1.28,31.6," "],
	[510,31.66000,1.222,0.0631,1779,4.74,3.47,113,16.95,631,44.70,0.85,1.31,29.3," "],
	[520,37.70000,1.244,0.0525,1730,4.84,3.70,108,17.33,621,47.50,0.84,1.35,26.9," "],
	[530,44.58000,1.268,0.0445,1679,4.95,3.96,104,17.72,608,50.60,0.85,1.39,24.5," "],
	[540,52.38000,1.294,0.0375,1622,5.08,4.27,101,18.1,594,54.00,0.86,1.43,22.1," "],
	[550,61.19000,1.323,0.0000,1564,5.24,4.64,97,18.6,580,58.30,0.87,1.47,19.7," "],
	[560,71.08000,1.355,0.0269,1499,5.43,5.09,94,19.1,563,63.70,0.90,1.52,17.3," "],
	[570,82.16000,1.392,0.0228,1429,5.68,5.67,91,19.7,548,76.70,0.94,1.59,15.0," "],
	[580,94.51000,1.433,0.0193,1353,6.00,6.40,88,20.4,528,76.70,0.99,1.68,12.8," "],
	[590,108.30000,1.482,0.0163,1274,6.41,7.35,84,21.5,513,84.10,1.05,1.84,10.5," "],
	[600,123.50000,1.541,0.0137,1176,7.00,8.75,81,2.27,497,92.90,1.14,2.15,8.4," "],
	[610,137.30000,1.612,0.0115,1068,7.85,11.1,77,24.1,467,103,1.3,2.60,6.3," "],
	[620,159.10000,1.705,0.0094,941,9.15,15.4,72,25.9,444,114,1.52,3.46,4.5," "],
	[625,169.10000,1.778,0.0085,858,10.6,18.3,70,27,430,121,1.65,4.20,3.5," "],
	[630,179.70000,1.856,0.0075,781,12.6,22.1,67,28,412,130,2.0,4.80,2.6," "],
	[635,190.90000,1.935,0.0066,683,16.4,27.6,64,30,392,141,2.7,6.00,1.5," "],
	[640,202.70000,2.075,0.0057,560,26,42.0,59,32,367,155,4.2,9.60,0.8," "],
	[645,215.20000,2.351,0.0045,361,90," ",54,37,331,178,12,26.00,0.1," "],
	[647.3,221.20000,3.17,0.0032,0," "," ",45,45,238,238," "," ",0.0," "]]
agua_df = pd.DataFrame(agua_array)
agua_df = agua_df.loc[3:]
agua_df = agua_df.reset_index()
agua_df.index = range(0, len(agua_df))
agua_df = agua_df.replace(" ",0)
agua_df = agua_df.astype(float, errors = 'raise')

    #Temperatura de saturação água em função da pressão
agua_sat_array = [["Pressão","Temperatura"],
    ["P","T"],
    ["[bar]","[ºC]"],
    [0.04,28.96],
    [0.06,36.16],
    [0.08,41.51],
    [0.1,45.81],
    [0.2,60.06],
    [0.3,69.1],
    [0.4,75.87],
    [0.5,81.33],
    [0.6,85.94],
    [0.7,89.95],
    [0.8,93.5],
    [0.9,96.71],
    [1,99.63],
    [1.5,111.4],
    [2,120.2],
    [2.5,127.4],
    [3,133.6],
    [3.5,138.9],
    [4,143.6],
    [4.5,147.9],
    [5,151.9],
    [6,158.9],
    [7,165],
    [8,170.4],
    [9,175.4],
    [10,179.9],
    [15,198.3],
    [20,212.4],
    [25,224],
    [30,233.9],
    [35,242.6],
    [40,250.4],
    [45,257.5],
    [50,264],
    [60,275.6],
    [70,285.9],
    [80,295.1],
    [90,303.4],
    [100,311.1],
    [110,318.2],
    [120,324.8],
    [130,330.9],
    [140,336.8],
    [150,342.2],
    [160,347.4],
    [170,352.4],
    [180,357.1],
    [190,361.5],
    [200,365.8],
    [220.9,374.1]]
agua_sat_df = pd.DataFrame(agua_sat_array)
agua_sat_df = agua_sat_df.loc[3:]
agua_sat_df = agua_sat_df.reset_index()
agua_sat_df.index = range(0, len(agua_sat_df))
agua_sat_df = agua_sat_df.replace(" ",0)
agua_sat_df = agua_sat_df.astype(float, errors = 'raise')

    #Propriedades termofísicas ar
ar_array = [["Temperatura","Densidade","Calor específico","Viscosidade dinâmica","Viscosidade cinemática","Condutividade térmica","Viscosidade","Prandtl"],
    ["T","p","cp","u*10^7","v*10^6","k*10^3","u*10^6","Pr"],
    ["[K]","[Kg/m³]","[kJ/(kg*K)]","[N*s/m²]","[m²/s]","[W/(m*K)]","[m²/s]"," "],
    [100,3.5562,1.032,71.1,2.000,9.34,2.54,0.786],
    [150,2.3364,1.012,103.4,4.426,13.8,5.84,0.758],
    [200,1.7458,1.007,132.5,7.590,18.1,10.3,0.737],
    [250,1.3947,1.006,159.6,11.44,22.3,15.9,0.72],
    [300,1.1614,1.007,184.6,15.89,26.3,22.5,0.707],
    [350,0.995,1.009,208.2,20.92,30,29.9,0.7],
    [400,0.8711,1.014,230.1,26.41,33.8,38.3,0.69],
    [450,0.774,1.021,250.7,32.39,37.3,47.2,0.686],
    [500,0.6964,1.030,270.1,38.79,40.7,56.7,0.684],
    [550,0.6329,1.040,288.4,45.57,43.9,66.7,0.683],
    [600,0.5804,1.051,305.8,52.69,46.9,76.9,0.685],
    [650,0.5356,1.063,322.5,60.21,49.7,87.3,0.69],
    [700,0.4975,1.075,338.8,68.10,52.4,98,0.695],
    [750,0.4643,1.087,354.6,76.37,54.9,109,0.702],
    [800,0.4354,1.099,369.8,84.93,57.3,120,0.709],
    [850,0.4097,1.110,384.3,93.80,59.6,131,0.716],
    [900,0.3868,1.121,398.1,102.9,62,143,0.72],
    [950,0.3666,1.131,411.3,112.2,64.3,155,0.723],
    [1000,0.3482,1.141,424.4,121.9,66.7,168,0.726],
    [1100,0.3166,1.159,449,141.8,71.5,195,0.728],
    [1200,0.2902,1.175,473,162.9,76.3,224,0.728],
    [1300,0.2679,1.189,496,185.1,82,257,0.719],
    [1400,0.2488,1.207,530,213,91,303,0.703],
    [1500,0.2322,1.230,557,240,100,350,0.685],
    [1600,0.2177,1.248,584,268,106,390,0.688],
    [1700,0.2049,1.267,611,298,113,435,0.685],
    [1800,0.1935,1.286,637,329,120,482,0.683],
    [1900,0.1833,1.307,663,362,128,534,0.677],
    [2000,0.1741,1.337,689,396,137,589,0.672],
    [2100,0.1658,1.372,715,431,147,646,0.667],
    [2200,0.1582,1.417,740,468,160,714,0.655],
    [2300,0.1513,1.478,766,506,175,783,0.647],
    [2400,0.1448,1.558,792,547,196,869,0.63],
    [2500,0.1389,1.665,818,589,222,960,0.613],
    [3000,0.1135,2.726,955,841,486,1570,0.536]]
ar_df = pd.DataFrame(ar_array)
ar_df = ar_df.loc[3:]
ar_df = ar_df.reset_index()
ar_df.index = range(0, len(ar_df))
ar_df = ar_df.replace(" ",0)
ar_df = ar_df.astype(float, errors = 'raise')

    #Números de Nusselt região Anular e taxa de transferência de calor constante
Nu_array = [["Razão diâmetros","Nusselt"],
    [0,0],
    [0.05,17.81],
    [0.1,11.91],
    [0.2,8.499],
    [0.4,6.583],
    [0.6,5.912],
    [0.8,5.58],
    [1,5.385]]
Nu_df = pd.DataFrame(Nu_array)
Nu_df = Nu_df.loc[1:]
Nu_df = Nu_df.reset_index()
Nu_df.index = range(0, len(Nu_df))
Nu_df = Nu_df.replace(" ",0)
Nu_df = Nu_df.astype(float, errors = 'raise')

##------------------------------Variáveis gerais------------------------------##
    #Listas de operação de tipo de fluido, estado e escoamento
tipo_fluido = ["Agua", "Ar"]
escoamento = ["Interno-Circular","Interno-Anelar"]

    #Definindo array que serão armazenados os resultados
resultados_array = []

    #Definindo array para método interativo
n_m_1,n_temp_4 = ([] for i in range(2))

    #Nome das abas dos arquivos Excel
nome_tab = [['Temp_1_1','Temp_1_2','Temp_1_3','Temp_1_4','Temp_1_5','Temp_1_6'],
        ['Temp_3_1','Temp_3_2','Temp_3_3','Temp_3_4','Temp_3_5','Temp_3_6'],
        ['Press_1_1','Press_1_2','Press_1_3','Press_1_4','Press_1_5','Press_1_6']]

    #Nome dos arquivos Excel para cada simulação en funcão da variável de entrada
nome_result = ["Resultados_1.xlsx","Resultados_2.xlsx","Resultados_3.xlsx"]

#Definindo dicionário das colunas
dict_col = {0:'Temperatura entrada água',
                1:'Temperatura saída água',
                2:'Temperatura entrada ar',
                3:'Temperatura saída ar',
                4:'Vazão água',
                5:'Vazão do ar',
                6:'Delta_Tml',
                7:'Reynolds ar',
                8:'Reynolds água',
                9:'Nusselt ar',
                10:'Nusselt água',
                11:'Coef. convectivo ar',
                12:'Coef. convectivo água',
                13:'Calor ar',
                14:'Calor água',
                15:'Calor coef. global',
                16:'Pressão ar',
                17:'Pressão água'}

#Definindo dicionário das unidades
dict_unity = {'Temperatura entrada água':['[°C]'],
                'Temperatura saída água':['[°C]'],
                'Temperatura entrada ar':['[°C]'],
                'Temperatura saída ar':['[°C]'],
                'Vazão água':['[kg/h]'],
                'Vazão do ar':['[kg/h]'],
                'Delta_Tml':['[]'],
                'Reynolds ar':['[]'],
                'Reynolds água':['[]'],
                'Nusselt ar':['[]'],
                'Nusselt água':['[]'],
                'Coef. convectivo ar':['[W/m²*K]'],
                'Coef. convectivo água':['[W/m²*K]'],
                'Calor ar':['[W]'],
                'Calor água':['[W]'],
                'Calor coef. global':['[W]'],
                'Pressão ar':['[bar]'],
                'Pressão água':['[bar]']}

##------------------------------Variáveis dimensionais------------------------------##
    #Diâmetros do tubo interno
de_i = 33.40*(pow(10,-3))
esp_i = 3.38*(pow(10,-3))
di_i = de_i - 2*(esp_i)     #26.64 mm

    #Diâmetros do tubo externo
de_e = 48.30*(pow(10,-3))
esp_e = 3.38*(pow(10,-3))
di_e =  de_e - 2*(esp_e)

    #Comprimento efetivo em [m]
lef_i = 2400*(pow(10,-3))

    #Razão entre diâmetros interno e externo da região anular
raz_diam = de_i/di_e

    #Diâmetro hidráulico da região anular
d_h_e = di_e - de_i
    #Área de troca interno anular
a_troca = (pi*de_i*lef_i)
    #Área de troca interno gás
a_troca_q = (pi*di_i*lef_i)
    #Área de troca interno água
a_troca_f = a_troca
    #Área transversal gás
a_transv_q = (pi*pow(di_i,2)/4)
    #Área transversal água
a_transv_f = (pi*(pow(di_e,2)-pow(de_i,2))/4)

##------------------------------Funções------------------------------##

#Função para criar lista com intervalo de valores (aceita float como passo)
""" Detalhes dos parâmetros:  
    inicio = Valor inicial do intervalo
    fim = Valor final do intervalo
    passo = Valor do passo do intervalo (n deve ser 0)
    n = Quantidade de divisões do intervalo
"""
def list_range(inicio,fim,passo,n):
    i = 0
    list = []

    if n != 0:
        end = n
        passo = (fim - inicio) / (n)
    elif n == 0:
        end = (fim - inicio) / passo
    else:
        return 0
    
    while i <= end:
        s = (inicio) + (passo * i)
        list.append(s)
        i += 1
    return list

#Função para busca e interpolação:
""" Detalhes dos parâmetros:
    df = Dataframe para realizar as buscas
    valor = Valor a ser encontrado ou interpolado
"""
def interpolacao(df,valor):
    for i in range(0,len(df.index)):
        valor_teste = df.loc[i,0]
        #Teste
            #Se o valor desejado se encontra na tabela, retorna a linha referente a ele
        if valor_teste == valor:
            x0 = 0
            x1 = 0
            y = pd.DataFrame(df.loc[i]).T
            break
            #Se o valor não for encontrado, realiza a interpolação
        elif valor_teste > valor:
            x1 = valor_teste
            y1 = pd.DataFrame(df.loc[i]).T
            y = pd.DataFrame(y0.loc[j] + (y1.loc[i] - y0.loc[j]) * ((valor - x0) / (x1 - x0))).T
            break
        #Definindo valores para a sequencia do loop
        x0 = valor_teste
        y0 = pd.DataFrame(df.loc[i]).T
        j = i
    #Zera o índice da linha
    y = y.set_axis([0],axis=0)
    return y

#Função para encontrar a temperatura de saturação em função da pressão de operação da água (Interpolação)
""" Detalhes dos parâmetros:
    pressao = Valor em bar da pressão que se quer retornar a temperatura de saturação
"""
def temp_sat(pressao):
    df = agua_sat_df
    y = interpolacao(df,pressao)
    y = y.drop(["index"],axis=1)
    y = y.loc[0].tolist()
    return y[1]

#Função para os cálulos necessários para encontrar resultados
""" Detalhes dos parâmetros:
    vazq_entra = Vazão de entrada do fluido quente em [kg/s]
    vazf_entra = Vazão de entrada do fluido frio em [kg/s]
    Tq_entra = Temperatura de entrada do fluido quente em [°C]
    Tq_sai = Temperatura de saída do fluido quente em [°C]
    Tf_entra = Temperatura de entrada do fluido frio em [°C]
    Tf_sai = Temperatura de saída do fluido frio em [°C]
    p_3 = Pressão absoluta do fluido quente [bar]
    p_1 = Pressão absoluta do fluido frio [bar]
"""
def calculo(vazq_entra,vazf_entra,Tq_entra,Tq_sai,Tf_entra,Tf_sai,p_q,p_f):
    #Função para encontrar as propriedades termofisicas dos fluidos:
    """ Detalhes dos parâmetros:
        tipo_fluido = Qual fluido de interesse (CONSULTAR VARIÁVEL "tipo_fluido" PARA VER OPÇÕES)
        temp_med = Temperatura média/fluido a se retornar as propriedades termofísicas em [K]
    """
    #Ordem da lista propriedades termofísicas retornado:
    #[densidade,calor específico,viscosidade absoluta,viscosidade cinemática,condutividade térmica,Prandtl,difusividade térmica]
    def prop_term(tipo_fluido,temp_med):
        p = list()
        u = 0
        #Seleção da tabela
        if tipo_fluido == "Agua":
            df = agua_df

        elif tipo_fluido == "Ar":
            df = ar_df
        #Procura e interpolação (quando necessário)
        y = interpolacao(df,temp_med)
        #Organização e conversão das propriedades para o SI
        if tipo_fluido == "Agua":
            y = y.drop(["index",0,1,3,4,6,8,10,12,13,14], axis = 1)
            y = y.set_axis([0,1,2,3,4], axis = 1)
            for i in range(0,len(y.columns)):
                p.append(y.at[0,i])
            p.insert(3,0)
            p.insert(7,0)
            p[0] = 1 / (p[0] * pow(10,-3))
            p[1] = p[1] * pow(10,3)
            p[2] = p[2] * pow(10,-6)
            p[4] = p[4] * pow(10,-3)

        elif tipo_fluido == "Ar":
            y = y.drop(["index",0],axis = 1)
            y = y.set_axis([0,1,2,3,4,5,6],axis = 1)
            for i in range(0,len(y.columns)):
                p.append(y.at[0,i])
            u = p[6]
            p.remove(u)
            p.insert(5,u)
            p[1] = p[1] * pow(10,3)
            p[2] = p[2] * pow(10,-7)
            p[3] = p[3] * pow(10,-6)
            p[4] = p[4] * pow(10,-3)
            p[6] = p[6] * pow(10,-6)
        return p        

    #Cálculo MDLT
    """ Detalhes dos parâmetros:  
        Tq_entra = Temperatura de entrada do fluido quente em [°C]
        Tq_sai = Temperatura de saída do fluido quente em [°C]
        Tf_entra = Temperatura de entrada do fluido frio em [°C]
        Tf_sai = Temperatura de saída do fluido frio em [°C]
    """
    def MDLT(Tq_entra,Tq_sai,Tf_entra,Tf_sai):
        #Configuração contracorrente
        delta_T1 = Tq_entra - Tf_sai
        delta_T2 = Tq_sai - Tf_entra
        delta_Tml = (delta_T2 - delta_T1) / log(delta_T2 / delta_T1)
        return delta_Tml

    #Cálculo Reynolds
    """ Detalhes dos parâmetros:     
        densidade = Densidade mássica do fluido em [kg/m³]
        visc_abs = Viscosidade absoluta do fluido em [N*s/m²]
        diametro = Diâmetro da seção transversal ou diâmetro hidáulico do escoamento em [m]
        a_transv = Área transversal do escoamento em [m²]
        taxa_massica = Vazão mássica do escoamento em [kg/s]
        vel_media = Velocidade média do escoamento em [m/s] (se 0, a função realiza o cálculo do mesmo através dos parâmetros anteriores)
    """
    def reynolds(densidade, visc_abs, diametro, a_transv, taxa_massica, vel_media):
        #Calcula a velociade média do fluido
        if vel_media == 0:
            vel_media = (taxa_massica) / (densidade * a_transv)
        #Cálculo do numero de reynolds
        Re = (densidade * vel_media * diametro) / (visc_abs)
        return Re

    #Cálculo Nusselt (Laminar ou Turbulento)
    """ Detalhes dos parâmetros:  
        escoamento = Região de escoamento (CONSULTAR VARIÁVEL "escoamento" PARA VER OPÇÕES)
        Re = Número de Reynolds do escoamento
        Pr = Número de Prandtl do fluido em escoamento
        raz_diam = Razão dos diâmetros interno e externo da seção anular
    """
    def nusselt(escoamento,Re,Pr,raz_diam):
        #Escoamento Laminar
        if Re <= 2300.00:
            if escoamento == "Interno-Circular":
                Nud = 4.36
            
            elif escoamento == "Interno-Anelar":
                Nud = float(interpolacao(Nu_df,raz_diam).iloc[0][1])
            
        #Escoamento Turbulento
        elif Re > 2300.00:
            #Correlação Gnieslinski
            #0.5<=Pr<=200 \ 3000<=Re<=5000000
            f = pow((0.790*np.log(Re)-1.64),-2)
            Nud = ((f/8)*(Re-1000)*Pr)/(1+12.7*pow((f/8),(1/2))*(pow(Pr,(2/3))-1))
        return Nud

    #Cálculo coeficiente convectivo
    """ Detalhes dos parâmetros:
        Nud = Número de Nusselt do escoamento
        condutividade_termica = Condutividade térmica do fluido em [W/(m*K)]
        diametro = Diâmetro da seção transversal ou diâmetro hidáulico do escoamento em [m]
    """
    def coef_convec(Nud,condutividade_termica,diametro):
        h = Nud*condutividade_termica/diametro
        return h

    #Cálculo resistência Convecção + resistencia por incrustação
    """ Detalhes dos parâmetros:
        tipo_fluido = Qual fluido do escoamento (CONSULTAR VARIÁVEL "tipo_fluido" PARA VER OPÇÕES)
        h = Coeficiente convectivo médio do escoamento em [W/(m²*K)]
        a_troca = Área de troca térmica em [m²]
    """
    def res_conv(tipo_fluido,h,a_troca):
        if tipo_fluido == "Agua":
            R_f = 0.0001
        
        elif tipo_fluido == "Ar":
            R_f = 0.0004
        res_conv = R_f/a_troca + 1/(h*a_troca)
        return res_conv

    #Cálculo resistencia Condução
    """ Detalhes dos parâmetros:
        k_mat = Condutividade térmica do material em [W/(m*K)]
        di = Diâmetro interno do material em [m]
        de = Diâmetro externo do material em [m]
        L = Comprimento de troca térmica em [m]
    """
    def res_cond(k_mat,di,de,L):
        res_cond = log(de/di)/(2*pi*k_mat*L)
        return res_cond

    #Definição de variáveis
        #Array onde ficarão os resultados da simulação
    resultados = []

    #Calculando temperaturas médias dos fluidos e o deltaTml
        #Temperaturas médias dos fluidos
    temp_med_i = ((Tq_entra+Tq_sai)/2)+273
    temp_med_e = ((Tf_entra+Tf_sai)/2)+273
        #deltaTml
    delta_Tml = MDLT(Tq_entra,Tq_sai,Tf_entra,Tf_sai)

    #Propriedades termofísicas:
        #Gás de exaustão na temperatura média fluido (propriedades do ar)
    p_i = prop_term(tipo_fluido[1],temp_med_i)
        #Água na temperatura média fluido
    p_e = prop_term(tipo_fluido[0],temp_med_e)
        #Material na temperatura de superfície
    k_mat = 15.5

    #Número de Reynolds:
        #Tubo circular
    Re_i = reynolds(p_i[0],p_i[2],di_i,a_transv_q,vazq_entra,0)
        #Anular
    Re_e = reynolds(p_e[0],p_e[2],d_h_e,a_transv_f,vazf_entra,0)

    #Número de Nusselt:
        #Tubo circular
    Nud_i = nusselt(escoamento[0],Re_i,p_i[5],0)
        #Anular
    Nud_e = nusselt(escoamento[1],Re_e,p_e[5],raz_diam)

    #Coeficiente convectivo
        #Tubo circular
    h_i = coef_convec(Nud_i,p_i[4],di_i)
        #Anular
    h_e = coef_convec(Nud_e,p_e[4],d_h_e)

    #Resistências:
        #Convectiva tubo ciruclar
    R_conv_i = res_conv(tipo_fluido[1],h_i,a_troca_q)
        #Condução do material do tubo
    R_cond = res_cond(k_mat,di_i,de_i,lef_i)
        #Convectiva anular
    R_conv_e = res_conv(tipo_fluido[0],h_e,a_troca_f)
        #Total (configuração em série)
    Rtot = R_conv_i + R_cond + R_conv_e

    #Taxa de transferência de calor através das resistência total
    q = (1/Rtot)*delta_Tml

    #Taxa de transferência de calor através das vazões mássicas e capacidade térmicas
        #Tubo circular
    q_i = vazq_entra*p_i[1]*abs(Tq_entra-Tq_sai)
        #Anular
    q_e = vazf_entra*p_e[1]*abs(Tf_sai-Tf_entra)

    #Criando lista e retornando o vetor com os resultados e as propriedades da região anular
    resultados.extend([Tf_entra,Tf_sai,Tq_entra,Tq_sai,vazf_entra*3600,vazq_entra*3600,delta_Tml,Re_i,Re_e,Nud_i,Nud_e,h_i,h_e,q_i,q_e,q,p_q,p_f])
    return resultados, p_e

##------------------------------SIMULAÇÃO------------------------------##

#Definindo intervalos de operação:
    #Temperatura de entrada da água em [°C]
temp_1_range = list_range(10,30,1,0)
    #Temperatura de entrada do gás em [°C]
temp_3_range = list_range(740,860,5,0)
    #Pressão de operação da água em [bar]
p_1_range = list_range(3,12,0.5,0)
#Variação de estados de entrada para simulação
    #Temperatura de entrada da água em [°C]
temp1_lim = [10,20,35] 
    #Temperatura de entrada do gás em [°C]
temp3_lim = [740,780,860]
    #Pressão de operação da água em [bar]
p1_lim = [3,5,12]
    #Criando lista a ser percorrida para a simulação (interativo)
temp_4_range = list_range(250,150,0,200)

#Laço para as variáveis principais
for cond in range(0,3,1):
    #Criando arquivo Excel para armazenar resultados
    writer = pd.ExcelWriter(nome_result[cond], engine='xlsxwriter')

        #Variando temperatura de entrada da água
    if cond == 0:
        var_prim = temp_1_range

        #Variando temperatura de entrada do gás
    elif cond == 1:
        var_prim = temp_3_range

        #Variando pressão da água
    elif cond == 2:
        var_prim = p_1_range 

    #Laço para as variáveis secundárias
    for sub_cond in range(0,6,1):

        ##----------Definindo variáveis de estado padrão----------##
            #Ponto 1 - Alimentação de água
        temp_1 = 25 #°C
        p_1 = 5 #bar
            #Valor para chute inicial da vazão mássica de água
        m_1 = 14 / (3600) #kg/s

            #Ponto 2 - Saída de água
        t_sat = 151.9 #°C (Tabela Shapiro p/ P = 5 bar)
        temp_2 = t_sat - 20 #°C
        p_2 = p_1 #bar
        m_2 = m_1 #kg/s

            #Ponto 3 - Alimentação de gás de exaustão
        temp_3 = 780 #°C
        p_3 = 1 #bar
        m_3 = 8.6 / (3600) #kg/s

            #Ponto 4 - Saída de gás de exaustão
        temp_4 = 400 #temp_3 #°C (valor arbitrário)
        p_4 = p_3 #bar
        m_4 = m_3 #kg/s
        
        #Limpando array de resultados
        resultados_array.clear()
        
        #Laço para a percorrer a lista de variáveis principais escolhidas:
        for j in var_prim:     
            ##----------Modos de operação----------##
                #Variando temperatura de entrada da água
            if cond == 0:
                temp_1 = j
                    #Variando pressão absoluta da água
                if sub_cond < 3:
                    p_1 = p1_lim[sub_cond]
                    t_sat = temp_sat(p_1)
                    temp_2 = t_sat - 20 #[°C]

                    #Variando temperatura de entrada do gás de exaustão
                elif sub_cond >= 3:
                    temp_3 = temp3_lim[sub_cond-3]
                
                #Variando temperatura de entrada do gás
            elif cond == 1:
                temp_3 = j
                    #Variando pressão absoluta da água
                if sub_cond < 3:
                    p_1 = p1_lim[sub_cond]
                    t_sat = temp_sat(p_1)
                    temp_2 = t_sat - 20 #[°C]

                    #Variando temperatura de entrada da água
                elif sub_cond >= 3:
                    temp_1 = temp1_lim[sub_cond-3]
                
                #Variando pressão da água
            elif cond == 2:
                p_1 = j
                t_sat = temp_sat(p_1)
                temp_2 = t_sat - 20 #[°C]
                    #Variando temperatura de entrada da água
                if sub_cond < 3:
                    temp_1 = temp1_lim[sub_cond]

                    #Variando temperatura de entrada do gás de exaustão
                elif sub_cond >= 3:
                    temp_3 = temp3_lim[sub_cond-3]

            #Laço para a variação da temperatura de saída do gás:
            for k in range(0,201,1):
                temp_4 = float(temp_4_range[k])
                #Realizando os cálculos e colhendo os resultados para determinada operação
                resultado, prop_e = calculo(m_3,m_1,temp_3,temp_4,temp_1,temp_2,p_3,p_1)

                #Condição de 1% de erro entre as taxas de transferência de calor do coef. global e pelo gás 
                if ((abs(resultado[15]-resultado[13])/resultado[15])*100<=1):
                    #Cálculo da vazão mássica da água para a solução encontrada                   
                    m_1_novo = (resultado[15] / (prop_e[1] * (temp_2 - temp_1))) #kg/s

                    #Adicionando em listas os valores de vazão mássica da água e temperatura de saída do gás, respectivamente:
                    n_m_1.append(m_1_novo)
                    n_temp_4.append(temp_4) #°C

            #Reset das variáveis de temperatura e vazão massica final encontradas
            temp_4_f = 0
            m_1_f = 0

            #Cálculo dos valores de temperatura e vazão mássica finais (Média simples dos valores encontrados e adicionados nas listas)
            temp_4_f = sum(n_temp_4) / len(n_temp_4)
            m_1_f = (sum(n_m_1) / len(n_m_1))

            #Cálculo final do resultado com temperatura e vazão mássica finais:
            resultado, prop_e = calculo(m_3,m_1_f,temp_3,temp_4_f,temp_1,temp_2,p_3,p_1)

            #Adição do resultado na tabela final:
            resultados_array.append(resultado)

            #Limpando listas de valores de soluções encontradas:
            n_m_1.clear()
            n_temp_4.clear()       
        
        #Criando tabela com resultados e adicionando em arquivo Excel
        resultados_df = pd.DataFrame(resultados_array)
        resultados_df = resultados_df.rename(columns = dict_col, inplace = False)
        df_un = pd.DataFrame(data=dict_unity)
        resultados_df_f = pd.concat([df_un, resultados_df])
        resultados_df_f.reset_index(drop=True, inplace=True)
        resultados_df_f.to_excel(writer,sheet_name = nome_tab[cond][sub_cond])

    #Salvando arquivo Excel
    writer.save()

#Vaiável para cálculo do tempo de processamento
fim = timeit.default_timer()
#Print do tempo de processamento em [s]
print ('duracao: %f seg' % (fim - inicio))