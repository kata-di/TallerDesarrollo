def dropout_rate(df):
    total = len(df)
    dropped = len(df[df["status"] == "Dropped"])
    rate = dropped / total * 100
    return round(rate, 2)
def porcentajeCausa(df):
    salida = {}
    dropped = len(df[df["status"] == "Dropped"])
    family = len(df[df["cause"] == "Family"])
    financial = len(df[df["cause"] == "Financial"])
    academic = len(df[df["cause"] == "Academic"])
    rateFam = family / dropped * 100   
    rateFi = financial / dropped * 100
    rateAc = academic / dropped * 100
    if rateFam == rateFi and rateFi == rateAc:
        salida = {rateAc, "All"}
    if rateFam > rateFi and rateFi > rateAc:
        salida = {rateFam, "Family"}
    if rateFi > rateFam and rateFam > rateAc:
        salida = {rateFi, "Financial"}
    if rateAc > rateFam and rateFam > rateFi:
        salida = {rateAc,"Academic"}
    if rateFam > rateAc and rateAc > rateFi:
        salida = {rateFam, "Family"}
    if rateFi > rateAc and rateAc > rateFam:
        salida = {rateFi, "Financial"}
    if rateAc > rateFi and rateFi > rateFam:
        salida = {rateAc, "Academic"}
    if rateFam > rateAc and rateAc > rateFi:
        salida = {rateFam, "Family"}
    if rateFi > rateAc and rateAc > rateFam:
        salida = {rateFi, "Financial"}
    if rateAc > rateFi and rateFi > rateFam:
        salida = {rateAc, "Academic"}

    return salida

def porcCarreras(df):
    lCarreras = df["career"]
    vistos = []
    salida = {}
    salidas = []
    for carr in lCarreras:
        if carr not in vistos:
            vistos.append(carr)
            total = len(df[df["career"] == carr])
            if len(df[(df["status"] == "Dropped")] != 0):
                l = len(df[(df["status"] == "Dropped") & (df["career"] == carr)])
                rate = l/total*100
                salida = {carr, rate}
                salidas.append(salida)
            else: 
                salida = {carr, 0}
                salidas.append(salida)

    return salidas