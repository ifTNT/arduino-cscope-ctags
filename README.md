# arduino-cscope-ctags

![License](https://img.shields.io/badge/license-GPLv3-brightgreen)
![CI Status](https://img.shields.io/travis/com/ifTNT/arduino-cscope-ctags)

Generating cross-reference between Arduino sketches, libraries, and cores for code tracing. Navigating under Arduino sketches using cscope/ctags.

## Introduction

Arduino is a convenient and easy-to-use environment for developing embedding applications. On the other hand, tracing the code of Arduino core can help us to realize how the lower-level function was implemented and further assist us in debugging. However, it's tough to work that tracing code with vanilla Arduino IDE, especially with third-party core variants like ESP32.  
Thus, the purpose of this tool is to simplify the work to generate the database of cross-references from the Arduino sketch using cscope and ctags. Once the database is generated, you can begin tracing the code use cscope/ctags with any text editor like vim, emacs, vscode, or sublime text.

## How to Use

### i. The Context of the Example

- Board: NodeMCU-32S
- Third-Party Core: [arduino-esp32](https://github.com/espressif/arduino-esp32/tree/1.0.6)
- Sketch: [ESP32/FreeRTOS](https://github.com/espressif/arduino-esp32/blob/1.0.6/libraries/ESP32/examples/FreeRTOS/FreeRTOS.ino)
- Text Editor: vim

### ii. Usage Guide by Example

1. Query the Fully Qualified Board Name (FQBN) of your board.

   ```bash
   arduino-cli board listall | grep NodeMCU-32S
   ```

   Result:  
   ![result](https://i.imgur.com/qfcC3KT.png)  
   The FQBN of NodeMCU-32S is **esp32:esp32:nodemcu-32s**

2. Change directory to your target sketch

   ```bash
   cd path/to/your/sketch
   ```

3. Generate the database of cross-references with `arduino-cscope-ctags`.

   ```bash
   # arduino-cscope-ctags fqbn path/to/your/sketch
   arduino-cscope-ctags esp32:esp32:nodemcu-32s .

   # Generated cross-references will be placed in ".tags" directory by default.
   ls -alh .tags
   ```

   Result:  
   ![](https://i.imgur.com/VOyidp2.png)  
   ![](https://i.imgur.com/uZhXUCx.png)  
   Ctags may generate a lot of warning messages about ignoring null tags, but that's ok. The program will display "All done successfully" when there's no error occurred during retrieving symbols.  
   And the program will generate a directory named ".tags" in the directory of your sketch by default. The database of cscope and ctags are presented in that directory.

4. Load cross-references to your text editor.

   ```bash
   vim your_sketch_name.ino

   # --- Command in vim ---
   # Load tags to ctags
   :set tags=.tags/ctags
   # Load cross-references to cscope
   :cs add .tags/cscope.out
   ```

5. That's all of the work you need to do.  
   Now you can begin code tracing. For example, we can use `:cs find c setup` to investigate how the task is created and where is the _setup()_ be called at the beginning of arduino-esp32. In addition to that, we can use `Ctrl-]` and `Ctrl-t` to jump between tags.
   ![](https://i.imgur.com/3t7I1MW.png)  
   ![](https://i.imgur.com/tzK9sda.png)  
   You may want to further learn how to use cscope and ctags from the following resources.

   - [The Vim/Cscope Tutorial](http://cscope.sourceforge.net/cscope_vim_tutorial.html)
   - [Ctags Tutorial from University of Washington](https://courses.cs.washington.edu/courses/cse451/10au/tutorials/tutorial_ctags.html)

   Enjoy hacking!

## How to Install

### i. Dependencies

This tool depends on python, [arduino-cli](https://github.com/arduino/arduino-cli), [cscope](http://cscope.sourceforge.net/), and [ctags](https://github.com/universal-ctags/ctags).  
Specifically, this tool was developed and be tested on the following platform on TravisCI.

- ArchLinux, Ubuntu 16.04
- Python >= 3.6
- Arduino-cli == 0.18.3
- Cscope >= 15.8
- Universal Ctags/Exuberant Ctags >= 5.9.0

It shouldn't be any problem if you are using Linux based operating system and python>=3.6. But working on other platforms is not guaranteed. If you are encountering any problems getting this tool to work, please kindly let me know. The contacting information are listed below.

### ii. Installing Instruction

1. Install python3.6, arduino-cli, cscope and ctags via the package manager of your distribution.
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

6. All set. You can then follow the instruction in the previous section to use _arduino-cscope-ctags_.

## Command-line Arguments

Usage:

```bash
arduino-cscope-ctags [-h] [-o DB_OUTPUT] fqbn sketch_path
```

### i. Positional Arguments

- fqbn : The Fully Qualified Board Name (FQBN) of your target board. It can be obtained by command `arduino-cli board listall`.
  - e.g. arduino:avr:uno
- sketch_path : The path to your Arduino sketch. Must contain at least one ".ino" file.

### ii. Optional Arguments

- -h, --help : show the help message and exit
- -o DB_OUTPUT, --db-output DB_OUTPUT
  - The base output folder of cross-references related to your sketch directory. Default is the ".tags" folder in your sketch directory.

## Limitations and Known Issues

Although this project is a useful tool, there are still existed some limitations of this project.

1. **Doesn't support Windows.** The project is developed and be tested on Linux. The support of Windows is one of the future works.
2. **Can't trace pre-compiled binary.** Cscope and ctags are born for code tracing. However, all of the core implementation involved in trade secrets are released in the pre-compiled binary format. So there is always some floor in the code that we can't further dig into with cscope/ctags.

## How to Contribute

This project is under the **GNU General Public License version 3 (GPLv3)**. Any contributions are welcomed.  
If you encountered some problem, make an issue on GitHub and we will help you as soon as possible.  
If you have any idea to improve this tool, please let us know through the issue or pull request functionality on GitHub.  
Cause the tested platforms are limited. If this tool works fine on your platform, please create an issue on GitHub with the detailed version of your platform.  
You can also contact us via the e-mail _iftnt1999 [at] gmail.com_. We will appreciate if hearing any feedback from you.
