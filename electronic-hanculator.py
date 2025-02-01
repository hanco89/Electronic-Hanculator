#================================Programa calculador de resistencias================================

#====Funciones====

#-----Función de conversión de unidades-----

#==={
def converter_ohm(unit_to_convert,unit_destination,amount_unit_to_convert):

    #Diccionario de conversiones:

    conversions = {

        "E" : 1e18,
        "P" : 1e15,
        "T" : 1e12,
        "G": 1e9,
        "M": 1e6,
        "k": 1e3,
        "b": 1,
        "m": 1e-3,
        "u": 1e-6,
        "n": 1e-9,
        "p": 1e-12

        }

    #Calculando:    

    #Si la unidad a convertir, la unidad a la que queremos llegar y la cantidad estan en el diccionario se ejecuta:
    if unit_destination in conversions and unit_to_convert in conversions:

        #Se multiplica la cantidad por el resultado de la division entre la unidad a convertir y la unidad destino:
        result_converter = amount_unit_to_convert * (conversions[unit_to_convert] / conversions[unit_destination])

        #Retornando el resultado:
        return  result_converter
    
    else:

        
        return "Valor ingresado no válido"
#===}    

#-----Funcion para mostrar los tipos de unidades-----

#==={
def options_units_function():

    # Diccionario de opciones de las unidades
    options_units = {
        
        "E" : "Exa",
        "P" : "Peta",
        "T" : "Tera",
        "G"   : "Giga", 
        "M"   : "Mega", 
        "k"   : "Kilo", 
        "b"    : "Unidad base (Ohm, Amper, Volt)", 
        "m" : "Mili", 
        "u"   : "Micro",
        "n"   : "Nano", 
        "p"   : "Pico"

        }

    # Crear la cadena de salida que contiene todas las opciones

    result = f"Opciones disponibles de unidades:\n"

    for abbreviation, meaning in options_units.items():
        result += f"Opcion: {abbreviation} /// Significado: {meaning}\n"
        # Retornar la cadena con las opciones
    return result
#===}

#-----Funcion para calcular resistencias en serie-----

#==={
def calculate_series_r(amount_r_serie):
     
    #Lista para almacenar las resistencias dadas por el usuario

    resistances_series = {}

    #Diccionario de conversiones de unidades:

    conversions = {

        "E" : 1e18,
        "P" : 1e15,
        "T" : 1e12,
        "G": 1e9,
        "M": 1e6,
        "k": 1e3,
        "b": 1,
        "m": 1e-3,
        "u": 1e-6,
        "n": 1e-9,
        "p": 1e-12

        }

    #Mostrando las opciones:
    
    print(options_units_function())
    
    #Creando valores de R dependiendo la decision del usuario:
    
    #Adviertiendo al usuario que use mayusculas para diferenciar las unidades:
    print("Por favor respeta las mayusculas con respecto a la opcion que eligas: P ≠ p")
    
    for r_series in range(amount_r_serie):
       
        #Pidiendo al usuario unidad y valor:
        #Unidad de cada resistencia:
        unit = input(f"Ingresa la unidad de R{r_series+1}= ")
        if unit in conversions:
        
            #Aviso para que el usuario no cometa errores:
            print("Si es un numero decimal, utiliza un punto . en lugar de una coma ,")

            #Valor de cada resistencia:
            valor_unit = num_validation_float(input(f"Ingresa el valor de R{r_series+1}= "))

            valor_in_ohm = valor_unit * conversions[unit]

        #Si el usuario ingresa una unidad invalida:   
        elif not unit in conversions:
            
            try:
                
                validation = False
                while not unit in conversions:
                    
                    print(f"Unidad {unit} no valida. Reingrese el valor:") 
                    unit = input(f"Ingresa la unidad de R{r_series+1}= ")
                    
            except:
                    print("Error, Reingrese el valor")    
                       
        #Almacenando las resistencias en el diccionario:
        resistances_series[f"R{r_series+1}"] = valor_in_ohm

        #Calcular la resistencia total:
        resistance_total = sum(resistances_series.values())

    #Mostrar resultados:
    print("Resistencias en Ohm:")

    #Iterando el diccionario:
    for key,value in resistances_series.items():

        #Mostrando clave y valor:
        print(f"{key} = {value}Ω")
            
    #Mostrando resultados finales:    
    print(f"Resistencia total real: {resistance_total}Ω")

    #Mostrando el valor redondeado:
    print(f"Resistencia total redondeada: {resistance_total:.2f}Ω")  
