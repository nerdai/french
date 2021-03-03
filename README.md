# The galaxy is full of stars


##Setup
1. Make sure Homebrew is installed
    1. make sure homebrew is installed.
        1. `which brew` ...did it work? If not run this command somewhere
        ```
        mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
        ```
    2. `brew --version` should read `2.6.0` as of `Dec 1, 2020` 
    3. if you are below `2.6.0` run `brew update`
2. Make sure env tools are installed
    1. for each of the next 3 components, `pyenv` `pyenv-virtualenv` `pipenv`    
        1. If they exist (ie. they are in the output of `brew list`)
            1. if they are outdated (ie, they are in the in the output of `brew outdated`) then run `brew upgrade <component>`
        2. If they don't exist, run `brew install <component>`
                
3. Initialize your dev env
    1. `pipenv shell`
    2. `pipenv sync`
 
