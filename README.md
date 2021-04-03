# AcidSphingomyelinase

This repository contains the data tables mentionned in the paper :
Ancien F., Pucci F., Rooman M., In silico analysis of the molecular-level impact of SMPD1variants on Niemann-Pick disease severity, *MDPI*, *in review process*

Statistical potentials mentioned in this file are explained in more details in :


## NiemannPick.ActivityInputData.csv
This file contains 66 variants with the input data needed by SMPD1-ZooM and the reported enzymatic activity in literature.
The file is comma-separated with line number, the columns names are described as follows:

- mutName: The mutation descriptor mapped to 3D protein structure numbering
- activity: Relative enzymatic activity of mutated SMPD1 (in %)
- Annotation: The phenotype associated with the variant. Unknown (U), Neutral (N), Disease causing (D), NPDA causing (A) or NPDB causing (B)
- sd: A statistical potential associated with spatial distance between residues (in kcal/mol)
- sds: A statistical potential associated with spatial distance between residues (in kcal/mol)
- sad: A statistical potential associated with spatial distance between residues and solvent accessibility (in kcal/mol)
- acc: Solvent accessibility of the wild-type residue
- ddG: Folding free energy variation upon mutation as calculated by PoPMuSiC (in kcal/mol)
- annScore: The deleteriousness score predicted by SNPMuSiC$_{SSS}$ (Deleterious if > 0)
- CARBOHYD: The spatial distance between variant and the nearest glycosylation site
- DISULFID: The spatial distance between variant and the closest cystein involved in a disufid bridge
- METAL: The spatial distance between variant and the nearest metal binding site
- DEOGEN_2_PREDICTION: The deleteriousness score predicted by DEOGEN2 (Deleterious if > 0.5)
- DEOGEN_2_PROVEAN_VALUE: The deleteriousness score predicted by PROVEAN (Deleterious if < -2.5)
- DEOGEN_2_CONSERVATION_INDEX: The conservation index at the variant position
- DEOGEN_2_PROBABILITY_VALUE: The log-odd ratio of this specific variant
- isChangingAromaticity: 1 if both or neither wild-type and mutant residues are aromatic, else 0

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
This file contains 266 variants with the input data on which the analysis in publication was done.
The file is comma-separated with line number, the columns names are described as follows:
- mutName: The mutation descriptor mapped to 3D protein structure numbering
- Annotation: The phenotype associated with the variant. Unknown (U), Neutral (N), Disease causing (D), NPDA causing (A) or NPDB causing (B)
- PROVEAN: The deleteriousness score predicted by PROVEAN (Deleterious if < -2.5)
- DEOGEN2: The deleteriousness score predicted by DEOGEN2 (Deleterious if > 0.5)
- SNPsss: The deleteriousness score predicted by SNPMuSiC$_{SSS}$ (Deleterious if > 0)
- PoPMuSiC: Folding free energy variation upon mutation as calculated by PoPMuSiC (in kcal/mol)
- Wst: A statistical potential associated with torsion angles between residues (in kcal/mol)
- Wstt: A statistical potential associated with torsion angles between residues (in kcal/mol)
- Wsst: A statistical potential associated with torsion angles between residues (in kcal/mol)
- Wsa: A statistical potential associated with solvent accessibility (in kcal/mol)
- Wsaa: A statistical potential associated with solvent accessibility (in kcal/mol)
- Wssa: A statistical potential associated with solvent accessibility (in kcal/mol)
- Wsta: A statistical potential associated with solvent accessibility and torsion angles between residues (in kcal/mol)
- Wsd: A statistical potential associated with spatial distance between residues (in kcal/mol)
- Wsds: A statistical potential associated with spatial distance between residues (in kcal/mol)
- Wsad: A statistical potential associated with spatial distance between residues and solvent accessibility (in kcal/mol)
- Wsadsa: A statistical potential associated with spatial distance between residues and solvent accessibility (in kcal/mol)
- Wstd: A statistical potential associated with spatial distance and torsion angles between residues (in kcal/mol)
- Wstdst: A statistical potential associated with spatial distance and torsion angles between residues (in kcal/mol)
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
This file contains SMPD1-Zoom predictions for all 266 variants in NiemannPick.InputData.csv.
Columns are described as follows:
- mutName: The mutation descriptor mapped to 3D protein structure numbering
- P(Neutral): The probability for the variant to be Neutral
- P(NPDA): The probability for the variant to be associated with NPDA
- P(NPDB): The probability for the variant to be associated with NPDB
- Prediction: The class given to the variant based on the highest probability

## NiemannPick.WholeProtein.InputData.csv
This file contains the data needed by SMPD1-ZooM to make a prediction for all possible variants in SMPD1 3D structure.
- mutName: The mutation descriptor mapped to 3D protein structure numbering
- sd: A statistical potential associated with spatial distance between residues (in kcal/mol)
- sds: A statistical potential associated with spatial distance between residues (in kcal/mol)
- sad: A statistical potential associated with spatial distance between residues and solvent accessibility (in kcal/mol)
- acc: Solvent accessibility of the wild-type residue
- ddG: Folding free energy variation upon mutation as calculated by PoPMuSiC (in kcal/mol)
- annScore: The deleteriousness score predicted by SNPMuSiC$_{SSS}$ (Deleterious if > 0)
- CARBOHYD: The spatial distance between variant and the nearest glycosylation site
- DISULFID: The spatial distance between variant and the closest cystein involved in a disufid bridge
- METAL: The spatial distance between variant and the nearest metal binding site
- DEOGEN_2_PREDICTION: The deleteriousness score predicted by DEOGEN2 (Deleterious if > 0.5)
- DEOGEN_2_PROVEAN_VALUE: The deleteriousness score predicted by PROVEAN (Deleterious if < -2.5)
- DEOGEN_2_CONSERVATION_INDEX: The conservation index at the variant position
- DEOGEN_2_PROBABILITY_VALUE: The log-odd ratio of this specific variant
- isChangingAromaticity: 1 if both or neither wild-type and mutant residues are aromatic, else 0

## NiemannPick.WholeProtein.Predictions.csv
This file contains SMPD1-Zoom predictions for all the variants in NiemannPick.WholeProtein.InputData.csv.
- mutName: The mutation descriptor mapped to 3D protein structure numbering
- P(Neutral): The probability for the variant to be Neutral
- P(NPDA): The probability for the variant to be associated with NPDA
- P(NPDB): The probability for the variant to be associated with NPDB
- Prediction: The class given to the variant based on the highest probability