#===}         

#-----Funcion para calcular resistencias en paralelo-----

#==={   
def calculate_parallel_r(amount_r_parallel):

    #Lista para almacenar las resistencias dadas por el usuario
    resistances_parallel = {}

    #Diccionario de conversiones:
    conversions = {
        
        "E" : 1e18,
        "P" : 1e15,
        "T" : 1e12,
        "G": 1e9,
        "M": 1e6,
        "k": 1e3,
        "b": 1,
        "m": 1e-3,
        "u": 1e-6,
        "n": 1e-9,
        "p": 1e-12

        }
    
    #Mostrando las opciones llamando a la funcion options_units_function()
    print(options_units_function())
    
    #Creando valores de R dependiendo la decision del usuario:
    for r_parallel in range(amount_r_parallel):

        #Pidiendo al usuario que ingrese la unidad de cada resistencia
        unit = input(f"Ingresa la unidad de R{r_parallel+1}= ")
        
        if unit in conversions:
            
            #Pidiendo al usuario que ingrese el valor de cada resistencia
            value = num_validation_float(input(f"Ingresa el valor de R{r_parallel+1}= "))
            
            #Abriendo un try en caso de un posible error
            try:

                #Convertir a  Ohm
                valor_en_ohm = value * conversions[unit]
            
            #En caso de error:
            except:
                
                #Mostrando una advertencia y pidiendo que reingrese una opcion:
                print("ERROR: VALOR INGRESADO NO VALIDO. SIGA LAS REGLAS E INTENTE DE NUEVO:")
                user_option = user_validation()
                
        #Si el usuario ingresa una unidad inexistente:    
        elif not unit in conversions:
            
            #Abriendo un try en caso de error:
            try:
                
                #Abriendo un bucle hasta que la unidad ingresada por el usuario no este en el diccionario de conversiones
                while not unit in conversions:
                    
                    #Mostrando mensaje de error:
                    print(f"Unidad {unit} no valida. Reingrese el valor:") 
                    
                    #Pidiendo al usuario que ingrese la unidad nuevamente:
                    unit = input(f"Ingresa la unidad de R{r_parallel+1}= ")
                    
            #En caso de error:        
            except:
                    print("Error, Reingrese el valor")    

        #Almacenando las resistencias en el diccionario:
        resistances_parallel[f"R{r_parallel+1}"] = valor_en_ohm

        #Calcular la resistencia total:
        
        #Lo que hice yo:
        #r_division_by_one = 1 / (sum(1 / resistances_parallel.values()))

        #Como me corrigio chat gpt:
        r_division_by_one = 1 / sum(1 / r for r in resistances_parallel.values())

        
    #Mostrando resultado final:
    #Iterando el diccionario con las resistencias almacenadas:
    for sub_resistances_parallel in resistances_parallel.items():

        key = sub_resistances_parallel[0]
        value = sub_resistances_parallel[1]

        #Presentando las resistencias al usuario
        print(f"{key} = {value}Ω")

    #Resistencia total:    
    print(f"Valor final:{r_division_by_one}Ω")

    #Resistencia total redondeada a 2 decimales: 
    print(f"Valor redondeado:{r_division_by_one:.2f}Ω")
#===}    

#-----Funcion calculadora de colores de resistencias-----

