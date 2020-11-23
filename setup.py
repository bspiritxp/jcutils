import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='JC python utils',
    version='0.0.1b',
    author='Jochen.He',
    author_email='thjl@hotmail.com',
    description='some python util tools in one package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    python_requires='>=3.7',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
    ]
)
