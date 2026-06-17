# -*- coding: utf-8 -*-

"""
Classe School
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Goncourt:
    """Couche métier de l'application de gestion d'une école,
    reprenant les cas d'utilisation et les spécifications fonctionnelles :
    - courses : liste des cours existants
    - teachers : liste des enseignants
    - students : liste des élèves"""


