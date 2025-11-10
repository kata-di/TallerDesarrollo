from data_loader import load_data
from analysis import dropout_rate, porcentajeCausa
if __name__ == "__main__":
    data = load_data()
    rate = dropout_rate(data)
    print(f"Dropout rate: {rate}%")
    porcCausa = porcentajeCausa(data)
    print(f"El porcentaje de la causa de deserción más común y su nombre es: {porcCausa} respectivamente")