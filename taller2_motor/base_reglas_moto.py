from .regla import Regla

HECHOS_INICIALES_MOTOCICLETA = {
    "tiene_motor": True,
    "tiene_dos_ruedas": True,
    "es_menor_de_edad": True,
}

REGLAS_MOTOCICLETA = [
    Regla(
        id="R1",
        condiciones={"tiene_motor": True, "tiene_dos_ruedas": True},
        conclusion={"es_motocicleta": True},
    ),
    Regla(
        id="R2",
        condiciones={"es_motocicleta": True},
        conclusion={"requiere_casco": True},
    ),
    Regla(
        id="R3",
        condiciones={"requiere_casco": True, "es_menor_de_edad": True},
        conclusion={"permiso_denegado": True},
    ),
]