#==={
def calculate_color_r(op_color):

    #Diccionarios para determinar el valor de cada color

    #Primera y segunda banda:

    first_and_second_band = {  
        
        "negro" : "0",                    
        "marron" : "1",
        "rojo" : "2",
        "naranja" : "3",
        "amarillo" : "4",
        "verde" : "5",
        "azul" : "6",                 
        "violeta" : "7",                
        "gris" : "8",                
        "blanco" : "9",                   
        "oro" : None,                   
        "dorado" : None,                   
        "plata": None,        
        "plateado" : None,     
        "ninguno" : None
                            
        }

    #Tercera banda

    third_band = {  
        
        "negro" : 1,        
        "marron" : 10,        
        "rojo" : 100,        
        "naranja" : 1000,        
        "amarillo" :10000,        
        "verde" : 100000,          
        "azul" : 1000000,                  
        "violeta" : 10000000,                 
        "gris" : 100000000,                 
        "blanco" : 1000000000,                 
        "oro" : 0.1,                 
        "dorado" : 0.1,              
        "plateado" : 0.01,          
        "plata" : 0.01,                 
        "ninguno" : None

        }

    #Cuarta Banda           
    
    quarter_band = {    
        
        "negro" : None,        
        "marron" : "±1%",        
        "rojo" : "±2%",        
        "naranja" : None,        
        "amarillo" :None,         
        "verde" : "±0.5%",          
        "azul" : "±0.25%",          
        "violeta" : "±0.10",         
        "gris" : "±0.05%",         
        "blanco" : None,         
        "oro" : "±5%",         
        "dorado" : "±5%",         
        "plateado": "±10%",        
        "plata": "±10%",    
        "ninguno" : None

        }

    

    #Abriendo un bucle que termina si el usuario elige salir
    while op_color != 0:

        if op_color == 1:

            first = input("Ingresa el color de la primera banda: ").lower()
            second = input("Ingresa el color de la segunda banda: ").lower()
            third = input("Ingresa el color de la tercera banda: ").lower()
            quarter = input("Ingresa el color de la cuarta banda: ").lower()

            if first and second and third in first_and_second_band:

                #Sumando las dos primeras bandas:
                sum_first_and_second_bands = int(first_and_second_band[first] + first_and_second_band[second])

                #Multiplicando por el valor de la tercera banda:  
                multiply_sum_first_second = sum_first_and_second_bands * third_band[third]

                #Mostrando resultados:
                result_finally_color = f"El resultado es: {multiply_sum_first_second}Ω {quarter_band[quarter]}"
                print(result_finally_color)
                op_color = decision_color()
                        
            elif first or second or third not in first_and_second_band:   
                    
                print("ERROR:COLOR NO VALIDO")
                op_color = 0
                    
                        
        elif op_color == 2:

            decision_user_color = input("Quieres salir o calcular?: ").lower()

            if decision_user_color == "calcular":
                
                print("Debes ingresar el valor en Ohms Ω")
                number = input("Ingresa el valor: ")
                numbers_in_colors = []

                for iteration_number in number:

                    first_band_number = first_and_second_band[0] = iteration_number
                    numbers_in_colors.append(first_band_number)

                for numbers_in_list in numbers_in_colors:

                    print(f"Los colores son: {numbers_in_list}")   
                               
#===}

#----- Funcion para mostrar las opciones -----

#==={
def options_main():

    #opciones:
    options = {
    
        "0" : "Salir.",
        "1" : "Conversion de unidades SI." ,
        "2" : "Cálcular resistencias en serie." , 
        "3" : "Cálcular resistencias en paralelo." ,
        "4" : "Identificar valores de resistencia según colores.",
        "5" : "Ley de Ohm.",
        "6" : "Calcular resistencia limitadora de diodo led."
    
        }
    
    result_2 = "Opciones:"

    #mostrando las diferentes opciones:
    for num, meaning in options.items():
        
        result_2 += f"\n Opcion: {num} /// {meaning}"

    return result_2    
#===}

#----- Funcion para validar la opcion de usuario -----

