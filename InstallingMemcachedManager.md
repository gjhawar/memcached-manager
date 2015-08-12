# Pre-Reqs. #

  * [PyQT4](http://wiki.python.org/moin/PyQt)
  * [Matplotlib](http://matplotlib.sourceforge.net/)
    * [Numpy](http://numpy.scipy.org/)
  * [PyYAML](http://pyyaml.org/)

# How to Install #

You must have installed all the Pre-Reqs before continuing on.

## PyPi Install ##

This is the simplest install route.

```
#Install
sudo easy_install MemcachedManager

#Launch/Run
MemcachedManager
```

## Source Download ##

```
#Install
tar -xzf Memcached\ Manager-0.1a1.5.tar.gz
cd Memcached\ Manager
python setup.py install

#Launch/Run
MemcachedManager
```

## Git for Dev ##

This is currently the only way to try out Memcached-Manager. It should be pretty simple for anyone with a bit of programming experience.

```
# Git Checkout
git clone git@github.com:nerdynick/MemcachedManager.git MemcachedManager

# Change Directory into the newly checkout code
cd MemcachedManager/src/MemachedManager

# Execute MemcachedManager
python Main.py
```