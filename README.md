# LiDAR multi-angle elevation views
Generating multi-angle elevation views from LiDAR point cloud data
![Rotation_detailed_36](https://github.com/user-attachments/assets/9872d445-6d2c-4d13-a238-9ead969605bd)

Using the center of the bounding box for each tree, we defined a circle with a diameter equivalent to the longer side of the bounding box. This circle was used to extract all point clouds within the cylindrical space centered on the tree, reducing the influence of point clouds from other ground objects and adjacent trees. The heights of the extracted points were then normalized relative to the minimum ground point height. We generated an elevation view every 10 degrees by rotating around the normal through the center of the circle and the horizontal plane, resulting in 36 distinct views for each tree. This involved rotating the X-coordinates of the vegetation points and creating scatter plots for each rotated view, enhanced with a custom color map based on the adjusted heights. 