#==={
def user_validation():    

    valid = False
    mostrar_opciones = options_main()
    print(mostrar_opciones)

    while not valid:

        try: 

            user_option = int(input("Ingresa una opcion (Numero): "))
            valid = True
            return user_option

        except:

            print("Error: Valor ingresado no válido, vuelve a ingresarlo:")
#===}

#----- Funcion para validar la entrada de un numero por el usuario y devolver int -----

#==={
def num_validation_int(val):
    
    try:
        return int(val)
    
    except ValueError:

        value_valid = False
        while not value_valid:

            try:

                print("Valor ingresado no válido. Por favor ingresa un valor válido.")
                val = int(input("Ingresa el valor nuevamente: "))
                value_valid = True  
                
            except ValueError:

                print("Error: El valor ingresado no es un número entero válido. Vuelve a intentarlo.")

        return int(val)
#===}

#----- Funcion para validar la entrada de un numero por el usuario y devolver float -----

#==={
def num_validation_float(val):
    
    try:
        return float(val)
    
    except ValueError:

        value_valid = False
        while not value_valid:

            try:

                print("Valor ingresado no válido. Por favor ingresa un valor válido.")
                val = int(input("Ingresa el valor nuevamente: "))
                value_valid = True  
                
            except ValueError:

                print("Error: El valor ingresado no es un número entero válido. Vuelve a intentarlo.")

        return float(val)
#===}

#----- Funcion para elegir que tipo de conversion de colores hacer ----

#==={
def decision_color():
    
    print("ingresa una opcion:")
    print("Opciones: 0)Salir --- 1)color/numero --- 2)numero/color")
            
    try:
        op_color = int(input("Ingresa la opcion (Numero): "))
    except:
        op_color = num_validation_int(input("Ingresa la opcion (Numero): "))
            
    return op_color        
#===}

#----- Funcion para mostrar las opciones de las magnitudes de la ley de ohm

#==={
def show_options_magnitudes(): 
           
        options_magnitudes = {  0 : "Salir",
                            1 : "Calcular Voltaje",
                            2 : "Calcular Intensidad",
                            3 : "Calcular Reistencia",
                            4 : "Calcular Potencia"
                        }
        for option_mag , meaning_mag in options_magnitudes.items():
            print(f"Opcion : {option_mag} /// {meaning_mag}")
#===}

#----- Funcion para hacer calculos de la ley de Ohm -----

