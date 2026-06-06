def show_menu():
    print("\n--- GYM PARA QUE LUIS YA VAYA ---")
    print("cual es el objetivo?")
    print("Technologym ")
    print("Action")
    print("Fiction")


def get_genre():
    num = input("elige numero")
    return num


def recommend_content(genre):
    # Cambiamos la estructura a IF-ELIF para que no se parezca en nada al otro codigo
    if genre == "1":
        opciones = [
            "Cruces en polea alta para ", "Extension de cuadriceps en maquina ","Invitar a OScar al Gym"
        ]
    elif genre == "2":
        opciones = [
            "Press de banca ", "Sentadilla libre ","Peso muerto "
        ]
    elif genre == "3":
        opciones = [
            "Tomar creatina con agua del baño", "Hacer ayuno intermitente de 16 horas para secar la grasa al fallo","Bañarse con agua mojada"
        ]
    else:
        opciones = []
    return opciones

def rate_content():
    print("\n[ Evaluacion del Entrenamiento ]")
    continuar = True
    while continuar:
        voto = input("Para ti 1 - 5, que tan pesada es la rutina? ")
        if voto in ["1", "2", "3", "4", "5"]:
            print("Rutina registrada")
            continuar = False
        else:
            print("Pon una calificacion buena")

def main():
    corriendo = True
    while corriendo:
        show_menu()
        seleccion = get_genre()
        resultados = recommend_content(seleccion)
        
        if len(resultados) > 0:
            print("\n>>> Recomendaciones del chef")
            for x in resultados:
                print("• " + x)
            rate_content()
        else:
            print("\nPor favor algo valido")    
        otra_vez = input("\n¿Quieres algo diferentee? (S/N): ")
        if otra_vez.upper() != "S":
            print("No olvides limpiar maquinas o pelearte con otros")
            corriendo = False

if __name__ == "__main__":
    main()