from setuptools import setup

setup(
    name='analysis_cli',
    version='0.0.1',
    install_requires=[
    ],
    include_package_data=True,
    entry_points='''
    [console_scripts]
    analysis_dir=analysis_cli.cli:analysis_dir
    '''
)