#==={    
def calcular_ley_ohm(op_magnitude):
    
    options_magnitudes = {  0 : "Salir",
                            1 : "Calcular Voltaje",
                            2 : "Calcular Intensidad",
                            3 : "Calcular Reistencia",
                            4 : "Calcular Potencia"
                        }
    if op_magnitude in options_magnitudes:
        
        while op_magnitude != 0:
            
            if op_magnitude == 1:
            
                print("Calcula Voltaje:")
            
                i  = num_validation_float(input("Ingresa la intensidad del circuito: "))
                r = num_validation_float(input("Ingresa la resistencia del circuito: "))
                v = i * r 
            
                print(f"Valores Ingresados :\n Intensidad = {i}A \n Resistencia = {r}Ω")
                print(f"EL resultado es {v}V\n")
                show_options_magnitudes()
                op_magnitude = num_validation_int(input("Elige una opcion : "))   
                
            
            elif op_magnitude == 2:    
            
                print("Calcula Intensidad:")
            
                v = num_validation_float(input("Ingresa el voltaje del circuito: "))
                r = num_validation_float(input("Ingresa la resistencia del circuito: "))
                i = v / r
            
                print(f"\nValores Ingresados :\n Voltaje = {v}V \n Resistencia = {r}Ω")
                print(f"EL resultado es {i}A")
                show_options_magnitudes()
                op_magnitude = num_validation_int(input("Elige una opcion : "))   
                
            
            elif op_magnitude == 3:
            
                print("Calcula Resistencia:")
            
                v = num_validation_float(input("Ingresa el voltaje del circuito: "))
                i = num_validation_float(input("Ingresa la intensidad del circuito: "))
                r = v / i    
            
                print(f"\nValores Ingresados :\n Voltaje = {v}V \n Intensidad = {i}A")
                print(f"EL resultado es {r}Ω")
                show_options_magnitudes()
                op_magnitude = num_validation_int(input("Elige una opcion : "))   
                
            
            elif op_magnitude == 4:
            
                print("Calcula Potencia:")
            
                print("Metodo 1: Calcular mediante Intensidad y Voltaje \n Metodo 2: Calcula mediante Intensidad y Resistencia \n Metodo 3: Calcular mediante Voltaje y Resistencia")    
                op_power = num_validation_int(input("Ingresa una opcion (1/2/3) : "))
            
                if op_power == 1:
                
                    print("Calcula potencia (I*V)")
                
                    i = num_validation_float(input("Ingresa la intensidad del circuito: "))
                    v = num_validation_float(input("Ingresa el voltaje del circuito: "))
                    p = i * v
                
                    print(f"\nValores Ingresados :\n Voltaje = {v}V \n Intensidad = {i}A")
                    print(f"EL resultado es {p}W")
                    show_options_magnitudes()
                    op_magnitude = num_validation_int(input("Elige una opcion : "))   
                
                elif op_power == 2:
                
                    print("Calcula potencia (I^2 * R)")
                
                    i = num_validation_float(input("Ingresa la intensidad del circuito: "))
                    r = num_validation_float(input("Ingresa la resistencia del circuito: "))
                    p = r * (i ** 2)
                
                    print(f"\nValores Ingresados :\n Resistencia = {r}Ω \n Intensidad = {i}A")
                    print(f"EL resultado es {p}W")
                    show_options_magnitudes()
                    op_magnitude = num_validation_int(input("Elige una opcion : "))   
                
                elif op_power == 3:
                
                    print("Calcula potencia (V^2 / R)")
                
                    v = num_validation_float(input("Ingresa el voltaje del circuito: "))
                    r = num_validation_float(input("Ingresa la resistencia del circuito: "))
                    p = (v ** 2) / r
                
                    print(f"\nValores Ingresados :\n Resistencia = {r}Ω \n Voltaje = {v}V")
                    print(f"EL resultado es {p}W")
                    show_options_magnitudes()
                    op_magnitude = num_validation_int(input("Elige una opcion : ")) 
                       
                
                show_options_magnitudes()
                op_magnitude = num_validation_int(input("Elige una opcion : "))   
        
    else: 
        
        print("ERROR: VALOR NO VALIDO")    
#===}

#----- Funcion para calcular la resistencia limitadora de un diodo led -----
#===={
def calcular_diodo_led():
    pito = "aparato reproductor del hombre"
        
#====}                
                    
#================================ Main ================================

#Mensaje de bienvenida:
print("Bienvenido a Electronic Hanculator , aqui tienes herramientas para trabajar con resistencias")

#Mensaje para indicar que eliga una opcion:
print("Por favor, elige una de las siguientes options para continuar:")

#opciones:
options_main()

#mostrando las diferentes opciones:
mostrar_opciones = options_main()
print(mostrar_opciones)

#Pidiendo al usuario que eliga una opcion:
user_option = input("Ingresa una opcion (Numero): ")

#En caso de ingresar un valor diferente a un numero:
while not user_option.isdigit():

    print("Error: Debes ingresar una de las opciones que aparecen en pantalla")
    print("Ejemplo: 1: Conversion de unidades, si deseas elegir conversion de unidades ingresa: 1")
    user_option = input("Ingresa una opcion (Numero): ")

#Convirtiendo el numero a entero
user_option = int(user_option)    

#Diccionario para las unidades:
options_units = {   
    
    "g" : "Giga " ,          
    "m" : "Mega" ,          
    "k" : "Kilo " ,           
    "b" : "Unidad Base(Ohm, Amper, Volt)" ,            
    "mili" : "Mili" ,         
    "u" : "Micro",         
    "n" : "Nano" ,          
    "p" : "Pico"
                 
    }

