# arduino-cscope-ctags

Generating database of cscope/ctags from Arduino sketch in one command for code tracing.

## Introduction

Arduino is a convenient environment for developing embedding application. On the other hand, tracing the code of Arduino core can help us to realize how the lower-level function was implemented and futher assist us in debugging. However, it's a tough work that tracing code with vanilla Arduino IDE, especially with third party core variants like ESP32.  
Thus, the purpose of this tool is to simplify the work to generate the symbol database of cscope and ctags from Arduino sketch. Once the database is generated, you can begin tracing the code use cscope/ctags with other text editor like vim, emacs, vscode or sublime text.

## How to use

### The context of example

- Board: NodeMCU-32S
- Third Party Core: [arduino-esp32](https://github.com/espressif/arduino-esp32/tree/1.0.6)
- Sketch: [ESP32/FreeRTOS](https://github.com/espressif/arduino-esp32/blob/1.0.6/libraries/ESP32/examples/FreeRTOS/FreeRTOS.ino)
- Text Editor: vim

### Usage guide by example

1. Query the Fully Qualified Board Name (FQBN) of your board.

   ```bash
   arduino-cli board listall | grep NodeMCU-32S
   ```

   ![result](https://i.imgur.com/qfcC3KT.png)  
   The fqbn of NodeMCU-32S is _esp32:esp32:nodemcu-32s_

2. Change directory to your target sketch

   ```bash
   cd path/to/sketch
   ```

3. Generate the symbol database of cscope/ctags with arduino-cscope-ctags.

   ```bash
   arduino-cscope-ctags esp32:esp32:nodemcu-32s .
   ls -alh .tags
   ```

   ![](https://i.imgur.com/3oYbRuV.png)  
   ![](https://i.imgur.com/m9G8li7.png)  
   ![](https://i.imgur.com/uZhXUCx.png)  
   Ctags may generate a lot of warning message about ignoring null tags, but that's ok. The program will display 'All done successfully' when there's no error occured during retriving symbols.  
   And the program will generate a directory named '.tags' in the directory of your sketch by default. The symbol database of cscope and ctags are presented in the directory mentioned above.

4. Load symbol database to your text editor.

   ```bash
   vim FreeRTOS_ESP32.ino

   # Command in vim
   :set tags=.tags/ctags
   :cs add .tags/cscope.out
   ```

5. You are done.
   Now you can begin code tracing. For example, we can use `:cs find c setup` to investigate how the task is created and where is the _setup()_ be called at the beging of arduino-esp32.  
   ![](https://i.imgur.com/3t7I1MW.png)  
   ![](https://i.imgur.com/tzK9sda.png)

## How to install

### Dependencies

This tool depends on python, [arduino-cli](https://github.com/arduino/arduino-cli), [cscope](http://cscope.sourceforge.net/) and [ctags](https://github.com/universal-ctags/ctags).  
Specifically, this tool was developed and be tested on the following platform.

- ArchLinux 5.11.16-arch1-1
- Python 3.6
- Arduino-cli 0.18.3
- Cscope 15.9
- Universal Ctags 5.9.0

It shouldn't be any problem if you are using Linux based operating system and python 3.6~3.9. But working on other platform is not guaranteed. If you are encounting any problem to get this tool work, please kindly let me know. The contacting informations are listed below.

### Installing instruction

1. Install python3.6, arduino-cli, cscope and ctags via the package manager of your distrubution.
2. Download the source code of this project.

   ```bash
   git clone https://github.com/ifTNT/arduino-cscope-ctags.git
   cd arduino-cscope-ctags/
   ```

3. Use the following command to install other dependencies.

   ```bash
   sudo pip install -r requirements.txt
   ```

4. Enable executing flag of the main program.

   ```bash
   chmod +x arduino-cscope-ctags
   ```

5. Copy the executable to the system directory.

   ```bash
   sudo cp arduino-cscope-ctags /usr/local/bin/
   #or
   sudo ln -s ${PWD}/arduino-cscope-ctags /usr/local/bin/
   ```

6. Enjoy hacking!

## Command-line arguments

Usage:

```bash
arduino-cscope-ctags [-h] [-o DB_OUTPUT] fqbn sketch_path
```

### Positional arguments

- fqbn : The Fully Qualified Board Name (FQBN) of your target board. It can be obtained by command `arduino-cli board listall`. e.g.: arduino:avr:uno
- sketch_path : The path to your Arduino sketch. Must containing at least one '.ino' file.

### Optional arguments

- -h, --help : show this help message and exit
- -o DB_OUTPUT, --db-output DB_OUTPUT
  - The base output folder related to your sketch directory. Default is the '.tags' folder in your sketch directory.

## How to contribute

Any contribution are welcomed.  
If you encounterd some problem, make a issue on GitHub and we will help you as soon as possible.  
If you have any idea to improve this tool, please let us know through the issue or pull request functionality on GitHub.  
Cause the tested platforms are limited. If this tool works fine on your platform, please create an issue on GitHub with the detailed version of your platform.  
You can also contact us via the e-mail _iftnt1999 [at] gmail.com_. We will apprciate if hearing any feedback from you.
