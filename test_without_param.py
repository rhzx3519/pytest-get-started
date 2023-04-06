def test_vlan():
    device_vlans = ["100"]
    expected_vlans = ["100", "101", "102"]

    for v in expected_vlans:
        assert v in device_vlans