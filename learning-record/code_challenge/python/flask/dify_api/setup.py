from setuptools import setup, find_packages

setup(
    name='dify_api',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'dify_api = dify_api.app:app'  
        ]
    }
)