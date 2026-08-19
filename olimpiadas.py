import random

#simulador de olimpiadas
class Participante:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def __eq__(self,other: object)->bool:
        if isinstance(other,Participante):
            return self.nombre==other.nombre, self.pais==other.pais
        return False

    def __hash__(self)->int:
        return hash(self.nombre,self.pais)


class Olimpiadas:
    def __init__(self):
        self.eventos = []
        self.participantes = {}
        self.eventos_resultados = {}
        self.pais_resultados = {}

    #PRIMERA OPCION
    def registrar_evento(self):
        nombre_evento = input("Ingresa el nombre del evento: ")

        if(nombre_evento in self.eventos):
            print(f"EL evento {nombre_evento} ya existe")
        else:
            self.eventos.append(nombre_evento)
            print(f"Se creo el evento llamado {nombre_evento} correctamente")

    #SEGUNDA OPCION
    def registrar_participantes(self):

        if(not self.eventos):
            print("No hay eventos disponibles. Primero crea uno")
        else:
            nombre = input("Ingresa el nombre del participante: ")
            pais = input("Ingresa el pais del participante: ")
            participante = Participante(nombre,pais)

            print("Eventos disponibles")
            for index,evento in enumerate(self.eventos):
                print(f"{index+1}. {evento}")

            evento_escogido = int(input("Escoge un evento: "))-1

            if(evento_escogido >= 0 and evento_escogido < len(self.eventos)):
                evento = self.eventos[evento_escogido]

                if(evento in self.participantes and participante in self.participantes[evento]):
                    print(f"El participante {nombre} ya esta registrado en el evento {evento}")
                else:
                    if(evento not in self.participantes): #si no esta el evento en el diccionario de participantes
                        self.participantes[evento] = [] # se crea un arreglo del evento en el diccionario de participantes

                    self.participantes[evento].append(participante)
                    print(f"El participante {nombre} del pais {pais} se inscribio al evento {evento} correctamente.")
            else:
                print("Selecciona un evento disponible. El participante no se registro")

    #TERCERA OPCION
    def simular_evento(self):

        if( not self.eventos):
            print("No hay evento disponibles. Crea uno")
            return 
        
        for evento in self.eventos:
            if (len(self.participantes[evento]) < 3):
                print("Es necesario tener minimo 3 participantes por evento")
                return
            else:
                participante_evento = random.sample(list(self.participantes.items(),3))   #Escoge a tres participantes aleatorios
                random.shuffle(participante_evento)     #reordena los participantes

            oro,plata,bronce = participante_evento
            self.eventos_resultados = [oro,plata,bronce]

            self.actualizar_resultados_pais(oro.pais,"oro")
            self.actualizar_resultados_pais(plata.pais, "plata")
            self.actualizar_resultados_pais(bronce.pais,"bronce")

            print(f"Resultados del evento {evento}")
            print(f"Oro: {oro.nombre} {oro.pais}")
            print(f"Plata: {plata.nombre} {plata.pais}")
            print(f"Bronce: {bronce.nombre} {bronce.pais}")


    def actualizar_resultados_pais(self,pais,medalla):
        if(pais not in self.pais_resultados):
            self.pais_resultados[pais] = {"oro":0, "plata":0, "bronce":0}

        self.pais_resultados[pais][medalla] +=1 #Se pone el +1 para sumar la medalla

    # CUARTA OPCION
    def mostrar_reporte(self):
        if(self.eventos_resultados):

            print("INFORME DE RESULTADOS POR EVENTO")

            for evento, ganadores in self.eventos_resultados.items():
                print(f"Evento: {evento}")
                print(f"Resultados del evento {evento}")
                print(f"Oro: {ganadores[0].nombre} ({ganadores[0].pais})")
                print(f"Plata: {ganadores[1].nombre} ({ganadores[1].pais})")
                print(f"Bronce: {ganadores[2].nombre} ({ganadores[2].pais})")
        else:
            print("No hay reusltados a mostrar")


        if(self.pais_resultados):
            print("")
            print("INFORME DE RESULTADOS POR PAIS")

            for pais, medalla in sorted(self.pais_resultados.items() , key=lambda x:(x[1]["oro"], x[1]["plata"], x[1]["bronce"]),reverse=True):
                print(f"{pais}: Oro {medalla["oro"]}, Plata: {medalla["plata"]}, Bronce: {medalla["bronce"]}")

        else:
            print("NO hay medallas por pais")



#instancia
olimpiadas = Olimpiadas()



# MENU
opcion=0
while(opcion != 5):

    print("---- SIMULADOR DE OLIMPIADAS ----")
    print("1. Registrar evento")
    print("2. Registrar participante")
    print("3. Simular evento")
    print("4. Mostrar Reporte")
    print("5. Salir")

    opcion = int(input("Hoy quiero... "))


    if(opcion == 1):
        olimpiadas.registrar_evento()

    elif(opcion == 2):
        olimpiadas.registrar_participantes()

    elif(opcion == 3):
        olimpiadas.simular_evento()

    elif(opcion == 4):
        olimpiadas.mostrar_reporte()

    elif(opcion == 5):
        print("Saliendo...")
        break

    else:
        print("Esa opcion no es valida. Por favor selecciona una opcion correcta")
