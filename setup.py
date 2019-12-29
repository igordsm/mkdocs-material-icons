import setuptools

with open('README.md') as f:
    long_descr = f.read()

setuptools.setup(
    name='mkdocs-material-icons',
    version='0.1.4',
    description='Python Markdown filter that outputs HTML for material icons.'
                'Designed for use with mkdocs and Material Theme.',
    long_description=long_descr,
    long_description_content_type="text/markdown",
    author='Igor Montagner',
    author_email='igordsm@gmail.com',
    packages=setuptools.find_packages()
)