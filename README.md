# LiDAR multi-angle elevation views
Generating multi-angle side-view projections of individual trees from LiDAR point clouds

![Projction](https://github.com/user-attachments/assets/db1d3559-755a-47be-aa32-aa4207a22c28)


Using the center of the bounding box for each tree, we defined a circle with a diameter equivalent to the longer side of the bounding box. A cylindrical space is then established using this circle as the base, capturing all points within its boundary. Next, the point cloud is projected onto a plane that intersects the center of the bounding box and is perpendicular to the horizontal plane (XY plane). The projection plane rotates around the vertical (Z) axis passing through the center of the circle, generating side views at regular angular intervals. 
