import math
import numpy as np
import torch
import matplotlib.pyplot as plt
import functools

class Camera:
    def __init__(self, focal_length, center, basis):
        camera_center = center.detach().clone()
        transposed_basis = torch.transpose(basis, 0, 1)
        camera_center[:3] = camera_center[
                            :3] * -1  # We don't want to multiply the homogenous coordinate component; it needs to remain 1
        camera_origin_translation = torch.eye(4, 4)
        camera_origin_translation[:, 3] = camera_center
        extrinsic_camera_parameters = torch.matmul(torch.inverse(transposed_basis), camera_origin_translation)
        intrinsic_camera_parameters = torch.tensor([[focal_length, 0., 0., 0.],
                                                    [0., focal_length, 0., 0.],
                                                    [0., 0., 1., 0.]])
        self.transform = torch.matmul(intrinsic_camera_parameters, extrinsic_camera_parameters)

    def to_2D(self, point):
        # return torch.transpose(point, 0, 1)
        rendered_point = torch.matmul(self.transform, torch.transpose(point, 0, 1))
        point_z = rendered_point[2, 0]
        return rendered_point / point_z


def camera_basis_from(camera_depth_z_vector):
    depth_vector = camera_depth_z_vector[:3]  # We just want the inhomogenous parts of the coordinates

    # This calculates the projection of the world z-axis onto the surface defined by the camera direction,
    # since we want to derive the coordinate system of the camera to be orthogonal without having
    # to calculate it manually.
    cartesian_z_vector = torch.tensor([0., 0., 1.])
    cartesian_z_projection_lambda = torch.dot(depth_vector, cartesian_z_vector) / torch.dot(
        depth_vector, depth_vector)
    camera_up_vector = cartesian_z_vector - cartesian_z_projection_lambda * depth_vector

    # The camera coordinate system now has the direction of camera and the up direction of the camera.
    # We need to find the third vector which needs to be orthogonal to both the previous vectors.
    # Taking the cross product of these vectors gives us this third component
    camera_x_vector = torch.linalg.cross(depth_vector, camera_up_vector)
    inhomogeneous_basis = torch.stack([camera_x_vector, camera_up_vector, depth_vector, torch.tensor([0., 0., 0.])])
    homogeneous_basis = torch.hstack((inhomogeneous_basis, torch.tensor([[0.], [0.], [0.], [1.]])))
    homogeneous_basis[0] = unit_vector(homogeneous_basis[0])
    homogeneous_basis[1] = unit_vector(homogeneous_basis[1])
    homogeneous_basis[2] = unit_vector(homogeneous_basis[2])
    return homogeneous_basis


def basis_from_depth(look_at, camera_center):
    depth_vector = torch.sub(look_at, camera_center)
    depth_vector[3] = 1.
    return camera_basis_from(depth_vector)


def unit_vector(camera_basis_vector):
    return camera_basis_vector / math.sqrt(
        pow(camera_basis_vector[0], 2) +
        pow(camera_basis_vector[1], 2) +
        pow(camera_basis_vector[2], 2))


def plot(style="bo"):
    return lambda p: plt.plot(p[0][0], p[1][0], style)


def line(marker="o"):
    return lambda p1, p2: plt.plot([p1[0][0], p2[0][0]], [p1[1][0], p2[1][0]], marker="o")


Y_0_0 = 0.5 * math.sqrt(1. / math.pi)
Y_m1_1 = lambda theta, phi: 0.5 * math.sqrt(3. / math.pi) * math.sin(theta) * math.sin(phi)
Y_0_1 = lambda theta, phi: 0.5 * math.sqrt(3. / math.pi) * math.cos(theta)
Y_1_1 = lambda theta, phi: 0.5 * math.sqrt(3. / math.pi) * math.sin(theta) * math.cos(phi)
Y_m2_2 = lambda theta, phi: 0.5 * math.sqrt(15. / math.pi) * math.sin(theta) * math.cos(phi) * math.sin(
    theta) * math.sin(phi)
