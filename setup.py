from cx_Freeze import setup, Executable

setup(
    name = "main",
    version = "0.1",
    description = "PM_tests",
    executables = [Executable("main.py")]
)