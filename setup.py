from setuptools import setup

setup(
    name="bjontegaard",
    version="1.0.0",
    license="BSD-3-Clause",
    package_dir={"bjontegaard": "bd"},
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
    ],
    py_modules=["bjontegaard", ],
    packages=["bjontegaard", ],
)
