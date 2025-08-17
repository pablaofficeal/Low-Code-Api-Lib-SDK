from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my_sdk",
    version="0.1.0",
    author="Pavlo",
    author_email="pavlo@example.com",
    description="SDK для работы с API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pavlo/my_sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.0",
    ],
)