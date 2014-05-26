class PrimerAlgoParams(object):
    PARAMS = {
            # Bacteria
            'minProdLen' : 140,
            'maxProdLen' : 270,
            'minBacNum' : 100e3,

            # Single primer params
            'max_GC_content' : 70,
            'min_GC_clamp' : 1,
            'max_GC_clamp' : 4,
            'minPrimerLen' : 18,
            'maxPrimerLen' : 22,
            'minTm' : 56,
            'maxTm' : 62,
            'max_repeat' : 4,
            'max_run' : 4,
            'primer_conc' : 50e-9,
            'salt_conc' : 0.05,

            # Self/Cross dimers
            'minMatch' : 4, 
            'dBases' : 4,
            'temp_dG' : 37,
            'minDimerDeltaG' : -11,
            'minAdaptorDeltaG' : -15.5,

            # Pair/Chain design params
            'deltaTm' : 3,
            'maxOverlap' : 0,

            # Adaptors
            'adaptors' : ['TACACGACGCTCTTCCGATCT', 'AGACGTGTGCTCTTCCGATCT'],

            # Other product
            'hg_match_file' : 'hg_matches',
            'mm_match_file' : 'mm_matches',

            # Design directories and names
            # primer_list_name' : 'excel_list_primers',
            'filedir.dir' : '/data2/fefuks/COMPASS/PrimersDesign/gg_201305_primers_multLen',
            'filedir.design_name' : 'FirstDesign',
            'filedir.primer_list_name' : 'gg_multLen_primers',
            }
