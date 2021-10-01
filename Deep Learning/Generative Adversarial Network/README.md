**Face Generation**

**GOAL**

To create a Generative Adversarial Network to generate Images of Faces.


**PURPOSE**

To understand the concept of Generative Adversarial Network

**DATASET** (if applicable)

<a href="https://www.kaggle.com/jessicali9530/celeba-dataset">Celeba Dataset</a>

**DESCRIPTION**

Basically in Generative Adversarial Network, there will be two architectures.
- Generator : Generates new data
- Discriminator (Critic) : Discriminates whether an input is real or fake

Input of Generator is random noise from which a new image of face will be generated.
Input of Discriminator is of two types :
- Output from Generator which is to be classified as Fake by Discriminator
- Original Data from Dataset which is to be classified as Real by Generator

The main aim for the Generator is to fool Discriminator by producing such an output so that Discriminator classifies the image as real.

**WORKFLOW OF YOUR PROJECT FILES**

- Import Dataset and Libraries
- Setting Parameters and Hyper-parameters
- Config with <a href="https://wandb.ai/home">wandb</a> (optional)
- Define Generator Architecture in Generator Class
- Define Critic Architecture in Critic Class
- Initialize Weights (Optional)
- Define function for gradient penalty calculation
- Define function for saving and loading checkpoints
- A cell for loading previously saved checkpoint
- Training Loop with loggin in wandb
- Cells to generate new faces

**USAGE**

I have choosed this issue specifically because I was impressed by the GeneratorDiscriminator Conflict.


**USE CASES**

- Used in Gaming Industry
- Text to Image Generation


**LIBRARIES USED**

- torch
- torchvision
- os
- PIL
- pdb
- tqdm
- numpy
- matplotlib
- wandb

**ADVANTAGES**

Unsupervised Learning will be the future of AI

**DISADVANTAGES**

None

**APPLICATIONS**

- Gaming Industry

**RESEARCH**

None

**SCREENSHOTS**

Here is the link of the wandb project I have done.
<a href="https://wandb.ai/avinash-218/Face_GAN/overview?workspace=user-avinash-218">Face Generation</a>

**CONCLUSION**

What's the conclusion of this concept. It should be clear and precise.
Also showcase the appropriate results derived if it's applicable. Be briefer.


**REFERENCES**

- Unsupervised Learning
- Generator Vs Discriminator

**YOUR NAME**

- Name : Avinash R
- LinkedIn : https://www.linkedin.com/in/avinash-r-2113741b1/
- GitHub : https://github.com/avinash-218
- Kaggle : https://www.kaggle.com/ravinash218
- Portfolio : https://avinash-218.github.io/avinash-portfolio-2/#profiles
