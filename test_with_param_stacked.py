import pytest

device_vlans = {
    "rtr001": ["100", "101"],
    "rtr002": ["101", "102"],
    "rtr003": ["100", "102"],
}

@pytest.mark.parametrize("device", ["rtr001", "rtr002", "rtr003"])
@pytest.mark.parametrize("expected_vlan", ["100", "101", "102"])
def test_vlan(expected_vlan, device):
    assert expected_vlan in device_vlans.get(device, [])