Y_m1_2 = lambda theta, phi: 0.5 * math.sqrt(15. / math.pi) * math.sin(theta) * math.sin(phi) * math.cos(theta)
Y_0_2 = lambda theta, phi: 0.25 * math.sqrt(5. / math.pi) * (3 * math.cos(theta) * math.cos(theta) - 1)
Y_1_2 = lambda theta, phi: 0.5 * math.sqrt(15. / math.pi) * math.sin(theta) * math.cos(phi) * math.cos(theta)
Y_2_2 = lambda theta, phi: 0.25 * math.sqrt(15. / math.pi) * (
        pow(math.sin(theta) * math.cos(phi), 2) - pow(math.sin(theta) * math.sin(phi), 2))


def harmonic(C_0_0, C_m1_1, C_0_1, C_1_1, C_m2_2, C_m1_2, C_0_2, C_1_2, C_2_2):
    return lambda theta, phi: C_0_0 * Y_0_0 + C_m1_1 * Y_m1_1(theta, phi) + C_0_1 * Y_0_1(theta, phi) + C_1_1 * Y_1_1(
        theta, phi) + C_m2_2 * Y_m2_2(theta, phi) + C_m1_2 * Y_m1_2(theta, phi) + C_0_2 * Y_0_2(theta,
                                                                                                phi) + C_1_2 * Y_1_2(
        theta, phi) + C_2_2 * Y_2_2(theta, phi)


def channel_opacity(channel_density_distance_tuples):
    number_of_samples = len(channel_density_distance_tuples)
    print(number_of_samples)
    transmittances = list(map(lambda i: functools.reduce(
        lambda acc, j: acc + math.exp(- channel_density_distance_tuples[j, 0] * channel_density_distance_tuples[j, 2]),
        range(0, i), 0.), range(1, number_of_samples + 1)))
    density = 0.
    print(transmittances)
    for index, transmittance in enumerate(transmittances):
        if index == len(transmittances) - 1:
            break
        density += (transmittance - transmittances[index + 1]) * channel_density_distance_tuples[index, 1]
    return density


tuples = torch.tensor([[1, 1, 1], [1, 1, 1]])

print(channel_opacity(tuples))

voxel_grid = torch.ones([20, 20, 20, 4])
for i in range(20):
    for j in range(20):
        for k in range(20):
            voxel_grid[i,j,k] = torch.tensor([0.1, 0.5, 0.6, 0.7])

test_harmonic = harmonic(1, 2, 3, 4, 5, 6, 7, 8, 1)


# fig1 = plt.figure()
#
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             d = camera.to_2D(torch.tensor([[i, j, k, 1.]]))
#             print(d)
#             plt.plot(d[0][0], d[1][0], marker="o")
#

look_at = torch.tensor([0., 0., 0., 1])
camera_center = torch.tensor([30., -30., 30., 1.])
focal_length = 1

camera_basis = basis_from_depth(look_at, camera_center)
camera = Camera(focal_length, camera_center, camera_basis)

ray_origin = camera_center
camera_basis_x = camera_basis[0][:3]
camera_basis_y = camera_basis[1][:3]

camera_center_inhomogenous = camera_center[:3]

plt.figure()
plt.axis("equal")

for i in np.linspace(0, 20, 30):
    for j in np.linspace(-10, 30, 30):
        ray_screen_intersection = camera_basis_x * i + camera_basis_y * j
        unit_ray = unit_vector(ray_screen_intersection - camera_center_inhomogenous)
        density = 0.
        for k in np.linspace(0, 100):
            ray_endpoint = camera_center_inhomogenous + unit_ray * k
            ray_x, ray_y, ray_z = ray_endpoint
            if (ray_x < 0 or ray_x > 10 or
                    ray_y < 0 or ray_y > 10 or
                    ray_z < 0 or ray_z > 10):
                continue
            # We are in the box
            density += 0.1
        plt.plot(i, j, marker="o", color=str(1. - density))

plt.show()