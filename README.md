# Overview 

This repository has 6 main files: 

* `Problem_3.py` and `Problem_9.py`: 

These files contain the 2 problems that showed lowest line and branch coverage in HW2. It also incudes NLP Problem Description, Original Solution, Prompt used for generating specifications and the generated specifications. 

* `test_problem_3_baseline.py` and `test_problem_9_baseline.py`: 

These files contain the original test cases that were used in HW2. 

To get line and branch overage for Problem 3: 
```bash
pytest test_problem_3_baseline.py --cov=Problem_3 --cov-report=term-missing --cov-branch
```

To get line and branch overage for Problem 9: 
```bash
pytest test_problem_9_baseline.py --cov=Problem_9 --cov-report=term-missing --cov-branch
```

* `test_problem_3_specifications.py` and `test_problem_9_specifications.py`:

These files contain the original test cases as well as the LLM-generated specification guides test cases. 

To get line and branch overage for Problem 3: 
```bash
pytest test_problem_3_specifications.py --cov=Problem_3 --cov-report=term-missing --cov-branch
```

To get line and branch overage for Problem 9: 
```bash
pytest test_problem_9_specifications.py --cov=Problem_9 --cov-report=term-missing --cov-branch
```

The results and comparisons are provided in the report. 
