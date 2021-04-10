# AcidSphingomyelinase

This repository contains the data tables mentionned in the paper :
Ancien F., Pucci F., Rooman M., In silico analysis of the molecular-level impact of SMPD1variants on Niemann-Pick disease severity, *MDPI*, *in review process*

It also contains SMPD1_ZooM.py, a user-friendly program to predict the deleteriousness of variants in SMPD1 structure for homozyhous and heterozygous patients.

## SMPD1_ZooM.py

This tool is used to predict the phenotype related to variants in the SMPD1 gene.
The predicted phenotype is either "A" for Niemann-Pick disease type A, "B" for Niemann-Pick disease type B
or "N" for a neutral phenotype.

```
USAGE:
    python SMPD1_ZooM.py -var1 VAR1 [-var2 VAR2]

PARAMETERS:
    -var1:   A variant in the SMPD1 gene. If given alone, SMPD1-ZooM will consider homozygocy and
            predict the phenotype of a person holding that variant on both alleles.
            This has to be a proteic variant following the PDB 5i81 residue numbering (i.e W84C for example)
            Synonymous variants (like W84W) are accepted (Mandatory).

    -var2:   A second variant in the SMPD1 gene. If given, SMPD1-ZooM will consider heterozygocy and
            predict the phenotype of a person holding both variants in their allele. (Optional)
```

## NiemannPick.ActivityInputData.csv
This file contains 69 variants with the non-standardized input data needed by SMPD1-ZooM and the reported enzymatic activity in literature.
The file is comma-separated. Both values for heterozygous cases are written in the same line, separated by a '/'.  The columns names are described as follows:

- MutName: The mutation descriptor mapped to 3D protein structure numbering
- Activity: Relative enzymatic activity of mutated SMPD1 (in %)
- Annotation: The phenotype associated with the variant. Unknown (U), Neutral (N), Disease causing (D), NPDA causing (A) or NPDB causing (B)
- Wsd: ΔΔW<sub>sd</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues (in kcal/mol)
- Wsds: ΔΔW<sub>sds</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues (in kcal/mol)
- Wsad: ΔΔW<sub>sad</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues and solvent accessibility (in kcal/mol)
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
This file contains the 309 exomic single nucleotide variants extracted from Uniprot, ClinVar and INPDR.
Those variants are described in term of their annotations in the different databases and their mutant and wild-type allele frequencies when available.

- MutName: The mutation descriptor mapped to uniprot sequence numbering
- UniprotAnnotation: The annotation of this variant in Uniprot database. Unknown (U), Neutral (N), Disease causing (D), NPDA causing (A), NPDB causing (B) or not available (NA)
- ClinVarAnnotation: The annotation of this variant in ClinVar database. Unknown (U), Neutral (N), Disease causing (D), NPDA causing (A), NPDB causing (B) or not available (NA)
- InpdrAnnotation: The annotation of this variant in the INPDR database. Unknown (U), Neutral (N), Disease causing (D), NPDA causing (A), NPDB causing (B) or not available (NA)
- FinalAnnotation: The annotation used to train SMPD1-ZooM. See paper for the description on how this annotation was obtained.
- mutantAF (nuc/aa): The mutant allele frequency with, between parentheses, the mutant nucleotide and mutant residue associated. UN when global value was unavailble on dbSNP.
- wild-typeAF (nuc/aa): The wild-type allele frequency with, between parentheses, the wild-type nucleotide and wild-type residue associated. UN when global value was unavailble on dbSNP.
- Source: The source of the allele frequency as reported by dbSNP. Allele Frequencies Aggregator (ALFA), Genome Aggregation Database - Exomes (gnomAD-E), Haplotype Map (HapMap) or Exome Aggregation Consortium (ExAC).
- rsid: The variant identifier on dbSNP where the variant frequencies were obtained.

