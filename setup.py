from distutils.core import setup
from rfeed.rfeed import __version__

setup(
    name="rfeed",
    packages=['rfeed'],
    version=".".join(map(str, __version__)),
    description="Python RSS 2.0 Generator",
    author="Santiago L. Valdarrama",
    author_email="svpino@gmail.com",
    maintainer="Egor Smolyakov",
    maintainer_email="egorsmkv@gmail.com",
    url="https://github.com/egorsmkv/rfeed",
    keywords=['feed', 'rss'],
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: XML'
    ]
)