#Abriendo un bucle para continuar con el programa hasta que el usuario desee:
while user_option != 0:
   
#===== Opcion 1 : Conversion de unidades : =====

    if user_option == 1:
        
        conversions = {
        
        "E" : 1e18,
        "P" : 1e15,
        "T" : 1e12,
        "G": 1e9,
        "M": 1e6,
        "k": 1e3,
        "b": 1,
        "m": 1e-3,
        "u": 1e-6,
        "n": 1e-9,
        "p": 1e-12

        }

        #Presentando la opcion 1:
        print("Conversion de unidades:")
        print("Elige una opcion de acuerdo a esto:")

        #Mostrando al usuario las opciones de conversiones:
        options = options_units_function()
        print(options)


        #Advirtiendo al usuario para que tenga precaucion con respecto al uso de mayusculas:
        print("Por favor respeta las mayusculas con respecto a la opcion que eligas: P ≠ p")
        
        #Variables para definir las unidades y cantidad a convertir que quiera el usuario:
        
        #Variable para mantener el bucle abierto hasta que el usuario ingrese un valor correcto:
        value_valid = False
        
        #Ejecutando un bucle hasta que value_valid sea  True:
        while not value_valid:
            
            #Variable para definir la unidad a convertir:
            unit_to_convert = input("Ingresa la unidad que quieres convertir: ")
            
            #Variable para definir la unidad destino:
            unit_destination = input("Ingresa la unidad a la que la quieres convertir: ")
            
            #Si las unidades ingresadas son correctas, entonces continuar:
            if unit_to_convert in conversions and unit_destination in conversions:
                
                #la variable pasa de False a True, entonces termina el bucle y continua
                value_valid = True
                
            #Si las unidades ingresadas son incorrectas entonces repetir el bucle:    
            else:
                
                #Muestra mensaje de error y se repite el bucle
                print("Valor Ingresado no valido")
                 
        
        #Bucle para que el usuario ingrese un valor correcto
        
        #Variable para mantener el bucle abierto hasta que el usuario ingrese un valor correcto:
        value_valid = False

        #Ejecutando un bucle hasta que value_valid sea  True:
        while not value_valid:
            
            #Intentando ejecutar:
            try:

                #Advirtiendo al usuario que use un punto en vez de una coma:
                print("Si va a ingresar un numero decimal utilice un punto en vez de una coma")
                
                #Pidiendo al usuario que ingrese la cantidad a convertir
                amount_unit_to_convert = float(input("Ingresa la cantidad que quieras convertir: "))
                
                #Cerrando el bucle
                value_valid = True

            #En caso de error:
            except:

                print("Error: Valor ingresado no válido, vuelve a ingresarlo:")
                    
        #Calculando y mostrando el resultado con la funcion converter_ohm()
        result = converter_ohm(unit_to_convert,unit_destination,amount_unit_to_convert)
        
        #Si la unidad a convertir es unidad base entonces solo mostrar el simbolo de ohm Ω:
        if unit_to_convert and unit_destination in conversions :
            
            if unit_destination == "b":

                #Mostrando resultado
                print(f"Resultado final: {result}Ω")
                print(f"Resultado final redondeado: {result:.2f}Ω")
                user_option = user_validation()
            
        #Si es otro valor entonces usar como prefijo la letra correspondiente a la unidad en mayuscula:    
            elif unit_destination != "b":    

                #Mostrando resultado 
                print(f"Resultado final: {result} {unit_destination.upper()}Ω")
                print(f"Resultado final redondeado: {result:.2f}{unit_destination.upper()}Ω")
                user_option = user_validation()    
                
        else: 
            
            print(None)        