## NiemannPick.InputData.csv
This file contains 266 variants with the non-standardized input data on which the analysis in publication was done.
The file is comma-separated with line number, the columns names are described as follows:
- mutName: The mutation descriptor mapped to 3D protein structure numbering
- Annotation: The phenotype associated with the variant. Unknown (U), Neutral (N), Disease causing (D), NPDA causing (A) or NPDB causing (B)
- PROVEAN: The deleteriousness score predicted by PROVEAN (Deleterious if < -2.5)
- DEOGEN2: The deleteriousness score predicted by DEOGEN2 (Deleterious if > 0.5)
- SNPsss: The deleteriousness score predicted by SNPMuSiC<sub>SSS</sub> (Deleterious if > 0)
- PoPMuSiC: Folding free energy variation upon mutation as calculated by PoPMuSiC (in kcal/mol)
- Wst: ΔΔW<sub>st</sub>, the variation of energy linked to a statistical potential associated with torsion angles between residues (in kcal/mol)
- Wstt: ΔΔW<sub>stt</sub>, the variation of energy linked to a statistical potential associated with torsion angles between residues (in kcal/mol)
- Wsst: ΔΔW<sub>sst</sub>, the variation of energy linked to a statistical potential associated with torsion angles between residues (in kcal/mol)
- Wsa: ΔΔW<sub>sa</sub>, the variation of energy linked to a statistical potential associated with solvent accessibility (in kcal/mol)
- Wsaa: ΔΔW<sub>saa</sub>, the variation of energy linked to a statistical potential associated with solvent accessibility (in kcal/mol)
- Wssa: ΔΔW<sub>ssa</sub>, the variation of energy linked to a statistical potential associated with solvent accessibility (in kcal/mol)
- Wsta: ΔΔW<sub>sta</sub>, the variation of energy linked to a statistical potential associated with solvent accessibility and torsion angles between residues (in kcal/mol)
- Wsd: ΔΔW<sub>sd</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues (in kcal/mol)
- Wsds: ΔΔW<sub>sds</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues (in kcal/mol)
- Wsad: ΔΔW<sub>sad</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues and solvent accessibility (in kcal/mol)
- Wsadsa: ΔΔW<sub>sadsa</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues and solvent accessibility (in kcal/mol)
- Wstd: ΔΔW<sub>std</sub>, the variation of energy linked to a statistical potential associated with spatial distance and torsion angles between residues (in kcal/mol)
- Wstdst: ΔΔW<sub>stdst</sub>, the variation of energy linked to a statistical potential associated with spatial distance and torsion angles between residues (in kcal/mol)
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
This file contains SMPD1-Zoom predictions for the 130 variants in SMPD1 3D structure for which annotation is either N, A or B.
Columns are described as follows:
- mutName: The mutation descriptor mapped to 3D protein structure numbering
- P(Neutral): The probability for the variant to be Neutral
- P(NPDA): The probability for the variant to be associated with NPDA
- P(NPDB): The probability for the variant to be associated with NPDB
- Prediction: The class given to the variant based on the highest probability

## NiemannPick.WholeProtein.InputData.csv
This file contains the data needed by SMPD1-ZooM to make a prediction for all possible variants in SMPD1 3D structure.
- MutName: The mutation descriptor mapped to 3D protein structure numbering
- Wsd: ΔΔW<sub>sd</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues (in kcal/mol)
- Wsds: ΔΔW<sub>sds</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues (in kcal/mol)
- Wsad: ΔΔW<sub>sad</sub>, the variation of energy linked to a statistical potential associated with spatial distance between residues and solvent accessibility (in kcal/mol)
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

## NiemannPick.WholeProtein.Predictions.csv
This file contains SMPD1-Zoom predictions for all the variants in NiemannPick.WholeProtein.InputData.csv.
Columns are described as follows:
- mutName: The mutation descriptor mapped to 3D protein structure numbering
- P(Neutral): The probability for the variant to be Neutral
- P(NPDA): The probability for the variant to be associated with NPDA
- P(NPDB): The probability for the variant to be associated with NPDB
- Prediction: The class given to the variant based on the highest probability
