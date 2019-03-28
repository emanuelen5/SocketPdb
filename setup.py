from setuptools import setup, find_packages

# Get the long description from the README file
def readme():
    with open('README.md') as f:
        return f.read()

setup(
        name="socket_pdb",
        version="1.0.0",
        description="A remote debugger extension of pdb",
        long_description=readme(),
        url="https://github.com/emanuelen5/SocketPdb",
        license="UNLICENSED",
        author="Erasmus Cedernaes",
        author_email="erasmus.cedernaes@gmail.com",
        python_requires = ">=2.6",
        py_modules=["socket_pdb"],
        # Packages that need to be installed via pip
        install_requires = []
)
