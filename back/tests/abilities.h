const u8 gAbilityNames[ABILITIES_COUNT][ABILITY_NAME_LENGTH + 1] =
{
    [ABILITY_A] = _("Aa"),
    #ifdef GENERATION
        [ABILITY_B] = _("Bb"),
    #endif
    [ABILITY_C] = _("Cc"),
    #ifdef BADFLAG
        [WRONG_A] = _("XX"),
    #endif
    [ABILITY_D] = _("Dd"),
    #ifndef GENERATION
        [WRONG_B] = _("XX"),
    #else
        [ABILITY_E] = _("Ee"),
    #endif
    [ABILITY_F] = _("Ff"),
    #ifndef BADFLAG
        [ABILITY_G] = _("Gg"),
    #else
        [WRONG_C] = _("XX"),
    #endif
    [ABILITY_H] = _("Hh"),
    #define NEWFLAG
    #ifdef NEWFLAG
        [ABILITY_I] = _("Ii"),
    #else
        [WRONG_D] = _("XX"),
    #endif
    [ABILITY_J] = _("Jj"),
    #if NB_A == NB_A
        [ABILITY_K] = _("Kk"),
    #else
        [WRONG_E] = _("XX"),
    #endif
    [ABILITY_L] = _("Ll"),
    #if NB_A < NB_C
        [ABILITY_M] = _("Mm"),
    #elif NB_A > NB_C
        [WRONG_G] = _("XX"),
    #else 
        [WRONG_H] = _("XX"),
    #endif
    #if NB_A > NB_C
        [WRONG_I] = _("XX"),
    #elif NB_A < NB_C
        [ABILITY_N] = _("Nn"),
    #else
        [WRONG_J] = _("XX"),
    #endif
    #if GENERATION == 7
        [ABILITY_1] = _(""),
    #endif
    #if GENERATION != 7
        [WRONG_1] = _(""),
    #endif
    #if GENERATION >= 7
        [ABILITY_2] = _(""),
    #endif
    #if GENERATION <= 7
        [ABILITY_3] = _(""),
    #endif
    #if GENERATION > 7
        [WRONG_2] = _(""),
    #endif
    #if GENERATION < 7
        [WRONG_3] = _(""),
    #endif
    #if NB_A == NB_A
        [ABILITY_4] = _(""),
    #endif
    #if NB_A != NB_B
        [ABILITY_5] = _(""),
    #endif
    #if NB_A < NB_B
        [ABILITY_6] = _(""),
    #endif
    // not supported yet
    #if (NB_A < NB_B)
        [ABILITY_7] = _(""),
    #endif
    #if (NB_A)
        [ABILITY_8] = _(""),
    #endif
    #if (NB_A < NB_B) || (NB_A > NB_B)
        [ABILITY_9] = _(""),
    #endif
    #if (NB_A < NB_B) && (NB_B < NB_C)
        [ABILITY_10] = _(""),
    #endif
};
