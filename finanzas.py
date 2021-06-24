import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt


def cambiar_int(month):
    if df[month].dtype != int:
        df[month] = df[month].astype(str).astype(int)
        return df[month]



# LEER ARCHIVO CSV
try:
    df = pd.read_csv("finanzas2020corregido.csv")
except:
    print("No se ha encontrado ningún archivo para leer")
else:
    lista =["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    numero_meses = len(df.columns)
    numero_filas = len(df)
    if numero_meses == 12 and numero_filas >= 1:
        print("Archivo encontrado")
        print()
        print(df.head())

        # CAMBIAR DATOS DE OBJECT A INT
        try:
            for m in lista:
                cambiar_int(m)
        except:
            print("Error de tipo de datos: Compruebe que todos los datos seán numericos")
        else:
 
            # CALCULAR LA SUMATORIA DE TODOS LOS VALORES DE CADA MES
            ene = df["Enero"].sum()
            feb = df["Febrero"].sum()
            mar = df["Marzo"].sum()
            apr = df["Abril"].sum()
            may = df["Mayo"].sum()
            jun = df["Junio"].sum()
            jul = df["Julio"].sum()
            aug = df["Agosto"].sum()
            sep = df["Septiembre"].sum()
            octu = df["Octubre"].sum()
            nov = df["Noviembre"].sum()
            dec = df["Diciembre"].sum()


            print()
            # CREANDO UN DIC CON LA SUMATORIA DE CADA MES
            year = {"enero":ene, "febrero":feb, "marzo":mar, "abril": apr, "mayo":may, "junio":jun, "julio":jul, "agosto":aug, "septiembre":sep, 
                    "octubre":octu, "noviembre":nov, "diciembre":dec}
            print("Sumatoria de cada mes")
            print(year)


            print()
            # SELECCIONANDO EL MES CON EL MENOR VALOR (GASTADO MAS)
            gastado_mas = min(year.values())
            print("Maximo gasto: ",gastado_mas)
            for key, value in year.items():
                if gastado_mas == value:
                    print("El mes que hubo mas gasto: ",key)


            print()
            # SELECCIONANDO EL MES CON EL MAYOR VALOR (AHORRADO MAS)
            ahorrado_mas = max(year.values())
            print("Maximo ahorro: ",ahorrado_mas)
            for key, value in year.items():
                if ahorrado_mas == value:
                    print("El mes que hubo mas ahorro :",key)


            print()
            # CALCULANDO EL TOTAL DE GASTO DE CADA MES
            eg = 0
            for i in df["Enero"]:
                if i < 0:
                    eg = eg + i

            fg = 0
            for i in df["Febrero"]:
                if i < 0:
                    fg = fg + i

            mg = 0
            for i in df["Marzo"]:
                if i < 0:
                    mg = mg + i

            ag = 0
            for i in df["Abril"]:
                if i < 0:
                    ag = ag + i

            myg = 0
            for i in df["Mayo"]:
                if i < 0:
                    myg = myg + i

            jg = 0
            for i in df["Junio"]:
                if i < 0:
                    jg = jg + i

            jlg = 0
            for i in df["Julio"]:
                if i < 0:
                    jlg = jlg + i

            ag = 0
            for i in df["Agosto"]:
                if i < 0:
                    ag = ag + i

            ag = 0
            for i in df["Agosto"]:
                if i < 0:
                    ag = ag + i

            sg = 0
            for i in df["Septiembre"]:
                if i < 0:
                    sg = sg + i

            og = 0
            for i in df["Octubre"]:
                if i < 0:
                    og = og + i

            ng = 0
            for i in df["Noviembre"]:
                if i < 0:
                    ng = ng + i

            dg = 0
            for i in df["Diciembre"]:
                if i < 0:
                    dg = dg + i

            gasto_mes = [eg,fg,mg,ag,myg,jg,jlg,ag,sg,og,ng,dg]
            print("Sumatoria de gastos por cada mes")
            print(gasto_mes)


            print()
            # MEDIA DE GASTO AL AÑO
            media_gasto = statistics.mean(gasto_mes)
            print("La media de gasto al año es:")
            print(media_gasto)

            print()
            # GASTO TOTAL A LO LARGO DEL AÑO
            gasto_total = sum(gasto_mes)
            print("Gasto total a lo largo del año")
            print(gasto_total)

            print()
            # INGRESOS POR MES
            ei = ene - eg
            fi = feb - fg
            mi = mar - mg
            ai = apr - ag
            myi = may - myg
            ji = jun - jg
            jli = jul - jlg
            ai = aug - ag
            si = sep - sg
            oi = octu - og
            ni = nov - ng
            di = dec - dg
            ingreso_mes = [ei,fi,mi,ai,myi,ji,jli,ai,si,oi,ni,di]
            ingreso_total = sum(ingreso_mes)
            print("Sumatoria de ingresos por mes:")
            print("enero ",ei, "febrero ", fi, "marzo ", mi, "abril ", ai, "mayo ", myi, "junio ", ji, "julio ", jli, "agosto ", ai, "septiembre ", si, 
                    "octubre ", oi, "noviembre ", ni, "diciembre ", di)
            print()
            print("El ingreso total al año:")
            print(ingreso_total)

            print()
            # GRAFICO INGRESOS / GASTOS AL AÑO
            tabla = pd.DataFrame({"Mes":["enero", "febrero" , "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
                                        "noviembre", "diciembre"],
                                "Ingreso":[ei,fi,mi,ai,myi,ji,jli,ai,si,oi,ni,di],
                                "Gasto":[eg,fg,mg,ag,myg,jg,jlg,ag,sg,og,ng,dg]}) 
            print("Dataframe para el grafico:")
            print(tabla)

            ax = plt.gca()
            tabla.plot(kind="bar", x="Mes", y="Ingreso", ax=ax)
            tabla.plot(kind="bar", x="Mes", y="Gasto", color="red", ax=ax)
            plt.xlabel("Meses")
            plt.ylabel("Ingresos / Gastos")
            plt.show()

    else:
        print("Error de archivo: No hay 12 meses en el archivo o falta contenido en algún mes")









