from setuptools import setup

setup(
    name='zohoapi',
    packages=['zohoapi'],
    version='0.1',
    description='Wrapper for the Zoho CRM API',
    author='Ben Jarrett',
    author_email='',
    url='https://bitbucket.org/cannibalsock/zohoapi',
    keywords='zoho crm',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=['peppercorn'],

)