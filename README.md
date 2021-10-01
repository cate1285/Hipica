# Hipica
En un hipódromo requieren automatizar algunas operaciones que realizan diariamente al final del día, para ello deciden construir un módulo en Python que realice las siguientes operaciones:

 

1.     obtener_ganadores( lista_ganadores ): dada una lista de los caballos ganadores durante el día, y la función debe retornar la lista agregada con los nombres de los caballos ganadores (sin repeticiones):

 

Entrada

lista_ganadores = ['Spirit', 'Spirit', 'Imperiozo', 'Pegazo', 'Imperiozo', 'Babieca', 'Spirit', 'Jumper']

 

Salida

['Spirit', 'Imperiozo', 'Pegazo', 'Babieca', 'Jumper']

 

 

2.     obtener_posiciones_premio_doble( lista_carreras_con_premio, lista_ganadores, caballo ): dado que en la jornada tienen un beneficio a los apostadores, que consiste en regalar al duplicar el premio para una lista determinada de carreras. Por lo tanto, quieren saber la lista de carreras con premio doble en las que un caballo fue ganador.

 

Entrada

lista_carreras_con_premio = [0, 3, 6]

lista_ganadores = ['Spirit', 'Spirit', 'Imperiozo', 'Pegazo', 'Imperiozo', 'Babieca', 'Spirit', 'Jumper']

caballo = Spirit

 

Salida

[0, 6]

 

3.     obtener_caballos_no_ganadores( lista_ganadores_ayer, lista_ganadores_hoy ): requieren saber la lista de caballos que no ganaron durante el día actual comparado con los ganadores del día anterior.

 

Entrada

lista_ganadores_ayer = ['Spirit', 'Spirit', 'Imperiozo', 'Pegazo', 'Imperiozo', 'Babieca', 'Spirit', 'Jumper']

caballo = Spirit

lista_ganadores_hoy = ['Imperioso', 'Spirit', 'Imperiozo', 'Pegazo', 'Imperiozo', 'Spirit', 'Spirit', 'Pegazo']

caballo = Spirit

 

Salida

['Babieca', 'Jumper']

 

4.     contar_nuevos_caballos_ganadores( lista_ganadores_ayer, lista_ ganadores_hoy ): requieren saber la cantidad de caballos nuevos ganadores el día actual con respecto a los ganadores del día anterior. De acuerdo con el ejemplo, los caballos Spirit y Jumper fueron ganadores el día actual, pero no el día anterior. De ahí que la salida esperada sea 2.

 

Entrada

lista_ganadores_ayer = ['Imperioso', 'Imperioso', 'Babieca', 'Pegazo', 'Imperiozo', 'Babieca', 'Babieca', 'Babieca']

caballo = Spirit

lista_ganadores_hoy = ['Imperioso', 'Spirit', 'Imperiozo', 'Pegazo', 'Imperiozo', 'Spirit', 'Spirit', 'Jumper']

 

Salida

2

 

Entrada

Este programa no necesita entrada y tampoco generará salida. Se requiere que el estudiante genere un archivo con el nombre hipica.py. Adicionalmente, los nombres de las funciones deben ser iguales a los descritos en este documento.

 

Puntuación

Si el responsable de sistemas del hipódromo puede importar el módulo se obtiene un punto. Para cada función que cumpla con la funcionalidad pedida se agrega un punto, cuatro funciones para 4 puntos posibles. En total, 5 puntos.

