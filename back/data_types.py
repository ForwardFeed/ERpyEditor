class CompactBaseStats:
    def __init__(self, base, types, catchR, exp, EVY, items, gender, eggC, fren, grow, eggG, abis, inns, col, noFlip, flags):
        self.base = base
        self.types = types
        self.catchR = catchR
        self.exp = exp
        self.EVY = EVY
        self.items = items
        self.gender = gender
        self.eggC = eggC
        self.fren = fren
        self.grow = grow
        self.eggG = eggG
        self.abis = abis
        self.inns = inns
        self.col = col
        self.noFlip = noFlip
        self.flags = flags

class CompactEvolution:
    def __init__(self, kd, rs, inn):
        self.kd = kd
        self.rs = rs
        self.inn = inn

class CompactLevelUpMove:
    def __init__(self, lv, id):
        self.lv = lv
        self.id = id

class CompactedScripted:
    def __init__(self, how, map):
        self.how = how
        self.map = map

class PokePokedex:
    def __init__(self, id, desc, hw):
        self.id = id
        self.desc = desc
        self.hw = hw

class CompactSpecies:
    def __init__(self, NAME):
        self.NAME = NAME
        self.name = None
        self.stats = None
        self.evolutions = None
        self.eggMoves = None
        self.levelUpMoves = None
        self.TMHMMoves = None
        self.tutor = None
        self.forms = None
        self.SEnc = None
        self.dex = None
        self.id = None

class Locations:
    def __init__(self):
        self.maps = []
        self.landRate = []
        self.waterRate = []
        self.fishRate = []
        self.honeyRate = []
        self.rockRate = []
        self.hiddenRate = []
        self.rodGrade = []

class Location:
    def __init__(self, name):
        self.name = name
        self.land = []
        self.landR = None
        self.water = []
        self.waterR = None
        self.fish = []
        self.fishR = None
        self.honey = []
        self.honeyR = None
        self.rock = []
        self.rockR = None
        self.hidden = []
        self.hiddenR = None

class Encounter:
    def __init__(self, min_val, max_val, species):
        self.min = min_val
        self.max = max_val
        self.species = species

class TrainerPokemon:
    def __init__(self, species, ability, ivs, evs, item, nature, moves):
        self.species = species
        self.ability = None
        self.ivs = None
        self.evs = None
        self.item = None
        self.nature = None
        self.moves = None

# export interface TrainerPokemon{
#     specie: string,
#     ability: number,
#     ivs: number[],
#     evs: number[],
#     item: string,
#     nature: string,
#     moves: string[]
# }
# export interface Locations{
#     maps: Location[],
#     landRate: number[],
#     waterRate: number[],
#     fishRate: number[],
#     honeyRate: number[],
#     rockRate: number[],
#     hiddenRate: number[],
#     rodGrade: number[],

# }
# export interface Location {
#     name: string,
#     land: Encounter[] | undefined,
#     landR: number | undefined,
#     water: Encounter[] | undefined,
#     waterR: number | undefined,
#     fish: Encounter[] | undefined,
#     fishR: number | undefined,
#     honey: Encounter[] | undefined,
#     honeyR: number | undefined,
#     rock: Encounter[] | undefined,
#     rockR: number | undefined,
#     hidden: Encounter[] | undefined,
#     hiddenR: number | undefined,
# }

# export interface Encounter{
#     min: number,
#     max: number,
#     specie: string
# }

# interface CompactBaseStats{
#     base: number[]
#     types: number[],
#     catchR: number,
#     exp: number,
#     EVY: number[],
#     items: string[] | undefined,
#     gender: number,
#     eggC: number,
#     fren: number,
#     grow: number, 
#     eggG: number[],
#     abis: number[],
#     inns: number[],
#     col: number,
#     noFlip: boolean,
#     flags: string,
# }
# interface CompactEvolution{
#     kd: number,
#     rs: string,
#     in: number,
# }
# interface CompactLevelUpMove{
#     lv: number,
#     id: number,
# }
# interface CompactedScripted{
#     how: number, // indexed from CompactGameData.ScriptedEncoutersHowT
#     map: number, // index from CompactGameData.maps.
# }
# export interface PokePokedex {
#     id: number,
#     desc: string,
#     hw: [number, number]
#     // category: string
# }
# export interface CompactSpecie{
#     NAME: string,
#     name: string,
#     stats: CompactBaseStats,
#     evolutions: CompactEvolution[],
#     eggMoves: number[],
#     levelUpMoves: CompactLevelUpMove[],
#     TMHMMoves: number[],
#     tutor: number[],
#     forms: number[],
#     SEnc:CompactedScripted[], // scripted encounters
#     dex: PokePokedex,
#     id: number,
# }
        

# export interface CompactGameData{
#     abilities: Ability[],
#     moves: compactMove[],
#     species: CompactSpecie[],
#     locations: CompactLocations,
#     trainers: CompactTrainers[],
#     items: CompactBattleItems[],
#     typeT: string[], //types tabes
#     targetT: string[], //targets table
#     flagsT: string[],
#     effT: string[], // effect table
#     splitT: string[],
#     eggT: string[], // egg group table
#     growT: string[]; // Growth Table
#     colT: string[], //color table
#     evoKindT: string[],
#     natureT: string[],
#     scriptedEncoutersHowT: string[],
#     mapsT: string[],
# }