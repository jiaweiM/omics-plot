import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="omics-plot",
    version="0.0.1",
    author="Jiawei Mao",
    author_email="jiaweiM_philo@hotmail.com",
    description="Omics plot package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiaweiM/omics-plot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics :: Viewers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires='>=3.8'
)
