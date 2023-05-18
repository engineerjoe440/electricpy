################################################################################
"""Render images as needed using the various ElectricPy functions for docs."""
################################################################################

import os
import math, cmath
import numpy as np
import electricpy as ep
from electricpy import visu
from matplotlib import pyplot

FIGURE_DIRECTORY = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "static"
)

def canvas_capture(image_label):
    """Decorate a function to save the canvas as an image."""
    def decorate(render_method):
        def wrapper(*args, **kwargs):
            fig = pyplot.figure()
            render_method(*args, **kwargs)
            fig.savefig(f"{FIGURE_DIRECTORY}/{image_label}.png")
        return wrapper
    return decorate

@canvas_capture("PowerTriangle")
def render_power_triangle():
    """Render the Power Triangle Function."""
    visu.powertriangle(400, 200)

# @canvas_capture("PhasorPlot")
def render_phasor_plot():
    """Render the Phasor Plot Function."""
    # This phasorplot is ploted on seperate canvas
    phasors = ep.phasors.phasorlist([
        [67,0],
        [45,-120],
        [52,120]
    ])
    plt = visu.phasorplot(phasors=phasors, colors=["red", "green", "blue"])
    plt.savefig(f"{FIGURE_DIRECTORY}/PhasorPlot.png")

@canvas_capture("InductionMotorCircleExample")
def render_motor_circle():
    """Render the Induction Motor Circle and Draw."""
    open_circuit_test_data = {'V0': 400, 'I0': 9, 'W0': 1310}
    blocked_rotor_test_data = {'Vsc': 200, 'Isc': 50, 'Wsc': 7100}
    ratio = 1  # stator copper loss/ rotor copper loss
    output_power = 15000
    visu.InductionMotorCircle(
        no_load_data=open_circuit_test_data,
        blocked_rotor_data=blocked_rotor_test_data,
        output_power=output_power,
        torque_ration=ratio,
        frequency=50,
        poles=4
    ).plot()

@canvas_capture("ReceivingEndPowerCircleExample")
def render_receiving_end_power_circle():
    """Render the Receiving End Power Circle Plot."""
    visu.receiving_end_power_circle(
        A=cmath.rect(0.895, math.radians(1.4)),
        B=cmath.rect(182.5, math.radians(78.6)),
        Vr=cmath.rect(215, 0),
        Pr=50,
        power_factor=-0.9
    ).plot()

@canvas_capture("ReceivingPowerCircleExample")
def render_receiving_power_circle():
    """Render the Receiving End Power Circle Plot."""
    visu.PowerCircle(
        power_circle_type="receiving",
        A=cmath.rect(0.895, math.radians(1.4)),
        B=cmath.rect(182.5, math.radians(78.6)),
        Vr=cmath.rect(215, 0),
        Pr=50,
        power_factor=-0.9
    ).plot()

@canvas_capture("convbar-example")
def render_convbar_example():
    """Render the Plot Generated by the `electricpy.convbar` Function."""
    h = np.array([0, 1, 1, 1, 0])
    x = np.array([0, 1, 1, 1, 0])
    visu.convbar(h, x)

@canvas_capture("series-rlc-r5-l0.4")
def render_series_rlc_5_ohm():
    """Render the Series RLC Circuit's Visualization."""
    visu.SeriesRLC(
        resistance=5,
        inductance=0.4,
        capacitance=25.3e-6,
        frequency=50
    ).graph(lower_frequency_cut=0.1, upper_frequency_cut=100, samples=1000)

@canvas_capture("series-rlc-r10-l0.5")
def render_series_rlc_10_ohm():
    """Render the Series RLC Circuit's Visualization."""
    visu.SeriesRLC(
        resistance=10,
        inductance=0.5,
        capacitance=25.3e-6,
        frequency=50
    ).graph(lower_frequency_cut=0.1, upper_frequency_cut=100, samples=1000)

def main():
    """Run all of the Image Generators."""
    # Add function calls here as new rendering functions are added
    render_power_triangle()
    render_phasor_plot()
    render_motor_circle()
    render_receiving_end_power_circle()
    render_receiving_power_circle()
    render_convbar_example()
    render_series_rlc_5_ohm()
    render_series_rlc_10_ohm()


# Entrypoint
if __name__ == '__main__':
    main()


# END
