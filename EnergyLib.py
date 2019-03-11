import numpy as np
from PyMca5.PyMcaPhysics.xrf import Elements

ElementsInfo = [
   ["H",    0],
   ["He",   0],
   ["Li",   0],
   ["Be",   0],
   ["B",    0],
   ["C",    0],
   ["N",    0],
   ["O",    0],
   ["F",    0],
   ["Ne",   0],
   ["Na",   1.04],
   ["Mg",   1.25399995],
   ["Al",   1.48699999],
   ["Si",   1.74000001],
   ["P",    2.0150001],
   ["S",    2.30800009],
   ["Cl",   2.62199998],
   ["Ar",   2.95700002],
   ["K",    3.31299996],
   ["Ca",   3.69099998],
   ["Sc",   4.09000015],
   ["Ti",   4.51000023],
   ["V",    4.95200014],
   ["Cr",   5.41400003],
   ["Mn",   5.89799976],
   ["Fe",   6.40299988],
   ["Co",   6.92999983],
   ["Ni",   7.47700024],
   ["Cu",   8.04699993],
   ["Zn",   8.63799953],
   ["Ga",   9.2510004],
   ["Ge",   9.88500023],
   ["As",   10.5430002],
   ["Se",   11.2209997],
   ["Br",   11.9230003],
   ["Kr",   12.6479998],
   ["Rb",   13.3940001],
   ["Sr",   14.1639996],
   ["Y",    14.9569998],
   ["Zr",   15.7740002],
   ["Nb",   16.6140003],
   ["Mo",   17.4780006],
   ["Tc",   18.4099998],
   ["Ru",   19.277999],
   ["Rh",   20.2140007],
   ["Pd",   21.1749992],
   ["Ag",   22.1620007],
   ["Cd",   23.1720009],
   ["In",   24.2070007],
   ["Sn",   25.2700005],
   ["Sb",   26.3570004],
   ["Te",   3.76900005],
   ["I",    3.93700004],
   ["Xe",   4.11100006],
   ["Cs",   4.28599977],
   ["Ba",   4.46700001],
   ["La",   0],
   ["Ce",   0],
   ["Pr",   0],
   ["Nd",   0],
   ["Pm",   0],
   ["Sm",   0],
   ["Eu",   0],
   ["Gd",   0],
   ["Tb",   0],
   ["Dy",   0],
   ["Ho",   0],
   ["Er",   0],
   ["Tm",   0],
   ["Yb",   0],
   ["Lu",   0], 
   ["Hf",   0],
   ["Ta",   0],
   ["W",    0],
   ["Re",   0],
   ["Os",   0],
   ["Ir",   0],
   ["Pt",   0],
   ["Au",   9.71100044],
   ["Hg",   9.98700047],
   ["Tl",   0],
   ["Pb",   10.5489998],
   ["Bi",   0],
   ["Po",   0],
   ["At",   0],
   ["Rn",   0],
   ["Fr",   0],
   ["Ra",   0],
   ["Ac",   0],
   ["Th",   0],
   ["Pa",   0],
   ["U",    0],
   ["Np",   0],
   ["Pu",   0],
   ["Am",   0],
   ["Cm",   0],
   ["Bk",   0],
   ["Cf",   0],
   ["Es",   0],
   ["Fm",   0],
   ["Md",   0],
   ["No",   0],
   ["Lr",   0],
   ["Rf",   0],
   ["Db",   0],
   ["Sg",   0],
   ["Bh",   0],
   ["Hs",   0],
   ["Mt",   0],
]
Energies =[index[1] for index in ElementsInfo]
