import numpy as np
import cv2
import colour
import pyomo.environ as pyo

# Load images and preprocess
image = cv2.imread('sample_2.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

l, w, _ = image.shape
image_ref = cv2.imread('sample_1.jpg')
image_ref = cv2.resize(image_ref, (w,l))
image_ref = cv2.cvtColor(image_ref, cv2.COLOR_BGR2RGB)

# Define a Python function to compute Delta E outside of Pyomo
def compute_delta_E(x1, x2, x3):
    image_recon = image.copy()
    image_recon[:,:,0] = image_recon[:,:,0] * x1
    image_recon[:,:,1] = image_recon[:,:,1] * x2
    image_recon[:,:,2] = image_recon[:,:,2] * x3  

    image_recon = np.clip(image_recon, 0, 255).astype(np.uint8)
    image1_lab = cv2.cvtColor(image_ref, cv2.COLOR_RGB2Lab)
    image2_lab = cv2.cvtColor(image_recon, cv2.COLOR_RGB2Lab)  

    delta_E = np.sum(colour.delta_E(image1_lab, image2_lab, method='CIE 2000'))
    return delta_E

# Register the external function with Pyomo
pyo_compute_delta_E = pyo.ExternalFunction(compute_delta_E)

# Define your Pyomo model
model = pyo.ConcreteModel()

# Define the decision variables
model.x = pyo.Var([1,2,3], domain=pyo.NonNegativeReals, bounds=(0, 3))

# Define the objective function to call the external function
def objective_rule(model):
    return pyo_compute_delta_E(model.x[1], model.x[2], model.x[3])
model.OBJ = pyo.Objective(rule=objective_rule, sense=pyo.minimize)

'''
# Define the solver and solve the model
solver = pyo.SolverFactory('gurobi') # ipopt handles non-linear problems well

result = solver.solve(model)

# After solving the model, get the optimal scalar values
optimal_scalars = [pyo.value(model.x[i]) for i in range(1, 4)]

print('Optimal Scalars:', optimal_scalars)
'''