#! /usr/bin/python3
import pennylane as qml
from pennylane import numpy as np
import sys


def simple_circuits_30(angle):
    """The code you write for this challenge should be completely contained within this function
        between the # QHACK # comment markers.

    In this function:
        * Rotate a qubit around the y-axis by angle
        * Measure the expectation value of `PauliX`

    Args:
        angle (float): how much to rotate a state around the y-axis

    Returns:
        float: the expectation value of a PauliX measurement
    """
    x_expectation = 0.0

    # QHACK #

    # Step 1 : initialize a device
    num_wires = 1
    dev = qml.device("default.qubit", wires = num_wires)
    # Step 2 : Create a quantum circuit and qnode
    @qml.qnode(dev)
    def my_quantum_function(in_angle):
        qml.RY(in_angle, wires = 0)
        return qml.expval(qml.PauliX(0))
    # Step 3 : Run the qnode
    x_expectation = my_quantum_function(angle)
    # x_expectation = ?

    # QHACK #
    return x_expectation


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block

    # Load and process input
    angle_str = sys.stdin.read()
    angle = float(angle_str)

    ans = simple_circuits_30(angle)

    if isinstance(ans, np.tensor):
        ans = ans.item()

    if not isinstance(ans, float):
        raise TypeError("the simple_circuits_30 function needs to return a float")

    print(ans)
