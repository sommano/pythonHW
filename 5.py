import math


from anytree import Node, RenderTree
import sys
sys.path.append('../common')
import common
import decision_tree


csv_file_name = sys.argv[1]
verbose = int(sys.argv[2])  # verbosity level, 0 - only decision tree


(heading, complete_data, incomplete_data,
 enquired_column) = common.csv_file_to_ordered_data(csv_file_name)

tree = decision_tree.constuct_decision_tree(
    verbose, heading, complete_data, enquired_column)
decision_tree.display_tree(tree)
