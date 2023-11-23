from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='invisible_captcha_bypasser',
    version='0.0.1',
    author='nazavod',
    author_email='n4z4v0d@gmail.com',
    description='Bypassing invisible recaptcha v3',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/nazavod777/invisible_captcha_bypasser',
    packages=find_packages(),
    install_requires=['curl_cffi>=0.5.9'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='captcha recaptcha bypass recaptchav3 invisible_captcha',
    project_urls={
        'GitHub': 'https://github.com/nazavod777/invisible_captcha_bypasser'
    },
    python_requires='>=3.6'
)
