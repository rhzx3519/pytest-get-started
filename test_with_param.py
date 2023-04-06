import pytest

@pytest.mark.parametrize("expected_vlan", ["100", "101", "102"])
def test_vlan(expected_vlan):
    device_vlans = ["100"]
    assert expected_vlan in device_vlans