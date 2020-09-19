# Project-Airfoil-Optmization
The premise for developing an airfoil optimizer was to provide a free easy to use .exe program to users. 

The program uses Xfoil as the primary flow solver. The program is not only restricted to just the subsonic flow that Xfoil is hailed for. Other solvers such as MSES or a Naiver-Stokes solver may be used to solve complex flows and even supersonic flows. Multiple programs will be available for download with a unique solver built in.

The software requires the parameterization of airfoils. A few analytical solutions were tried before converging onto PARSEC. PARSEC parameterizes an airfoil into 11 different variables. The advantage of PARSEC is the set of equations that are used to describe the upper and lower airfoil surface coordinates lending in its ease to code. 

The optimizer itself is made up of two components: the gradient based optimizer and the genetic algorithm optimizer. The gradient based optimizer optimizes the airfoil in the "direction" where L/D is maximized. Once the maximum L/D is reached the gradient-based algorithm is swapped for the genetic algorithm. The genetic algorithm simulates two airfoils to determine which is better. The better airfoil is given the priority and placed on a line known as the Pareto front. The airfoil that is given priority is the airfoil that performs the best under a certain set of conditions when only one variable is changed. 

The program is currently under development and should be available in a few weeks.
