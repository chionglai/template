

from setuptools import setup, find_packages

VERSION = "0.0.1"

setup(
    name="template",
    version=VERSION,
    packages=find_packages() + ["template"],
    scripts=[],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },
    include_package_data=True,

    # metadata for upload to PyP
    author="Chiong Lai",
    author_email="chiong.lai@gmail.com",
    description="This is a template for Python setuptools",
    license="???",
    keywords="template",
    url="???",   # project home page, if any
    project_urls={
    },

    # could also include long_description, download_url, classifiers, etc.
    entry_points={
        "console_scripts": ["foo=template.foo:main"],
        "gui_scripts": ["foo_ui=gui.test_gui:main"],
    }
)
