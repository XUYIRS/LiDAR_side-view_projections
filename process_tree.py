import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize, LinearSegmentedColormap

custom_norm = Normalize(vmin=0, vmax=24) # z_min = 0 after normalizing point cloud
colors = [(0, '#015256'), (0.25, '#2ea6a5'), (0.5, '#f0b23b'), (0.75, '#f28727'), (1, '#da2514')]
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)


# Define a function to process each tree
def process_tree(tree, veg_tree, ground_tree, veg_xyz_all, 
                 ground_xyz_all, rotation_angle = 30):
    """
    Process individual trees to generate rotated images.

    Parameters:
    - tree: GeoDataFrame row containing the tree geometry and attributes.
    - veg_tree: KDTree constructed from vegetation points.
    - ground_tree: KDTree constructed from ground points.
    - veg_xyz_all: Array of vegetation points' coordinates.
    - ground_xyz_all: Array of ground points' coordinates.
    - rotation_angle: Rotation angle of views.

    Returns:
    - fig_list: List of figures generated for the tree.
    """
    fig_list = []
    center = [tree.geometry.centroid.x, tree.geometry.centroid.y]
    min_x, min_y, max_x, max_y = np.array(tree.geometry.bounds)
    r = max((max_x - min_x), (max_y - min_y)) / 2  # Radius of the cylinder

    # Query KDTree to get indices of points within the radius
    veg_index = veg_tree.query_ball_point(center, r=r, p=2.0, eps=0.0, workers=-1)
    if len(veg_index) == 0:
        return fig_list
    ground_index = ground_tree.query_ball_point(center, r=r, p=2.0, eps=0.0, workers=-1)

    # Filter points based on the indices
    veg_xyz = veg_xyz_all[veg_index]
    ground_xyz = ground_xyz_all[ground_index]

    # Adjust heights relative to the minimum ground point height
    z_min = np.min(ground_xyz['Z']) if len(ground_xyz) > 0 else np.min(veg_xyz['Z'])
    veg_xyz['Z'] -= z_min

    veg_xyz = veg_xyz[veg_xyz['Z'] >= 0]
    Z_filter = veg_xyz['Z']
    if len(Z_filter) == 0 or np.max(Z_filter) <= 3:  # Skip objects shorter than 3m
        return fig_list

    # Generate rotated images at 30-degree intervals
    for a in range(0, 360, rotation_angle):
        angle = np.radians(a)
        X_rotated = veg_xyz['X'] * np.cos(angle) - veg_xyz['Y'] * np.sin(angle)

        fig, ax = plt.subplots(dpi=100)
        ax.scatter(X_rotated, Z_filter, s=0.2, c=custom_cmap(custom_norm(Z_filter)))
        ax.set_ylim(0, np.max(Z_filter))
        ax.axis('off')
        ax.set_aspect('equal', adjustable='box')
        fig_list.append([center, fig, a])
    plt.close('all')
    return fig_list


def create_if_not(folder_path):
    *prev_path, last_folder = os.path.split(folder_path[:-1])
    prev_path = os.path.join(*prev_path)

    if os.path.exists(prev_path):
        if not os.path.exists(folder_path):
            try:
                os.mkdir(folder_path)
                print(f"Creating '{folder_path}': Successfully")
            except OSError as error:
                print(f"Creating '{folder_path}': {error}")
    else:
        print(f"Error: Path '{prev_path}' does not exist.")