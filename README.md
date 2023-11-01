# Query Refinement for Diversity Constraint Satisfaction

## Abstract
Diversity, group representation, and similar needs often apply to query results, which in turn require constraints on the sizes of various subgroups in the result set. Traditional relational queries only specify conditions as part of the query predicate(s) and do not support such restrictions on the output. In this paper, we study the problem of modifying queries to have the result satisfy constraints on the sizes of multiple subgroups in it. This problem, in the worst case, cannot be solved in polynomial time. Yet, with the help of provenance annotation, we are able to develop a query refinement method that works quite efficiently, as we demonstrate through extensive experiments. 


## Algorithms

- Baseline Algorithm (Baseline): This naive algorithm utilizes a provenance model to avoid multiple database accesses. However, it identifies minimal refinements by navigating through all potential refinements. Script can be found in Algorithm/LatticeTraversal_4_20220901.py.
- PVL-based Search (PS): This is algorithm with all optimizations to identify minimal refinements with PVL. Script can be found in Algorithm/ProvenanceSearchValues_8_20230119.py
- PVL-based Search without optimization (PS\_no\_opt): This version is our proposed approach but without the optimizations. Script can be found in Algorithm/ProvenanceSearchValues_8_no_optimization.py

## Datasets

In folder InputData.


## How to run experiments
run any .py file under folder Experiment


## Where to find the paper
Our technical report can be found at FullPaper/Query_Refinement.pdf

## Demo paper
Demo paper is accepted by VLDB 2023: https://dl.acm.org/doi/abs/10.14778/3611540.3611623 

Demo system: https://github.com/alons9911/Query_refinement
