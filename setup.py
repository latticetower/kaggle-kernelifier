import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kaggle-kernelifier",
    version="1.0.0",
    author="Tanya Malygina",
    #author_email="",
    description="tool to convert scripts to .ipynb notebook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/latticetower/kaggle-kernelifier",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Documentation",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
    ],  # available at https://pypi.org/classifiers/
    entry_points={  # points to where the cli is located
        "console_scripts": [
            # TODO: fill this
        ]
    }
)