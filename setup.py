from setuptools import setup, find_packages

setup(
    name='django-bricks',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True, # Important pour tes templates/static dans ces apps
    install_requires=[
        'django>=4.0',
        # Ajoutez ici les autres dépendances de vos bricks si nécessaire
    ],
)