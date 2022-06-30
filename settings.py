from pathlib import Path
import subprocess


PROJECT_ROOT = Path(__file__).parent

BB_DIR = PROJECT_ROOT / "bb"

if __name__ == "__main__":
    # command = f"dir {str(BB_DIR.resolve())}"
    # sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    command = ["dir", BB_DIR.resolve()]
    sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    rtrn = sp.wait()
    out, err = sp.communicate()
    print(out)

    print(PROJECT_ROOT.resolve())
    print(BB_DIR.resolve())
    print(str(BB_DIR.resolve()))
    print(type(BB_DIR.resolve()))