#===== Opcion 2 : Calculo de resistencias en serie : =====

    if user_option == 2:
        
        try:
            
            #Pidiendo al usuario que ingrese una opcion
            amount_r_serie = input("Ingresa la cantidad de resistencias en serie o 0 para salir: ")
            ars_validate_serie = num_validation_int(amount_r_serie)
            
            if ars_validate_serie < 2:

                print("Debes ingresar mas de 2 resistencias")

            else:

                calculate_series_r(ars_validate_serie) 

            
            if ars_validate_serie == 0:
                user_option = user_validation()
                
        except:
            
            print("ERROR: VALOR INGRESADO NO VALIDO. SIGA LAS REGLAS E INTENTE DE NUEVO:")
            user_option = user_validation()
            
                    
                  

#===== Opcion 3 : Calculo de resistencias en paralelo : =====                

    if user_option == 3:

            #Pidiendo al usuario que ingrese la cantidad de resistencias en paralelo o 0 para salir
            amount_r_paralell = num_validation_int(input("Ingresa la cantidad de resistencias en paralelo o 0 para salir: "))
            
            #Si el usuario ingresa el numero 0 volvera al menu principal
            if amount_r_paralell == 0:
                
                #Declarando otra vez la variable user_option mediante la funcion user_validation()
                user_option = user_validation()    

            #En caso de que el usuario ingrese menos de dos resistencias:
            if amount_r_paralell < 2:
                
                #Se abre un bucle hasta que el usuario ingrese mas de dos resistencias
                while amount_r_paralell < 2:
                    
                    #Mostrando el mensaje de advertencia
                    print("Debes ingresar mas de 2 resistencias")
                    
                    #Volviendo a pedir la canatidad
                    amount_r_paralell = num_validation_int(input("Ingresa la cantidad de resistencias en paralelo o 0 para salir: "))
                 
            #Si el usuario ingresa la cantidad de resistencias:
            else:
                
                #Llamando a la funcion calculadora de resistencias en paralelo
                calculate_parallel_r(amount_r_paralell) 
                
            
                


#===== Opcion 4 : Conversion de colores : =====

    if user_option == 4:
        
        #Preguntando al usuario que tipo de conversion de color quiere hacer
        op_color = decision_color()
        
        #llamando a la funcion para calcular los colores
        calculate_color_r(op_color)
        
        #Pidiendo al usuario que ingrese otra opcion
        user_option = user_validation()  
        
#==== Opcion 5 : Ley de OHm : =====        

    if user_option == 5:
        
        #Mostrando mensaje de la opcion
        print("Calcular Ley de Ohm")
        
        #Mostrando las opciones de conversion
        show_options_magnitudes()
        
        #Pidiendo al usuario que eliga una opcion y validando que sea un numero entero
        op_ohm = num_validation_int(input("Elige una opcion : "))
        
        #Llamando a la funcion calculadora de ley de ohm
        calcular_ley_ohm(op_ohm)
        
        #Pidiendo al usuario que ingrese otra opcion
        user_option = user_validation()  
        
#===== Opcion 6: Calculo resistencia limitadora diodo led ====        

    if user_option == 6:
        
        #Mostrando mensaje de la opcion:
        print("Calculo de resistencia limitadora de diodo led")
        
        #Mostrando las opciones
        print("Opciones:")
        print("\n0 : Salir ///\n1 : Calculo de un solo led ///\n2 : Calculo en serie///\n3 : Calculo en paralelo")
        
        #Creando una variable para validar los datos:
        options_r_led = [0,1,2,3]
        
        #Pidiendo al usuario que ingrese una opcion
        amount_r_led = num_validation_int(input("Ingresa una opcion: "))
        
        validation = False
        
        while validation == False:
        
            if amount_r_led in options_r_led:
                print("muy bien")
                #calcular_diodo_led(amount_r_led)
            
            else:
            
                #Mostrando mensaje de error:
                print("Opcion no valida. Intente de nuevo:")
            
                

                  

#Mensaje final:
print("Muchas gracias por usar Electronic Hanculator que tengas buen dia, puto...")   





