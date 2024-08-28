from libs.funcs import update

if __name__=="__main__":
    version=input("Descargar version (dejar en blanco para la última): ")
    if not(version):
        version="latest"
    match int(input("Descargar 1. Paquete o 2. Source: ")):
        case 1:
            update("compiled", version)
        case 2:
            update("source", version)