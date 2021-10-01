def obtener_ganadores(lista_ganadores):
  lista_unica=[]
  for i in lista_ganadores:
    if i not in lista_unica:
      lista_unica.append(i)
  return lista_unica

def obtener_posiciones_premio_doble(lista_carreras_con_premio,lista_ganadores,caballo ):
  lista_final_premio=[]
  c=0
  for i in lista_carreras_con_premio:
    if lista_ganadores[i] == caballo:
        lista_final_premio.append(i)
        c+=1
    else:
      c+=1

  return lista_final_premio


def obtener_caballos_no_ganadores(lista_ganadores_ayer,lista_ganadores_hoy):
  lista_t_no_ganadores=[]
  for i in lista_ganadores_ayer:
    if i not in lista_ganadores_hoy:
      lista_t_no_ganadores.append(i)
  return lista_t_no_ganadores

def contar_nuevos_caballos_ganadores(lista_ganadores_ayer,lista_ganadores_hoy):
  l_nuevos=[]
  a=len(lista_ganadores_ayer)
  b=len(lista_ganadores_hoy)
  if a < b:
    for item in lista_ganadores_ayer:
      if item not in lista_ganadores_hoy:
        if item not in l_nuevos:
          l_nuevos.append(item)
  else:
    for item in lista_ganadores_hoy:
      if item not in lista_ganadores_ayer:
        if item not in l_nuevos:
          l_nuevos.append(item)

  x=len(l_nuevos)
  return x
