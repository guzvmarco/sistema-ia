def predecir(datos):
    return {
        "status": "ok",
        "prediccion": [x * 2 for x in datos]
    }

if __name__ == "__main__":
    muestra = [1.2, 3.4, 0.8]
    print("API simulada activa")
    print("Resultado:", predecir(muestra))