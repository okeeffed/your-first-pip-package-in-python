import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="demo_pip_math",
    version="0.1.0",
    author="Dennis O'Keeffe",
    author_email="hello@dennisokeeffe.com",
    description="Demo your first Pip package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/okeeffed/your-first-pip-package-in-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='pip-demo math',
    project_urls={
        'Homepage': 'https://github.com/okeeffed/your-first-pip-package-in-python',
    },

)
