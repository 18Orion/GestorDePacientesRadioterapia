#Treatment type dict
TREATMENT_DICT={None : 0,
    "Prioridad" : 0, 
    "Preferente" : 0,
    "Su Curso" : 1, 
    "ELK3" : 2, 
    "IMRT" : 3, 
    "ICT" : 4,
    "BQ_HDR" : 6,
    "Urgente" : 7, 
    "Implante Semillas" :8}

#Treatment options
TREATMENT_OPTIONS=["Sin escoger",
    "3D",
    "VMAT",
    "IMRT",
    "ICT",
    "BQ-C (BQ-HDR)",
    "BQ-F",
    "Urgencia", 
    "Implante semillas"]

#Date type
DATE_OPTIONS=["Sin escoger", 
    "Solicitud", 
    "Recepción completa", 
    "Recepción incompleta",
    "Fin del calculo (Fin DC)",
    "QA",
    "Emisión"]

#Gender options
GENDER_OPTIONS=["Masculino", 
    "Femenino"]

#Gender guesser dict to transform to gender options
GENDER_GUESSER_DICT={"male":0, 
    "unknown":0,
    "mostly_male":0,
    "mostly_female":1, 
    "female": 1}

#Type of mantainement
MANTAINEMENT_TYPE=["Sin escoger",
    "Cambio de tubo",
    "Pruebas de aceptación",
    "Niveles de referencia",
    "Niveles de referencia tras cambio de tubo",
    "Niveles de referencia tras cambio de generador",
    "Control de calidad anual",
    "Control de calidad tras resolución de averías",
    "Control de calidad tras cierre de incidencia"]