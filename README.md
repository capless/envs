# envs
Easy access of environment variables from Python with support for booleans, strings, lists, tuples, integers, floats, and dicts.

## Use Case

If you need environment variables for your settings but need an easy way of Python objects instead of just strings. For example, if you need a list of strings.


[![Build Status](https://travis-ci.org/capless/envs.svg?branch=master)](https://travis-ci.org/bjinwright/envs)

## Strings

**Environment Variable Example:** SECRET_KEY='adfadfadfafasf'
```python
>>>from envs import env

>>>env('SECRET_KEY','default secret key here')
'adfadfadfafasf'
```

## Lists
**Environment Variable Example:** SERVER_NAMES="['coastal','inland','western']"
```python
>>>from envs import env

>>>env('SERVER_NAMES',var_type='list')
['coastal','inland','western']
```

## Tuples
**Environment Variable Example:** SERVER_NAMES="('coastal','inland','western')"

```python
>>>from envs import env

>>>env('SERVER_NAMES',var_type='list')
('coastal','inland','western')
```

## Dicts
**Environment Variable Example:** DATABASE="{'USER':'name','PASSWORD':'password'}"

```python
>>>from envs import env

>>>env('DATABASE',var_type='dict')
{'USER':'name','PASSWORD':'password'}
```

## Integers

**Environment Variable Example:** NO_SERVERS=12
```python
>>>from envs import env

>>>env('NO_SERVERS',var_type='integer')
12
```

## Floats

**Environment Variable Example:** INDEX_WEIGHT=0.9
```python
>>>from envs import env

>>>env('INDEX_WEIGHT',var_type='float')
0.9
```

## Booleans
**Environment Variable Example:** USE_PROFILE=false
```python
>>>from envs import env

>>>env('USE_PROFILE',var_type='boolean')
False
```
### Author

**Twitter:**:[@brianjinwright](https://twitter.com/brianjinwright)
**Github:** [bjinwright](https://github.com/bjinwright)
