import numpy as np
from scipy.optimize import linear_sum_assignment

def calculate_cost_matrix(drivers, passengers, traffic_grid, rates):
    n = len(drivers)
    m = len(passengers)
    cost_matrix = np.zeros((n, m))
    
    for i in range(n):
        for j in range(m):
            # Calculate Euclidean distance between driver i and passenger j
            dx, dy = drivers[i][0] - passengers[j][0], drivers[i][1] - passengers[j][1]
            distance = np.sqrt(dx**2 + dy**2)
            
            # Apply traffic modifier and driver rate
            cost_matrix[i][j] = distance * traffic_grid[i][j] * rates[i]
    
    return cost_matrix

def find_optimal_matches(drivers, passengers, traffic_grid, rates):
    # Calculate the cost matrix
    cost_matrix = calculate_cost_matrix(drivers, passengers, traffic_grid, rates)
    
    # Use the Hungarian algorithm to find the optimal assignment
    driver_indices, passenger_indices = linear_sum_assignment(cost_matrix)
    
    # Prepare output with each pair and the corresponding cost
    matches = [(d_idx, p_idx, round(cost_matrix[d_idx, p_idx], 2)) 
               for d_idx, p_idx in zip(driver_indices, passenger_indices)]
    return matches

# Input
drivers = [(0, 0), (2, 2), (4, 4)]
passengers = [(1, 1), (3, 3), (5, 5)]
traffic_grid = [
    [1, 2, 3],
    [2, 1, 4],
    [3, 4, 1]
]
rates = [1.5, 2.0, 1.8]

# Find optimal matches
optimal_matches = find_optimal_matches(drivers, passengers, traffic_grid, rates)
print(optimal_matches)
