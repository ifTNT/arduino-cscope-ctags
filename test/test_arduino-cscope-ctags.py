#!/bin/python3

import subprocess
from pathlib import Path
import shutil

test_sketch_path = Path("./test/FreeRTOS_ESP32").absolute()

def test_main_default():
  arduino_cli = subprocess.run([
    "arduino-cscope-ctags",
    "esp32:esp32:nodemcu-32s",
    str(test_sketch_path)
  ], cwd=test_sketch_path)

  tags_path = test_sketch_path/".tags"

  assert tags_path.is_dir()
  assert (tags_path/"cscope.out").is_file()
  assert (tags_path/"cscope.in.out").is_file()
  assert (tags_path/"cscope.po.out").is_file()
  assert (tags_path/"ctags").is_file()

  # Clean up
  shutil.rmtree(tags_path)

def test_main_custom_output():
  arduino_cli = subprocess.run([
    "arduino-cscope-ctags",
    "-o",
    ".tags/custom/",
    "esp32:esp32:nodemcu-32s",
    str(test_sketch_path)
  ], cwd=test_sketch_path)

  tags_path = test_sketch_path/".tags/custom"

  assert tags_path.is_dir()
  assert (tags_path/"cscope.out").is_file()
  assert (tags_path/"cscope.in.out").is_file()
  assert (tags_path/"cscope.po.out").is_file()
  assert (tags_path/"ctags").is_file()

  # Clean up
  shutil.rmtree(test_sketch_path/".tags")