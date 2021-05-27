# AcidSphingomyelinase

This repository contains the data and predictions mentionned in the paper :
Ancien F., Pucci F., Rooman M., In silico analysis of the molecular-level impact of SMPD1 variants on Niemann-Pick disease severity, **Int. J. Mol. Sci.** 2021, 22(9), 4516

It also contains SMPD1_ZooM.py, a user-friendly program to predict the severity of the Niemann-Pick disease caused by SMPD1 variants, both for homozyhous and heterozygous individuals.

## SMPD1_ZooM.py

This tool predicts the phenotype associated to SMPD1 variants.
The predicted phenotypes are: "A" for Niemann-Pick disease of type A, "B" for Niemann-Pick disease of type B or "N" for neutral phenotype.


```
USAGE:
    python SMPD1_ZooM.py -var1 VAR1 [-var2 VAR2]

PARAMETERS:
    -var1:   A variant in the SMPD1 gene. If given alone, SMPD1-ZooM assumes homozygocy and
            predicts the phenotype of an individual having that variant on both alleles.
            This has to be an amino acid variant following the PDB 5i81 residue numbering (Mandatory).

    -var2:   A second variant in the SMPD1 gene. If present, SMPD1-ZooM assumes heterozygocy and
            predicts the phenotype of an individual having var1 on one allele and var2 on the
            other allele. (Optional)
```

## NiemannPick.ActivityInputData.csv
This file contains 69 variants with the non-standardized input data needed by SMPD1-ZooM and the enzymatic activity reported in literature.
The file is comma-separated. Both values for heterozygous cases are written in the same line, separated by a '/'.  The column names are described as follows:

- Mutation: The mutation descriptor mapped to 3D protein structure numbering
- RelativeActivity: Relative enzymatic activity of mutated SMPD1 (in %)
- Annotation: The phenotype associated with the variant. Unknown (U), Neutral (N), Disease causing (D), NPDA causing (A) or NPDB causing (B)
- ddWsd: ΔΔW<sub>sd</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues (in kcal/mol)
- ddWsds: ΔΔW<sub>sds</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues (in kcal/mol)
- ddWsad: ΔΔW<sub>sad</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues and solvent accessibility (in kcal/mol)
- Access: Solvent accessibility of the wild-type residue
- PoPMuSiC: Folding free energy variation upon mutation as calculated by PoPMuSiC (in kcal/mol)
- SNPsss: The deleteriousness score predicted by SNPMuSiC<sub>SSS</sub> (Deleterious if > 0)
- Carbohyd: The spatial distance between variant and the nearest glycosylation site
- Disulfide: The spatial distance between variant and the closest cystein involved in a disufid bridge
- Metal: The spatial distance between variant and the nearest metal binding site
- DEOGEN2: The deleteriousness score predicted by DEOGEN2 (Deleterious if > 0.5)
- PROVEAN: The deleteriousness score predicted by PROVEAN (Deleterious if < -2.5)
- EvolCI: The conservation index at the variant position
- EvolLOR: The log-odd ratio of this specific variant
- Aromatic: 1 if both or neither wild-type and mutant residues are aromatic, else 0

## NiemannPick.AllVariants.csv
This file contains the 309 missense SMPD1 variants extracted from Uniprot, ClinVar and INPDR, their annotations in the different databases and their
mutant and wild-type allele frequencies when available. The residue numbering used in this file (and only this file), is the UniProt numbering. An
additional column indicates the corresponding numbering in the PDB file 5i81 when the residue is part of the 3D structure

- Mutation: The mutation descriptor mapped to uniprot sequence numbering
- PDBMutation: The mutation descriptor mapped to structure sequence numbering, when mapping is possible.
- UniprotAnnotation: The annotation of this variant in Uniprot database. Unknown (U), Neutral (N), Disease causing (D), NPDA causing (A), NPDB causing (B) or not available (NA)
- ClinVarAnnotation: The annotation of this variant in ClinVar database. Unknown (U), Neutral (N), Disease causing (D), NPDA causing (A), NPDB causing (B) or not available (NA)
- InpdrAnnotation: The annotation of this variant in the INPDR database. Unknown (U), Neutral (N), Disease causing (D), NPDA causing (A), NPDB causing (B) or not available (NA)
- FinalAnnotation: The annotation used to train SMPD1-ZooM. See paper for the description on how this annotation was obtained.
- mutantAF (nuc/aa): The mutant allele frequency with, between parentheses, the mutant nucleotide and mutant residue associated. UN when global value was unavailble on dbSNP.
- wild-typeAF (nuc/aa): The wild-type allele frequency with, between parentheses, the wild-type nucleotide and wild-type residue associated. UN when global value was unavailble on dbSNP.
- Source: The source of the allele frequency as reported by dbSNP. Allele Frequencies Aggregator (ALFA), Genome Aggregation Database - Exomes (gnomAD-E), Haplotype Map (HapMap) or Exome Aggregation Consortium (ExAC).
- rsid: The variant identifier on dbSNP where the variant frequencies were obtained.

