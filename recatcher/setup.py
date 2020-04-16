from setuptools import find_packages, setup

setup(
    name="CanaryCatcher",
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    instsall_requires=[
        'flask',
    ],
)