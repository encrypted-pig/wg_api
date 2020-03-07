import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
requirements = ["requests"]
setuptools.setup(
    name="wg-api",
    version="0.0.1",
    author="Encoded_pig",
    author_email="takonok.3000@ya.ru",
    description="wargaming api package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/encrypted-pig/in_dev_wg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires='>=3.6',
)