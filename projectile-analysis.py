#python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# --- 1. INITIAL SETTINGS AND CONSTANTS ---
# Style

def sm():
    plt.minorticks_on()
    plt.tick_params(axis='both',which='minor', direction = "in",top = True,right = True, length=5,width=1,labelsize=15)
    plt.tick_params(axis='both',which='major', direction = "in",top = True,right = True, length=8,width=1,labelsize=15)
    plt.tick_params(axis='both',which='minor', direction = "in",bottom = True,right = True, length=5,width=1,labelsize=15)
    plt.tick_params(axis='both',which='major', direction = "in",bottom = True,right = True, length=8,width=1,labelsize=15)

#Style:
# Physical constants
g = 9.81  # Gravitational acceleration (m/s^2)

# Experiment parameters (INSERT YOUR VALUES HERE)
h0 = 0.85  # Height of the table/ramp (m). Example: 85 cm = 0.85 m

# --- 2. EXPERIMENTAL DATA (REPLACE WITH YOUR DATA) ---
#
# ATTENTION: These are EXAMPLE data.
# The code simulates data that follow Model 2 + a small random error.
#
# Insert the values of 'h' (launch height on the ramp) in meters
h_exp = np.array([
    0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20
])

# Insert the values of 'A' (measured range) in meters
# FAKE DATA (FOR EXAMPLE PURPOSES):
A_exp_example = (np.sqrt(20/7) * np.sqrt(h0 * h_exp)) + (np.random.rand(len(h_exp)) * 0.02 - 0.01)
#
# INSERT YOUR REAL RANGE DATA 'A' HERE:
# Example: A_exp = np.array([0.15, 0.21, 0.26, ...])
A_exp = A_exp_example  # <- REPLACE "A_exp_example" WITH YOUR DATA


# --- 3. CALCULATIONS AND ANALYSIS (NO NEED TO MODIFY) ---

# The model is A = (slope) * sqrt(h).
# We will linearize the graph by plotting A vs. sqrt(h).
x_exp = np.sqrt(h_exp)  # Our X-axis will be sqrt(h)
y_exp = A_exp           # Our Y-axis will be A

# 3.1. Linear Fit (Linear Regression) of the data
# np.polyfit(x, y, 1) returns [slope, intercept]
slope_exp, intercept_exp = np.polyfit(x_exp, y_exp, 1)

# 3.2. THEORETICAL SLOPES
# Model 1 (Point Mass): A = (2*sqrt(h0)) * sqrt(h)
slope_model1 = 2 * np.sqrt(h0)

# Model 2 (Rigid Body): A = (sqrt(20/7)*sqrt(h0)) * sqrt(h)
slope_model2 = np.sqrt(20/7) * np.sqrt(h0)


# --- 4. GRAPH GENERATION (FIGURE 3 FROM THE PAPER) ---

# Create a smooth set of X (sqrt(h)) points to plot the theoretical lines
x_theoretical = np.linspace(min(x_exp), max(x_exp), 100)

# Compute Y values for each line
y_model1 = slope_model1 * x_theoretical       # Model 1 line
y_model2 = slope_model2 * x_theoretical       # Model 2 line
y_best_fit = slope_exp * x_theoretical + intercept_exp  # Experimental best-fit line

# Example uncertainty array (same value for all)
uncertainty_A = 0.005  # 5 millimeters
A_error = np.full_like(A_exp, uncertainty_A)

# Create the figure
plt.figure(figsize=(10, 7))

# Plot experimental data as points with error bars
plt.errorbar(
    x_exp,
    y_exp,
    yerr=A_error,      # Uncertainty in Y
    fmt='ko',          # 'ko' = black circles
    capsize=5,         # Adds caps on the error bars
    label='Experimental Data'
)

# Plot model lines
plt.plot(x_theoretical, y_model1, 'b--', label='Model 1 (Point Mass)')     # 'b--' = blue dashed
plt.plot(x_theoretical, y_model2, 'r-', label='Model 2 (Rigid Body)')      # 'r-' = red solid
plt.plot(x_theoretical, y_best_fit, 'g:', label='Linear Fit (Experimental)')  # 'g:' = green dotted

# Graph settings (labels, legends, titles)
# Using LaTeX ($) for nice labels
plt.xlabel(r'$\sqrt{h}$  (m$^{1/2}$)', fontsize=14)
plt.ylabel(r'$A$ (m)', fontsize=14)
#plt.title(r'Projectile Analysis: Range $A$ vs. $\sqrt{h}$', fontsize=16)
plt.legend(fontsize=12)
#plt.grid(False, linestyle='--', alpha=0.6)  # Add grid

sm()

# Show and save the graph
plt.savefig("result.png", dpi=300)
plt.show()


# --- 5. ANALYSIS REPORT (CONSOLE OUTPUT) ---

print("--- ANALYSIS REPORT ---")
print(f"Launch height (h0): {h0:.4f} m")
print("-" * 30)
print("THEORETICAL SLOPES (slope = A / sqrt(h))")
print(f"Model 1 (Point Mass): {slope_model1:.4f}")
print(f"Model 2 (Rigid Body): {slope_model2:.4f}")
print("-" * 30)
print("EXPERIMENTAL RESULTS")
print(f"Linear Fit Slope: {slope_exp:.4f}")
print(f"Linear Fit Intercept: {intercept_exp:.4f}")
print("-" * 30)

# Comparison
error_model1 = 100 * abs(slope_exp - slope_model1) / slope_model1
error_model2 = 100 * abs(slope_exp - slope_model2) / slope_model2

print("COMPARISON (Smaller error = better fit):")
print(f"Error in Model 1: {error_model1:.2f} %")
print(f"Error in Model 2: {error_model2:.2f} %")
print("-" * 30)

if error_model2 < error_model1:
    print("Conclusion: Model 2 (Rigid Body) is more accurate.")
else:
    print("Conclusion: Model 1 (Point Mass) is more accurate.")


#Quer que eu gere o arquivo `.py` já traduzido para download também?

