import phase_control

def test_get_pid_path(tmp_path):
    phase_control.PID_DIR = str(tmp_path)
    expected = tmp_path / "daemon.pid"
    assert phase_control.get_pid_path("daemon") == str(expected)
