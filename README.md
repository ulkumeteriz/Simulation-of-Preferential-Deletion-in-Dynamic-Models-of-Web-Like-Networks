# Simulation of Preferential Deletion in Dynamic Models of Web-Like Networks
Simulation of the proposed idea in paper https://www.sciencedirect.com/science/article/pii/S0020019006003632

The idea of birth and death processes proposed in the paper are simulated and findings are verified. The resulting datasets obtained from simulation are written into results.txt and figure5.txt files. According to data in the text files, graphs are drawn.

To draw graphs, you have to install pyplot in your local system. You can find the instructions [here](https://matplotlib.org/users/installing.html)

**To run simulator by using Makefile:**
	
	$ make simulate
	
**To draw graphs by using Makefile:**
	
	$ make draw
	
**To run simulator manually:**

	$ python Simulator.py
	
**To draw graphs manually:**

	$ python3 DrawGraphs.py