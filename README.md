## 🍌Beat Banana Collectors with Deep Q-learning 🍌

### 1. Project environment
This implementation concearns the unity environment "Banana Collectors", the goal of the game is for the agent to navigate the environment space, collecting as many yellow bananas as possible while avoiding blue bananas. A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. The actions are:
* 0 to move forward
* 1 to move backward
* 2 to turn left
* 3 to turn right

The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.

### 2. Requirements
In order to run the scripts of this project you must follow the following instructions.
#### Step 1: Clone the Course Repository
1. Create (and activate) a new environment with Python 3.6.

	- __Linux__ or __Mac__: 
	```bash
	conda create --name drlnd python=3.6
	source activate drlnd
	```
	- __Windows__: 
	```bash
	conda create --name drlnd python=3.6 
	activate drlnd
	```
	
2. Follow the instructions in [this repository](https://github.com/openai/gym) to perform a minimal install of OpenAI gym.  
	- Install the **box2d** environment group by following the instructions [here](https://github.com/openai/gym#box2d).
	
3. Clone the repository (if you haven't already!), and navigate to the `python/` folder.  Then, install several dependencies.
```bash
git clone https://github.com/udacity/Value-based-methods.git
cd Value-based-methods/python
pip install .
```

4. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `drlnd` environment.  
```bash
python -m ipykernel install --user --name drlnd --display-name "drlnd"
```

5. Before running code in a notebook, change the kernel to match the `drlnd` environment by using the drop-down `Kernel` menu. 
#### Step 2: Download the Unity Environment
For this project, you will not need to install Unity - this is because we have already built the environment for you, and you can download it from one of the links below. You need only select the environment that matches your operating system:

- Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip).
- Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
- Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
- Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

Then, place the file in the p1_navigation/ folder in the course GitHub repository, and unzip (or decompress) the file.

## 3. Run the code
One can **train**, **evaluate** and **watch** the agent using the jupyter notebook "Navigation.ipynb"
#### File descrpition
- "Navigation.ipynb" contains the fully described implementation in this jupyter notebook file.
- "model.py" contains the class of the neural network architecture that is used in this implementation (a simple multilayer perceptron).
- "rl_agent.py" contains the Agent class which is responsible for creating an agent that can explore and learn the game using Deep Q-learning. Here, we set the hyperparameters for the neural network (e.g. hidden layer size, activation functions).
- "trained_model.pth" contains the neural network weights of a trained agent that can be passed directly to evaluate the agent or watch the agent play the game. 

Both the **evaluation** and agent **demonstration** can be found inside the jupyter notebook with the related instructions before each cell.

#### And here is a little sneak peek:
![alt text](agent copy.gif)




