#!/bin/bash

JAVA=/usr/bin/java
FASTA=/Users/kxk302/workspace/HIV/HIV_V3.fas
MACSE=/Users/kxk302/workspace/HIV/macse_v2.05.jar

echo $JAVA -jar $MACSE -prog alignSequences -seq $FASTA -local_realign_init 1 -local_realign_dec 1 -out_NT $FASTA"_codon_macse.fas" -out_AA $FASTA"_AA_macse.fas"

$JAVA -jar $MACSE -prog alignSequences -seq $FASTA -local_realign_init 1 -local_realign_dec 1 -out_NT $FASTA"_codon_macse.fas" -out_AA $FASTA"_AA_macse.fas"

exit 0
