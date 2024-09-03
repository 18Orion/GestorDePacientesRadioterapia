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

TREATMENT_OPTIONS=["Sin escoger",
    "3D",
    "VMAT",
    "IMRT",
    "ICT",
    "BQ-C (BQ-HDR)",
    "BQ-F",
    "Urgencia", 
    "Implante semillas"]

DATE_OPTIONS=["Sin escoger", 
    "Solicitud", 
    "Recepción completa", 
    "Recepción incompleta",
    "Fin del calculo (Fin DC)",
    "QA",
    "Emisión"]

GENDER_OPTIONS=["Masculino", 
    "Femenino"]

GENDER_GUESSER_DICT={"male":0, 
    "unknown":0,
    "mostly_male":0,
    "mostly_female":1, 
    "female": 1}

MANTAINEMENT_TYPE=["Sin escoger",
    "Cambio de tubo",
    "Mantenimiento"]