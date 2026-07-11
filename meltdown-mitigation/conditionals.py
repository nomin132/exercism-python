"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and\
          temperature*neutrons_emitted < 500000:
       return True
    else: 
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    """The percentage value can be calculated as `(generated_power/theoretical_max_power)*100`
    where `generated_power` = `voltage` * `current`.
    Note that the percentage value is usually not an integer number, so make sure to consider the
    proper use of the `<` and `<=` comparisons."""

    generated_power= voltage*current
    efficency = generated_power / theoretical_max_power*100
    if efficency>=80:
        colour = "green"
    elif efficency >= 60: 
        colour = "orange"
    elif efficency >= 30:
        colour = "red"
    else: 
        colour = "black"
    return colour 


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    product=temperature*neutrons_produced_per_second 
    low_limit= threshold*0.9
    norm_limit=threshold*1.1
    if product<low_limit: 
        return "LOW"
    elif product<norm_limit: 
        return "NORMAL"
    else: 
        return "DANGER"
