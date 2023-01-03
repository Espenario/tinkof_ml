import argparse
import ast

from file_normalization import FileOptimizer
from plagiat_detection import PlagiatScanner

def main():
    parser = argparse.ArgumentParser(description="Antiplagiat tool")
    parser.add_argument(
        "--input", default="input.txt",
        help="Path to the file with pairs of files to compare",
    )
    parser.add_argument(
        "--scores", default="scores.txt",
        help="Path to the result file",
    )
    args = parser.parse_args()

    with open(args.input, mode="r", encoding="utf-8") as file:
        pairs = file.read().rstrip().split('\n')

    score_list = []
    #print(pairs)

    for pair in pairs:
        #print(pair)
        file1 = pair.split(' ')[0]
        file2 = pair.split(' ')[1]

        with open(file1, mode="r", encoding="utf-8") as f:
            code1_before = f.read()
        with open(file2, mode="r", encoding="utf-8") as f:
            code2_before = f.read()

        tree1_before_opt = ast.parse(code1_before)
        tree2_before_opt = ast.parse(code2_before)

        optimizer1 = FileOptimizer()
        optimizer2= FileOptimizer()

        tree1_after_opt = optimizer1.visit(tree1_before_opt)
        tree2_after_opt = optimizer2.visit(tree2_before_opt)

        code1_after = ast.unparse(tree1_after_opt)
        code2_after = ast.unparse(tree2_after_opt)

        plagiat_scanner = PlagiatScanner(code1_after, code2_after)
        
        score_list.append(round(plagiat_scanner.compute_Levenshtein_distance()/ ((len(code1_after) + len(code2_after)) / 2), 4))
    
    with open(args.scores, mode="w", encoding="utf-8") as file:
        file.write('\n'.join(str(x) for x in score_list))



if __name__ == "__main__":
    main()
