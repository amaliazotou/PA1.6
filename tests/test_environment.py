import math

from simulations.environment import Environment


def test_temperature_follows_sinusoid_without_door_event():
    env = Environment(base=5.0, amplitude=2.0, period_s=7200.0)

    assert env.T_out(0.0) == 5.0
    assert env.T_out(1800.0) == 5.0 + 2.0 * math.sin(math.pi / 2.0)


def test_door_event_applies_drop_during_window():
    env = Environment(base=5.0, amplitude=2.0, period_s=7200.0,
                      door_drop_C=5.0, door_start_s=1200.0, door_duration_s=120.0)

    assert env.T_out(1200.0) == 5.0 + 2.0 * math.sin(2.0 * math.pi * 1200.0 / 7200.0) - 5.0
    assert env.T_out(1259.0) == 5.0 + 2.0 * math.sin(2.0 * math.pi * 1259.0 / 7200.0) - 5.0
    assert env.T_out(1320.0) == 5.0 + 2.0 * math.sin(2.0 * math.pi * 1320.0 / 7200.0)


def test_door_event_is_not_applied_before_or_after_window():
    env = Environment(base=5.0, amplitude=2.0, period_s=7200.0,
                      door_drop_C=5.0, door_start_s=1200.0, door_duration_s=120.0)

    assert env.T_out(1199.0) == 5.0 + 2.0 * math.sin(2.0 * math.pi * 1199.0 / 7200.0)
    assert env.T_out(1320.0) == 5.0 + 2.0 * math.sin(2.0 * math.pi * 1320.0 / 7200.0)
