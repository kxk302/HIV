import argparse
import numpy as np
import pandas as pd

def main(in_file, out_file):

    alignments = []
    with open(in_file, 'r') as fp:
        for line in fp:
            # Skip the header lines
            if not line.startswith('>'):
                # Remove new line
                line = line[:-1]
                # Convert string into a list of characters
                line = [character for character in line]
                alignments.append(line)

    num_alignments = len(alignments)
    num_nucleotides = len(alignments[0])

    df = pd.DataFrame(alignments)

    num_rows = df.shape[0]
    num_cols = df.shape[1]
    print("num_rows: {}, num_cols: {}".format(num_rows, num_cols))

    # Columns that have a gap ('-' char) in them 
    bad_cols = df.columns[(df == '-').any()]
    print(bad_cols)

    # Drop columns that have a gap in them
    df = df.drop(columns=df.columns[(df == '-').any()])

    num_rows = df.shape[0]
    num_cols = df.shape[1]
    print("num_rows: {}, num_cols: {}".format(num_rows, num_cols))

    # Creates a empty output file. 
    # Just add the header here.
    # Rows get appended in loop below
    with open(out_file, 'w') as fp:
        fp.write("Sample\tAminoAcid\tPosition\n") 

    rows = []
    for idx in range(num_cols):
        vc = df.iloc[:, idx].value_counts()
        # position starts from 1
        position = df.columns[idx] + 1
        
        # 20 amino acids
        # Column order: A R N D C Q E G H I L K M F P S T W Y V
        row = []
        row.append(vc.get('A', 0))
        row.append(vc.get('R', 0))
        row.append(vc.get('N', 0))
        row.append(vc.get('D', 0))
        row.append(vc.get('C', 0))
        row.append(vc.get('Q', 0))
        row.append(vc.get('E', 0))
        row.append(vc.get('G', 0))
        row.append(vc.get('H', 0))
        row.append(vc.get('I', 0))
        row.append(vc.get('L', 0))
        row.append(vc.get('K', 0))
        row.append(vc.get('M', 0))
        row.append(vc.get('F', 0))
        row.append(vc.get('P', 0))
        row.append(vc.get('S', 0))
        row.append(vc.get('T', 0))
        row.append(vc.get('W', 0))
        row.append(vc.get('Y', 0))
        row.append(vc.get('V', 0))

        ignore_pos = any(ele == num_rows for ele in row)
        if ignore_pos:
            continue

        pos_df = pd.DataFrame({ df.columns.values.tolist()[idx] : df.copy().iloc[:,idx]})
        pos_df.insert(1, "Position", position)
        pos_df.to_csv(out_file, mode='a', header=False, sep="\t")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    # Required positional argument
    parser.add_argument('--in_file', type=str, help='File to preprocess', required=True)
    parser.add_argument('--out_file', type=str, help='Save preprocessing result to this file', required=True)
    args = parser.parse_args()
    main(in_file=args.in_file, out_file=args.out_file)	
