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
    def __init__(self, NAME, name, stats, evolutions, eggMoves, levelUpMoves, TMHMMoves, tutor, forms, SEnc, dex, id):
        self.NAME = NAME
        self.name = name
        self.stats = stats
        self.evolutions = evolutions
        self.eggMoves = eggMoves
        self.levelUpMoves = levelUpMoves
        self.TMHMMoves = TMHMMoves
        self.tutor = tutor
        self.forms = forms
        self.SEnc = SEnc
        self.dex = dex
        self.id = id



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