## NiemannPick.InputData.csv
This file contains 266 SMPD1 missense variants which are covered by the 3D structure, on which our analysis is based.
The data is non-standardized, the columns names are described as follows:
- Mutation: The mutation descriptor mapped to 3D protein structure numbering
- Annotation: The phenotype associated with the variant. Unknown (U), Neutral (N), Disease causing (D), NPDA causing (A) or NPDB causing (B)
- PROVEAN: The deleteriousness score predicted by PROVEAN (Deleterious if < -2.5)
- DEOGEN2: The deleteriousness score predicted by DEOGEN2 (Deleterious if > 0.5)
- SNPsss: The deleteriousness score predicted by SNPMuSiC<sub>SSS</sub> (Deleterious if > 0)
- PoPMuSiC: Folding free energy variation upon mutation as calculated by PoPMuSiC (in kcal/mol)
- ddWst: ΔΔW<sub>st</sub>, the variation of energy linked to a statistical potential associated with torsion angles between residues (in kcal/mol)
- ddWstt: ΔΔW<sub>stt</sub>, the variation of energy linked to a statistical potential associated with torsion angles between residues (in kcal/mol)
- ddWsst: ΔΔW<sub>sst</sub>, the variation of energy linked to a statistical potential associated with torsion angles between residues (in kcal/mol)
- ddWsa: ΔΔW<sub>sa</sub>, the variation of energy linked to a statistical potential associated with solvent accessibility (in kcal/mol)
- ddWsaa: ΔΔW<sub>saa</sub>, the variation of energy linked to a statistical potential associated with solvent accessibility (in kcal/mol)
- ddWssa: ΔΔW<sub>ssa</sub>, the variation of energy linked to a statistical potential associated with solvent accessibility (in kcal/mol)
- ddWsta: ΔΔW<sub>sta</sub>, the variation of energy linked to a statistical potential associated with solvent accessibility and torsion angles between residues (in kcal/mol)
- ddWsd: ΔΔW<sub>sd</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues (in kcal/mol)
- ddWsds: ΔΔW<sub>sds</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues (in kcal/mol)
- ddWsad: ΔΔW<sub>sad</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues and solvent accessibility (in kcal/mol)
- ddWsadsa: ΔΔW<sub>sadsa</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues and solvent accessibility (in kcal/mol)
- ddWstd: ΔΔW<sub>std</sub>, the variation of energy linked to a statistical potential associated with spatial distance and torsion angles between residues (in kcal/mol)
- ddWstdst: ΔΔW<sub>stdst</sub>, the variation of energy linked to a statistical potential associated with spatial distance and torsion angles between residues (in kcal/mol)
- Access: Solvent accessibility of the wild-type residue
- DeltaV: The volume difference between wild-type and mutant residues
- EvolCI: The conservation index at the variant position
- EvolLOR: The log-odd ratio of this specific variant
- EarlyF: Prediction score of whether the mutated residue is in an early-folded region
- PFAM: Log-odd ratio of deleterious/neutral variant frequency in the PFAM domain
- Saposin: 1 if variant is located in SMPD1 saposin domain, else 0
- Linker:  1 if variant is located in SMPD1 prolin-rich linker, else 0
- Catalytic: 1 if variant is located in SMPD1 catalytic domain, else 0
- Disulfide: The spatial distance between variant and the closest cystein involved in a disufid bridge
- Metal: The spatial distance between variant and the nearest metal binding site
- Carbohyd: The spatial distance between variant and the nearest glycosylation site
- Aromaticity: 1 if both or neither wild-type and mutant residues are aromatic, else 0
- Polarity: 1 if both wild-type and mutant residues are polar and uncharged, else 0 (CHECK) 
- Charge: 1 if both wild-type and mutant residues have the same charge, else 0


## NiemannPick.Predictions.csv
This file contains the SMPD1-Zoom predictions for the 130 variants in the SMPD1 3D structure with annotation N, A or B.
Columns are described as follows:
- Mutation: The mutation descriptor mapped to 3D protein structure numbering
- P(Neutral): The probability for the variant to be Neutral
- P(NPDA): The probability for the variant to be associated with NPDA
- P(NPDB): The probability for the variant to be associated with NPDB
- Prediction: The class given to the variant based on the highest probability

## NiemannPick.WholeProtein.InputData.csv
This file contains the data needed by SMPD1-ZooM to make a prediction for all possible variants in the SMPD1 3D structure.
- Mutation: The mutation descriptor mapped to 3D protein structure numbering
- ddWsd: ΔΔW<sub>sd</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues (in kcal/mol)
- ddWsds: ΔΔW<sub>sds</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues (in kcal/mol)
- ddWsad: ΔΔW<sub>sad</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues and solvent accessibility (in kcal/mol)
- Access: Solvent accessibility of the wild-type residue
- PoPMuSiC: Folding free energy variation upon mutation as calculated by PoPMuSiC (in kcal/mol)
- SNPMuSiCsss: The deleteriousness score predicted by SNPMuSiC<sub>SSS</sub> (Deleterious if > 0)
- Carbohyd: The spatial distance between variant and the nearest glycosylation site
- Disulfide: The spatial distance between variant and the closest cystein involved in a disufid bridge
- Metal: The spatial distance between variant and the nearest metal binding site
- DEOGEN2: The deleteriousness score predicted by DEOGEN2 (Deleterious if > 0.5)
- PROVEAN: The deleteriousness score predicted by PROVEAN (Deleterious if < -2.5)
- EvolCI: The conservation index at the variant position
- EvolLOR: The log-odd ratio of this specific variant
- Aromatic: 1 if both or neither wild-type and mutant residues are aromatic, else 0

## NiemannPick.WholeProtein.Predictions.csv
This file contains SMPD1-Zoom predictions for all the variants in NiemannPick.WholeProtein.InputData.csv.
Columns are described as follows:
- Mutation: The mutation descriptor mapped to 3D protein structure numbering
- P(Neutral): The probability for the variant to be Neutral
- P(NPDA): The probability for the variant to be associated with NPDA
- P(NPDB): The probability for the variant to be associated with NPDB
- Prediction: The class given to the variant based on the highest probability
