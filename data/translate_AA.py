import argparse
import numpy as np
import pandas as pd

def main(in_file, ref_aa_file, out_file):

    # Example reference AA
    # CTRPGNK-IR--R--RIH---I--GPGRAFYT-----DR-VG---D---IRQAYC

    ref_aa = []
    with open(ref_aa_file, 'r') as fp:
        for line in fp:
            # Remove new line
            line = line[:-1]
            # Convert string into a list of characters
            ref_aa = [character for character in line]

    num_aa = len(ref_aa)
    print("num_aa: {}".format(num_aa)) 
    print("ref_aa[num_aa - 1]: {}".format(ref_aa[num_aa - 1])) 
    print("ref_aa[num_aa - 2]: {}".format(ref_aa[num_aa - 2])) 

    num_gaps = 0
    reduce_positions = np.zeros(num_aa)

    for idx in range(num_aa):       
        if ref_aa[idx] == '-':
            num_gaps = num_gaps + 1
        else:
            reduce_positions[idx] = num_gaps 

    print("num_gaps: {}".format(num_gaps))
    print("reduce_positions: {}".format(reduce_positions))

    in_df = pd.read_csv(in_file, sep="\t")
    print(in_df.head())    
    print(in_df.tail())    

    # Deduct 1 as the paper we use for comparison used 0 indexing
    in_df['Position'] = in_df['Position'].apply(lambda x: x - reduce_positions[x-1] - 1).astype(int)

    print(in_df.head())    
    print(in_df.tail())    

    in_df.to_csv(out_file, sep="\t", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    # Required positional argument
    parser.add_argument('--in_file', type=str, help='Input file with un-translated positions', required=True)
    parser.add_argument('--ref_aa_file', type=str, help='Reference Amino Acid file', required=True)
    parser.add_argument('--out_file', type=str, help='Output file with translated positions', required=True)
    args = parser.parse_args()
    main(in_file=args.in_file, ref_aa_file=args.ref_aa_file, out_file=args.out_file)	
