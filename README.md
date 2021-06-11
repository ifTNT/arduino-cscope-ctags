# arduino-cscope-ctags

Generating tags of arduino sketch in one command for code tracing.

## Introduction

Arduino is a convenient environment for developing embedding application. Sometimes tracing the code of Arduino core can help us to realize how the lower-level function was implemented and futher assist debugging. However, it's a tough work that tracing code with vanilla Arduino IDE, especially with third party core variants like ESP32.  
Thus, the purpose of this tool is to simplify the work to generate the symbol database of cscope and ctags from Arduino sketch. Once the database is generated, you can begin tracing the code use cscope/ctags with other text editor like vim, emacs, vscode or sublime text.

## How to use

clear the cache /tmp/arduino-core-cache

## How to install

1. Install python3.6, arduino-cli, cscope and ctags via the package manage of your distrubution.
2. Download the source code of this project.

```bash
git clone https://github.io/ifTNT/arduino-cscope-ctags/arduino-cscope-ctags.git
cd arduino-cscope-ctags/
```

3. Use the following command to install other dependencies.

```bash
sudo pip install -r requirements.txt
```

4. Copy the executable to the system directory.

```bash
sudo cp arduino-cscope-ctags /usr/local/bin/
```

5. Enjoy hacking!

### Dependencies

python 3.6
arduino-cli 0.18.3
Universal Ctags 5.9.0
cscope 15.9

## How to contribute
