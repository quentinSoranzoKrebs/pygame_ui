from setuptools import setup, find_packages

setup(
    name='pygame_ui',
    version='0.1.0',
    packages=find_packages(),
    license='MIT',
    description='Simple library to create pygame user interface.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Votre nom',
    author_email='soranzokrebsquentin@gmail.com',
    url='lien_vers_votre_repo',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        # Liste des dépendances de votre bibliothèque
        'pygame',
        'matplotlib',
    ],
)
