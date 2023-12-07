# Setup
To setup the training and testing environment, first clone the repository:
```bash
git clone https://github.com/AlexWan0/cs182_final_project.git
```

Then, create the conda environment:
```bash
conda env create -f environment.yml
```

Note that CUDA is required to run these experiments.

# Training
To run with the full hyperparameter sweep (i.e., epochs, LR, and datasets), simply run:
```bash
python model.py
```

Due to resource limitations, a "debug" version is enabled by default.

# Evaluate
To run the entire set of psychometric tests, simply run:
```bash
python eval.py
```

The full set of 160 checkpoints is unfortunately too cost-prohibitive to distribute (and impractical for reviewers/graders to run). We instead distribute a subset of these checkpoints. We additionally provide a Colab notebook to run these checkpoints.

The checkpoints can be found here.
The Colab notebook can be found here (make sure the GPU runtime is enabled).

# Plots
The plots can be reproduced using the `plots.ipynb` and `lossplots.ipynb` notebooks.
