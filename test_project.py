from mylib.calc import add, sub, mul, div, power
from calCLI import cli
from click.testing import CliRunner
import subprocess

# Write a test for calCLI.py 
def test_cli():
    runner = CliRunner()
    
    result = runner.invoke(cli, ["add", "1", "2"])
    assert result.exit_code == 0
    assert result.output == "3.0\n"
    
    result = runner.invoke(cli, ["sub", "1", "2"])
    assert result.exit_code == 0
    assert result.output == "-1.0\n"
    
    result = runner.invoke(cli, ["mul", "1", "2"])
    assert result.exit_code == 0
    assert result.output == "2.0\n"
    
    result = runner.invoke(cli, ["div", "1", "2"])
    assert result.exit_code == 0
    assert result.output == "0.5\n"
    
    result = runner.invoke(cli, ["power", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "8.0\n"

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(1, 2) == -1

def test_mul():
    assert mul(1, 2) == 2

def test_div():
    assert div(1, 2) == 0.5

def test_power():
    assert power(2, 3) == 8

def test_main():
    result = subprocess.run(["python3", "calCLI.py", "add", "1", "2"], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout == "3.0\n"