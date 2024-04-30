from pathlib import Path

from setuptools import setup, find_packages

import puppeteer_pdf


setup(
    name='django-puppeteer-pdf',
    packages=find_packages(),
    include_package_data=True,
    version=puppeteer_pdf.__version__,
    description='Converts HTML to PDF using puppeteer.',
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    license='MIT License',
    author=puppeteer_pdf.__author__,
    author_email=puppeteer_pdf.__email__,
    url='https://github.com/incuna/django-puppeteer-pdf',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Framework :: Django',
    ],
    keywords='django puppeteer pdf',
)
