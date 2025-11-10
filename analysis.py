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
