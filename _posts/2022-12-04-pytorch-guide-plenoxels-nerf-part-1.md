---
title: "Plenoxels and Neural Radiance Fields using PyTorch: Part 1"
author: avishek
usemathjax: true
tags: ["Machine Learning", "PyTorch", "Programming", "Neural Radiance Fields", "Machine Vision"]
draft: false
---

This is part of a series of posts breaking down the paper [Plenoxels: Radiance Fields without Neural Networks](https://arxiv.org/abs/2112.05131), and providing (hopefully) well-annotated source code to aid in understanding.

**The final code has been moved to its own repository at [plenoxels-pytorch](https://github.com/asengupta/plenoxels-pytorch).**

- [Part 1 (this one)]({% post_url 2022-12-04-pytorch-guide-plenoxels-nerf-part-1 %})
- [Part 2]({% post_url 2022-12-05-pytorch-guide-plenoxels-nerf-part-2 %})
- [Part 3]({% post_url 2022-12-07-pytorch-guide-plenoxels-nerf-part-3 %})
- [Part 4]({% post_url 2022-12-18-pytorch-guide-plenoxels-nerf-part-4 %})
- [Part 5]({% post_url 2022-12-19-pytorch-guide-plenoxels-nerf-part-5 %})
- [Part 6]({% post_url 2022-12-27-pytorch-guide-plenoxels-nerf-part-6 %})

The relevant paper is [Plenoxels: Radiance Fields without Neural Networks](https://arxiv.org/abs/2112.05131). We will also use [this explanation](https://deeprender.ai/blog/plenoxels-radiance-fields-without-neural-networks) to understand some parts of this paper a little better.

Before we get into the implementations of the paper proper, we will need a game plan. This game plan will include some theoretical background that we will have to go through to implement parts of this paper. The theoretical background will include:

- Camera Model
- Volumetric Rendering Model
- Spherical Harmonics
- Regularisation

In this specific post, however, we will start building out a simple **volumetric renderer**. On the way, we will also discuss the pinhole camera model, on which most of our rendering will be based on.

### The World Camera Model and some Linear Algebra

The **pinhole camera model** has the following characteristics.

- The model exists in the world, and is expressed in the **world coordinate system**. This is usually our default three-dimensional basis.
- The camera exists somewhere in the world, and has its own coordinate system, the **camera coordinate system**. This is characterised by the **location** of the camera, the **focal length** of the camera, and the three-dimensional basis for the camera.
- The screen of the camera (which is basically where the image is formed) has its own two-dimensional coordinate system.

![Camera World Mode](/assets/images/camera-world-model.png)

The challenge is this: we have a point in 3D space expressed in the world coordinate system, let's call it $$X_W$$; we want to know what this point will translate to on the 2D coordinate system of the camera screen/film. At a very high level, given all the information about the camera and the world, we want to know about the camera transform matrix $$P$$.

$$
\begin{equation}
X_V=TX_W
\label{eq:1}
\end{equation}
$$

In the above diagram $$X_W = (x_w, y_w, z_w)$$.
We need to do the following steps:

- Express $$X_W$$ in the coordinate system of the camera as $$X_C$$. These are the **extrinsic parameters** of the camera.
- Express $$X_C$$ in the coordinate system of the camera screen, taking into account focal length. These are the **intrinsic parameters** of the camera.

The camera is characterised first by the camera center $$C$$. The first step is translating the entire world so that the origin is now at the camera. This is simply done by calculating $$X_W-C$$.

The camera is also characterised by its basis, which is essentially three 3D vectors. Now that the camera is at the center, we need to rotate the world so that everything in it is expressed using the camera's coordinate system. How do we achieve this change of basis?

We have discussed change of basis before in a few articles. Specifically see [The Gram-Schmidt Orthogonalisation]({% post_url 2021-05-27-gram-scmidt-orthogonalisation %}) and [Geometry of the Multivariate Gaussian Distribution]({% post_url 2021-08-30-geometry-of-multivariate-gaussian %}).

Specifically, we have an arbitrary basis $$B$$ in $$n$$-dimensional space, and let there be a vector $$v$$ expressed in the world coordinate system. We'd like to be able to represent $$v$$ using $$B$$'s coordinate system. Let's assume that $$v_B$$ is the vector $$v$$ expressed in $$B$$'s coordinate system.

Then, we can write:

$$
B v_B=v \\
\Rightarrow B^{-1}B v_B = B^{-1} v \\
\Rightarrow v_B = B^{-1} v
$$

Thus, multiplying $$B^{-1}$$ with our original world space vector $$v$$ gives us the same vector but expressed in the coordinate space of basis $$B$$.

Thus, the rotation that we need to do is:

$$
\begin{equation}
X_C=B^{-1} (X_W - C)
\label{eq:2}
\end{equation}
$$

In the diagram above, $$X_C=(x_C, y_C, x_C)$$.
A note on convention: the Z-axis of the camera always points in the direction the camera is pointing in: the X- and Y-axes are reserved for mapping the image onto the camera screen.

### The Pinhole Camera Model

Now we look at the intrinsic parameters which form the basis for the pinhole camera model, specifically the focal length and the mapping to the screen (which is where we will finally see the image). The pinhole camera model is represented by the following diagram.

![Pinhole Camera Mode](/assets/images/pinhole-camera-model.png)

By similar triangles, we have:

$$
\frac{y_V}{y}=\frac{f}{z} \\
y_V = \frac{f}{z} y
$$

Similarly, we have: $$\displaystyle x_V = \frac{f}{z} x$$. Finally, we have the translation from the camera viewfinder to the screen where we will see the image. The mapping to the screen is a simple $$x-y$$ translation represented by $$p_x$$ and $$p_y$$.

![Screen Camera Translation](/assets/images/screen-camera-translation.png)

The transform matrix in homogeneous coordinates is thus:

$$
\begin{equation}
P=
\begin{bmatrix}
f && 0 && p_x && 0 \\
0 && f && p_y && 0 \\
0 && 0 && 1 && 0
\end{bmatrix}
\label{eq:3}
\end{equation}
$$

Note that the above matrix is $$3 \times 4$$: passing a 3D coordinate in homogeneous form ($$4 \times 1$$) will yield a $$3 \times 1$$ vector.

The result of the transform $$PX_C$$ gives us:

$$
PX_C =
\begin{bmatrix}
f && 0 && p_x && 0 \\
0 && f && p_y && 0 \\
0 && 0 && 1 && 0
\end{bmatrix}

\begin{bmatrix}
x_C \\
y_C \\
z_C \\
1
\end{bmatrix}
=

\begin{bmatrix}
fx_C + z_C p_x \\
fy_C + z_C p_y \\
z_C \\
\end{bmatrix}
$$

Since $$z$$ is not constant, whatever result we get will be divided throughout by $$z$$, to give us the 2D view screen coordinates in homogeneous form.

$$
PX_C=\begin{bmatrix}
\displaystyle\frac{f}{z}x_C + p_x \\
\displaystyle\frac{f}{z}y_C + p_y \\
1 \\
\end{bmatrix}
$$

Pulling in $$\eqref{eq:2}$$, $$\eqref{eq:3}$$, and substituting in $$\eqref{eq:3}$$, we get:

$$
X_V = PB^{-1} (X_W - C)
$$

**Technical Note:** In the actual implementation, the camera center translation is implemented using homogeneous coordinates, so that instead of subtracting the camera center ($$C=(C_x, C_y, C_z)$$), we perform a matrix multiplication, like so:

$$
X_V = PB^{-1}.C'.X_W
$$

where $$C'=\begin{bmatrix}
0 && 0 && 0 && -C_x \\
0 && 1 && 0 && -C_y \\
0 && 0 && 0 && -C_z \\
0 && 0 && 0 && 1
\end{bmatrix}
$$.

### Implementation

The following code plays around with the pinhole camera model and sets up a very basic (maybe even contrived) volumetric rendering model. The details of the toy volumetric raycasting logic is explained after the listing. The code is annotated with comments so you should be able to follow along.

```python
{% include_absolute '/code/pytorch-learn/plenoxels/camera2.py' %}
```

We have not discussed the optical model for volumetric rendering, so for the moment, we will describe a very cheap way of getting a sense of what a volumetric rendering might look like.
- Determine a bundle of rays originating from the camera center. These rays will be intersecting the camera viewport.
- For each ray, sample a number of points along this ray upto some reasonable limit. The initial "density" of this ray is 0.
- For each such point, determine if it lies in an occupied voxel. If it does, increment the density of this ray by a tiny amount.
- At the end of the sampling of this ray, the accumulated density will be the greyscale intensity of the pixel in the camera viewport.

We have used a simple $$10 \times 10 \times 10$$ cube for this example. There is currently no data structure holding the cube information: we simply assume the cube extends from $$(0,0,0)$$ upto $$(10,0,0)$$, $$(0,10,0)$$, and $$(0,0,10)$$, and implement the voxel check accordingly.

![Basic Volumetric Raycasting](/assets/images/basic-volumetric-raycasting.png)

### Outputs

This is the voxel image of the cube.
![Voxel Cube](/assets/images/voxel-cube.png)

This is the volumetric render of the cube. As expected, the direction of the diagonal (as seen from the camera) is the densest, as the rays have to pass through the most number of voxels.

![Very Basic Volumetric Rendering of Cube](/assets/images/basic-volumetric-rendering-cube.png)

This concludes the first part of building the very basic infrastructure to support building the rest of the paper.

### References

- [Camera Matrix - Kris Kitani](https://www.cs.cmu.edu/~16385/s17/Slides/11.1_Camera_matrix.pdf)
- [Plenoxels: Radiance Fields without Neural Networks](https://arxiv.org/abs/2112.05131)
- [Plenoxels Explained](https://deeprender.ai/blog/plenoxels-radiance-fields-without-neural-networks)
- [Optical Model for Volumetric Rendering](https://www.youtube.com/watch?v=hiaHlTLN9TE)
